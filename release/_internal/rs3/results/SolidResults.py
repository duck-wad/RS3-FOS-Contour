from typing import Optional, Union
import grpc

import rs3.generatedFiles.SolidsResultsQueryService_pb2_grpc as SolidsResultsQueryService_pb2_grpc
import rs3.generatedFiles.SolidsResultsQueryService_pb2 as SolidsResultsQueryService_pb2

from rs3._proxyObject import _ProxyObject
from rs3._client import Client

from rs3.Geometry import Cube, Cylinder, Sphere
from rs3.results.SolidElementResults import SolidElementResults
from rs3.results.SolidNodalResults import SolidNodalResults, SolidsDataType

class SolidResults(_ProxyObject):
    '''
    Entry point to query solid nodal/element results for a given stage and SRF.

    Parameters:
        stageNumber (int): 1-based stage index.
        srfResultIndex (int): 0-based SRF value index. 0 is to query SRF-None values.

    Notes:
        - entityName is trimmed; empty strings are ignored.
        - region=None leaves the proto field unset (service returns all).
        - Exceptions from the underlying service are propagated as-is by the client.

    Examples:
        See :ref:`solid_result_example`.
    '''
    def __init__(self, client: Client, projectId: str, stageNumber: int, srfResultIndex: int, requiredDataTypes: Optional[set[SolidsDataType]] = None):
        super().__init__(client, projectId)
        self._queryService = SolidsResultsQueryService_pb2_grpc.SolidResultsQueryServiceStub(self._client.channel)
        self._stageNumber = stageNumber
        self._srfResultIndex = srfResultIndex
        self._requiredDataTypes = requiredDataTypes

    @staticmethod
    def createWithAvailabilityCheck(client: Client, projectId: str, stageNumber: int, srfResultIndex: int, requiredDataTypes: Optional[set[SolidsDataType]] = None) -> 'SolidResults':
        '''
        Check results availability and create a SolidResults instance if available.

        This method first checks if results are available for the specified stage, SRF value, and data types.
        If results are not available, it raises an exception. Otherwise, it creates and returns a SolidResults instance.

        Parameters:
            client: Client
                The gRPC client instance.
            projectId: str
                The project ID.
            stageNumber: int
                1-based stage index.
            srfResultIndex: int
                0-based SRF value index. 0 is to query SRF-None values.
            requiredDataTypes: Optional[set[SolidsDataType]]
                A set of SolidsDataType enum values to check availability for. 
                If None or empty, all data types are queried.

        Returns:
            SolidResults: A SolidResults instance if results are available.

        Raises:
            Exception: If results are not available for the specified stage, SRF value, and data types.
        '''
        if requiredDataTypes is None or len(requiredDataTypes) == 0:
            # When no specific data types are required, query all available data types
            requiredDataTypes = set(SolidsDataType)
        
        queryService = SolidsResultsQueryService_pb2_grpc.SolidResultsQueryServiceStub(client.channel)
        
        request = SolidsResultsQueryService_pb2.SolidResultsByDataTypesQueryRequest(
            _projectId=projectId,
            stageNumber=stageNumber,
            srfValueNumber=srfResultIndex,
            requiredDataTypes=[dt.name for dt in requiredDataTypes]
        )
        
        response = queryService.ReadResultsByStageSRFValueAndDataTypes(request)
        if not response.resultsAvailable:
            raise Exception(f"Results are not available for stage {stageNumber}, SRF result index {srfResultIndex}, and required data types: {[dt.name for dt in requiredDataTypes]}")
        
        return SolidResults(client, projectId, stageNumber, srfResultIndex, requiredDataTypes)

    
    def getMeshNodeResults(self, entityName: Optional[str] = None, region: Optional[Union[Cube, Cylinder, Sphere]] = None, includeIntersecting: bool = True) -> list[SolidNodalResults]:
        '''
        Query solid nodal results at a specific stage and SRF value.
        Parameters:
            entityName: Optional[str]: If provided, only nodes belonging to the specified entity are queried.
            region: Optional[Union[Cube, Cylinder, Sphere]]: Sample region filter. When None, the field is not set in the request (proto3 unset), and the service returns all nodes.
            includeIntersecting: bool: If True, nodes that intersect the sample region are included. When False, only nodes fully contained are included. Ignored when region is None.
        Raises:
            Exception if:
                - stageNumber is less than 1
                - stageNumber 
                is greater than the number of stages in the project
                - _srfResultIndex is less than 0
                - _srfResultIndex is greater than the number of SRF values in the project
        Returns:
            list[SolidNodalResults]: A list of solid nodal results wrappers for the requested stage and SRF value.
        '''
        request = self._makeNodalRequest(entityName, region, includeIntersecting) 

        # Call streaming RPC and process chunks as they arrive
        stream = self._queryService.QuerySolidNodalResults(request)

        # Extract header from first chunk and accumulate data from subsequent chunks
        allResults = []
        totalQueriedNodesCount = None
        dataTypeToIndexMap: dict[SolidsDataType, int] = {}
        
        for chunk in stream:
            if chunk.HasField('header'):
                # Process header chunk
                header = chunk.header
                totalQueriedNodesCount = header.totalQueriedNodesCount
                # Convert string keys to SolidsDataType enum
                for dataTypeName, index in header.dataTypeNameToIndexMap.items():
                    dataTypeToIndexMap[SolidsDataType[dataTypeName]] = index
            elif chunk.HasField('data'):
                # Process data chunk
                allResults.extend(chunk.data.results)

        if totalQueriedNodesCount != len(allResults):
            raise RuntimeError(f"Number of nodes received does not match the expected total queried nodes count. Expected {totalQueriedNodesCount}, but received {len(allResults)}.")
        

        return [
            SolidNodalResults(r, dataTypeToIndexMap) 
            for r in allResults
        ]


    def _makeNodalRequest(self, entityName: Optional[str], region: Optional[Union[Cube, Cylinder, Sphere]], includeIntersecting: bool = True) -> SolidsResultsQueryService_pb2.SolidNodalResultsQueryRequest:
        request = SolidsResultsQueryService_pb2.SolidNodalResultsQueryRequest(
            baseRequest=self._makeRequest(entityName, region, includeIntersecting),
            requiredDataTypes=[dt.name for dt in self._requiredDataTypes]
        )
        return request

    def _makeRequest(self, entityName: Optional[str], region: Optional[Union[Cube, Cylinder, Sphere]], includeIntersecting: bool = True) -> SolidsResultsQueryService_pb2.SolidResultsQueryRequest:       
        request = SolidsResultsQueryService_pb2.SolidResultsQueryRequest(
            _projectId=self._objectId,
            stageNumber=self._stageNumber,
            srfValueNumber=self._srfResultIndex)
        
        if entityName is not None:
            entityName = entityName.strip()
            if entityName:
                request.entityName = entityName
        
        if region is not None:
            if isinstance(region, (Cube, Cylinder, Sphere)):
                common_region = region.toCommonGeometryObject()
                request.sampleRegion.region.CopyFrom(common_region)
                request.sampleRegion.includeIntersecting = includeIntersecting
            else:
                raise TypeError(f"Unsupported region type: {type(region)}")

        return request


    def getMeshElementResults(self, entityName: Optional[str] = None, region: Optional[Union[Cube, Cylinder, Sphere]] = None, includeIntersecting: bool = True) -> list[SolidElementResults]:
        '''
        Query solid element results at a specific stage and SRF value via streaming.
        Parameters:
            entityName: Optional[str]: If provided, only elements belonging to the specified entity are queried.
            region: Optional[Union[Cube, Cylinder, Sphere]]: Sample region filter. When None, the field is not set in the request (proto3 unset), and the service returns all elements.
            includeIntersecting: bool: If True, elements that intersect the sample region are included. When False, only elements fully contained are included. Ignored when region is None.
        Raises:
            Exception if:
                - stageNumber is less than 1
                - stageNumber is greater than the number of stages in the project
                - _srfResultIndex is less than 0
                - _srfResultIndex is greater than the number of SRF values in the project
        Returns:
            list[SolidElementResults]: A list of solid element results wrappers for the requested stage and SRF value.
        '''
        request = self._makeRequest(entityName, region, includeIntersecting)

        # Call streaming RPC and process chunks as they arrive
        stream = self._queryService.QuerySolidElementResults(request)

        # Extract header from first chunk and accumulate data from subsequent chunks
        has_user_data = False
        user_data_map: dict[str, int] = {}
        all_results = []
        total_queried_elements_count = None 

        for chunk in stream:
            if chunk.HasField('header'):
                # Process header chunk
                header = chunk.header
                has_user_data = header.hasUserData
                total_queried_elements_count = header.totalQueriedElementsCount
                user_data_map = dict(header.userDataNameToResultIndexMap)
            elif chunk.HasField('data'):
                # Process data chunk
                all_results.extend(chunk.data.results)

        if total_queried_elements_count != len(all_results):
            raise RuntimeError(f"Number of elements received does not match the expected total queried elements count. Expected {total_queried_elements_count}, but received {len(all_results)}.")
        
        return [
            SolidElementResults(r, has_user_data, user_data_map) 
            for r in all_results
        ]

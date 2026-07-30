from typing import Optional, Union
import rs3.generatedFiles.JointResultsQueryService_pb2_grpc as JointResultsQueryService_pb2_grpc
import rs3.generatedFiles.ResultsQueryCommonMessage_pb2 as ResultsQueryCommonMessage_pb2
from rs3._proxyObject import _ProxyObject
from rs3._client import Client
from rs3.Geometry import Cube, Cylinder, Sphere
from rs3.results.ResultEnums import *

class JointNodalResults:
    '''
    Nodal result wrapper with per-material data access.

    Notes:
        - EntityNames/EntityIDs correspond to owning entities for this node.
    '''
    def __init__(self, grpcNodalResults):
        self._grpcNodalResults = grpcNodalResults
        
    @property
    def EntityName(self):
        return self._grpcNodalResults.entityInformation.name

    @property
    def EntityID(self):
        return self._grpcNodalResults.entityInformation.ID
    
    @property
    def NodeID(self):
        return self._grpcNodalResults.nodeInformation.nodeID

    @property
    def XCoordinate(self):
        return self._grpcNodalResults.nodeInformation.location.x
    
    @property
    def YCoordinate(self):
        return self._grpcNodalResults.nodeInformation.location.y
    
    @property
    def ZCoordinate(self):
        return self._grpcNodalResults.nodeInformation.location.z 
    
class JointElementResults:
    '''
    Element-level results wrapper for a specific stage/SRF context.

    Notes:
        - AttachedNodes returns a copy of node IDs; modifying it does not affect internal state.
    '''
    def __init__(self, grpcElementResults):
        self._grpcElementResults = grpcElementResults
        self._jointResults = grpcElementResults.jointNodalResults
    
    @property
    def ElementID(self):
        return self._grpcElementResults.elementInformation.elementID
    
    @property
    def AttachedNodeIDs(self):
        return list(self._grpcElementResults.elementInformation.nodeIDs)

    @property
    def EntityName(self):
        return self._grpcElementResults.entityInformation.name

    @property
    def EntityID(self):
        return self._grpcElementResults.entityInformation.ID

    @property
    def FailureType(self):
        return JointGaussPointFailureCombinations(self._grpcElementResults.failureType)
    
    def getResults(self, dataType: InterfaceResultTypes) -> list[float]:
        if not self._jointResults:
            raise ValueError("No joint results available")

        result = self._jointResults[0]
        return getattr(result, dataType.value)   

class JointResults(_ProxyObject):
    '''
    Entry point to query joint nodal/element results for a given stage and SRF.

    Parameters:
        stageNumber (int): 1-based stage index.
        srfResultIndex (int): 0-based SRF value index. 0 is to query SRF-None values.

    Notes:
        - entityName is trimmed; empty strings are ignored.
        - region=None leaves the proto field unset (service returns all).
        - Exceptions from the underlying service are propagated as-is by the client.

    Examples:
        See :ref:`joint_result_example`.
    '''

    def __init__(self, client: Client, projectId: str, stageNumber: list[int], srfResultIndex: int):
        super().__init__(client, projectId)
        self._queryService = JointResultsQueryService_pb2_grpc.JointResultsQueryServiceStub(self._client.channel)
        self._stageNumber = stageNumber
        self._srfResultIndex = srfResultIndex
    
    def getJointNodeResults(self, entityNames: Optional[list[str]] = None, region: Optional[Union[Cube, Cylinder, Sphere]] = None, includeIntersecting: bool = True) -> list[JointNodalResults]:
        request = self._makeRequest(entityNames, region, includeIntersecting)     
        stream = self._queryService.GetJointNodeResults(request)
        
        results = []
        totalQueriedNodesCount = None
        
        for chunk in stream:
            if chunk.HasField('header'):
                header = chunk.header
                totalQueriedNodesCount = header.totalQueriedNodesCount
            elif chunk.HasField('data'):
                results.extend(chunk.data.results)
                
        if totalQueriedNodesCount != len(results):
            raise RuntimeError(f"Number of nodes received does not match the expected total queried nodes count. Expected {totalQueriedNodesCount}, but received {len(results)}")
                    
        return [JointNodalResults(r) for r in results]
    
    def getJointElementResults(self, entityName: Optional[str] = None, region: Optional[Union[Cube, Cylinder, Sphere]] = None, includeIntersecting: bool = True) -> list[JointElementResults]:
        request = self._makeRequest(entityName, region, includeIntersecting)        
        stream = self._queryService.GetJointElementResults(request)
        
        results = []
        totalQueriedElementsCount = None
        
        for chunk in stream:
            if chunk.HasField('header'):
                header = chunk.header
                totalQueriedElementsCount = header.totalQueriedElementsCount
            elif chunk.HasField('data'):
                results.extend(chunk.data.results)
                
        if totalQueriedElementsCount != len(results):
            raise RuntimeError(f"Number of elements received does not match the expected total queried elements count. Expected {totalQueriedElementsCount}, but received {len(results)}")

        return [JointElementResults(r) for r in results]

    def _makeRequest(self, entityName: Optional[str], region: Optional[Union[Cube, Cylinder, Sphere]], includeIntersecting: bool = True) -> ResultsQueryCommonMessage_pb2.ResultsQueryRequest:       
        request = ResultsQueryCommonMessage_pb2.ResultsQueryRequest(
            _projectId=self._objectId,
            stageNumber=self._stageNumber,
            srfValueNumber=self._srfResultIndex)
        
        if entityName:
        # Trim whitespace inside each string if needed
            request.entityName = entityName.strip()
        
        if region is not None:
            if isinstance(region, (Cube, Cylinder, Sphere)):
                common_region = region.toCommonGeometryObject()
                request.sampleRegion.region.CopyFrom(common_region)
                request.sampleRegion.includeIntersecting = includeIntersecting
            else:
                raise TypeError(f"Unsupported region type: {type(region)}")

        return request

from typing import Optional, Union, List, Dict, Tuple

import rs3.generatedFiles.BeamsResultsQueryService_pb2_grpc as BeamsResultsQueryService_pb2_grpc

from rs3._client import Client

from rs3.Geometry import Cube, Cylinder, Sphere
from rs3.results.ResultsCommon import _NodeValuePairCollection, _ResultsQueryBase
from rs3.results.YieldedElement import YieldedElement
from rs3.results.ResultEnums import BeamsDataType, BeamForepolePileGaussPointFailureType


class BeamNodeResults:
    def __init__(self, grpcNodalResults):
        self._grpcNodalResults = grpcNodalResults

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
    
    @property
    def EntityName(self):
        return self._grpcNodalResults.entityInformation.name
    
    @property
    def EntityID(self):
        return self._grpcNodalResults.entityInformation.ID

class BeamElementResults:
    def __init__(self, grpcElementResults):
        self._grpcElementResults = grpcElementResults
        self._nodeResultsByDataType = self._buildNodeResultsByDataType(grpcElementResults)
        self._yieldedElement = YieldedElement(grpcElementResults.failurePoint, failureTypeEnum=BeamForepolePileGaussPointFailureType) if grpcElementResults.HasField('failurePoint') else None

    @property
    def ElementID(self):
        return self._grpcElementResults.elementInformation.elementID

    @property
    def EntityName(self):
        return self._grpcElementResults.entityInformation.name

    @property
    def EntityID(self):
        return self._grpcElementResults.entityInformation.ID

    @property
    def AttachedNodeIDs(self):
        return self._grpcElementResults.elementInformation.nodeIDs

    
    def getNodeResult(self, dataType: BeamsDataType) -> List[float]:
        if dataType not in self._nodeResultsByDataType:
            raise ValueError(f"Data type {dataType} not found")
        return self._nodeResultsByDataType[dataType].ResultValues

    
    def getResultsInNodeDataTuple(self, dataType: BeamsDataType) -> List[Tuple[int, float]]:
        if dataType not in self._nodeResultsByDataType:
            raise ValueError(f"Data type {dataType} not found")
        return self._nodeResultsByDataType[dataType].NodeValuePairs
        
    
    @property
    def YieldedElement(self):
        return self._yieldedElement

    
    def _buildNodeResultsByDataType(self, grpcElementResults):
        nodeIdResultPairs = [(nodeID, nodeValue) for nodeID, nodeValue in zip(grpcElementResults.elementInformation.nodeIDs, grpcElementResults.nodeValues)]
        pairsByType: Dict[BeamsDataType, List[tuple[int, float]]] = {dt: [] for dt in BeamsDataType}
        for nodeID, nodeValue in nodeIdResultPairs:
            pairsByType[BeamsDataType.AXIS_FORCE].append((nodeID, nodeValue.axisForce))
            pairsByType[BeamsDataType.SHEAR_FORCE_MIN_AXIS].append((nodeID, nodeValue.shearForceMinAxis))
            pairsByType[BeamsDataType.SHEAR_FORCE_MAX_AXIS].append((nodeID, nodeValue.shearForceMaxAxis))
            pairsByType[BeamsDataType.MOMENT_MIN_AXIS].append((nodeID, nodeValue.momentMinAxis))
            pairsByType[BeamsDataType.MOMENT_MAX_AXIS].append((nodeID, nodeValue.momentMaxAxis))
            pairsByType[BeamsDataType.DISPLACEMENT_X].append((nodeID, nodeValue.displacementX))
            pairsByType[BeamsDataType.DISPLACEMENT_Y].append((nodeID, nodeValue.displacementY))
            pairsByType[BeamsDataType.DISPLACEMENT_Z].append((nodeID, nodeValue.displacementZ))
            pairsByType[BeamsDataType.DISPLACEMENT_TOTAL].append((nodeID, nodeValue.totalDisplacement))

        return {dt: _NodeValuePairCollection(pairs) for dt, pairs in pairsByType.items()}



class BeamResults(_ResultsQueryBase):
    '''
    Entry point to query beam nodal results for a given stage and SRF.

    Parameters:
        stageNumber (int): 1-based stage index.
        srfResultIndex (int): 0-based SRF value index. 0 is to query SRF-None values.

    Notes:
        - entityName is trimmed; empty strings are ignored.
        - region=None leaves the proto field unset (service returns all).
        - Exceptions from the underlying service are propagated as-is by the client.

    Examples:
        See :ref:`beam_result_example`.
    '''

    def __init__(self, client: Client, projectId: str, stageNumber: int, srfResultIndex: int):
        super().__init__(client, projectId, stageNumber, srfResultIndex)
        self._queryService = BeamsResultsQueryService_pb2_grpc.BeamResultsQueryServiceStub(client.channel)

    
    def getBeamNodeResults(self, entityName: Optional[str] = None, region: Optional[Union[Cube, Cylinder, Sphere]] = None, includeIntersecting: bool = True) -> list[BeamNodeResults]:
        '''
        Query beam nodal results at a specific stage and SRF value.
        Parameters:
            entityName: Optional[str]: If provided, only nodes belonging to the specified entity are queried.
            region: Optional[Union[Cube, Cylinder, Sphere]]: Sample region filter. When None, the field is not set in the request (proto3 unset), and the service returns all nodes.
            includeIntersecting: bool: If True, nodes that intersect the sample region are included. When False, only nodes fully contained are included. Ignored when region is None.
        Raises:
            Exception if:
                - stageNumber is less than 1
                - stageNumber is greater than the number of stages in the project
                - _srfResultIndex is less than 0
                - _srfResultIndex is greater than the number of SRF values in the project
        Returns:
            list[BeamNodalResults]: A list of beam nodal results wrappers for the requested stage and SRF value.
        '''
        request = self._makeRequest(entityName, region, includeIntersecting)
        stream = self._queryService.QueryBeamNodalResults(request)
        allResults = []
        totalQueriedNodesCount = None
        for chunk in stream:
            if chunk.HasField('header'):
                header = chunk.header
                totalQueriedNodesCount = header.totalQueriedNodesCount
            elif chunk.HasField('data'):
                allResults.extend(chunk.data.results)
        if totalQueriedNodesCount is not None and totalQueriedNodesCount != len(allResults):
            raise RuntimeError(f"Number of nodes received does not match the expected total queried nodes count. Expected {totalQueriedNodesCount}, but received {len(allResults)}.")
        return [BeamNodeResults(r) for r in allResults]



    def getBeamElementResults(self, entityName: Optional[str] = None, region: Optional[Union[Cube, Cylinder, Sphere]] = None, includeIntersecting: bool = True) -> list[BeamElementResults]:
        '''
        Query beam element results at a specific stage and SRF value.
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
            list[BeamElementResults]: A list of beam element results wrappers for the requested stage and SRF value.
        '''
        request = self._makeRequest(entityName, region, includeIntersecting)
        stream = self._queryService.QueryBeamElementResults(request)
        allResults = []
        totalQueriedElementsCount = None
        for chunk in stream:
            if chunk.HasField('header'):
                header = chunk.header
                totalQueriedElementsCount = header.totalQueriedElementsCount
            elif chunk.HasField('data'):
                allResults.extend(chunk.data.results)
        if totalQueriedElementsCount != len(allResults):
            raise RuntimeError(f"Number of elements received does not match the expected total queried elements count. Expected {totalQueriedElementsCount}, but received {len(allResults)}.")
        return [BeamElementResults(r) for r in allResults]
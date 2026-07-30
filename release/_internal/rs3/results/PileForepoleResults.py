from typing import List, Dict, Union, Optional, Tuple

import rs3.generatedFiles.PileForepoleResultsQueryService_pb2_grpc as PileForepoleResultsQueryService_pb2_grpc

from rs3._client import Client

from rs3.results.ResultsCommon import _NodeValuePairCollection, _ResultsQueryBase
from rs3.results.ResultEnums import BeamsDataType, PileInterfaceDataType, BeamForepolePileGaussPointFailureType
from rs3.results.YieldedElement import YieldedElement
from rs3.Geometry import Cube, Cylinder, Sphere


class PileNodeResults:
    def __init__(self, grpcNodeResults):
        self._grpcNodeResults = grpcNodeResults
    
    @property
    def NodeID(self):
        return self._grpcNodeResults.nodeInformation.nodeID
    
    @property
    def XCoordinate(self):
        return self._grpcNodeResults.nodeInformation.location.x
    
    @property
    def YCoordinate(self):
        return self._grpcNodeResults.nodeInformation.location.y
    
    @property
    def ZCoordinate(self):
        return self._grpcNodeResults.nodeInformation.location.z
    
    @property
    def EntityName(self):
        return self._grpcNodeResults.entityInformation.name
    
    @property
    def EntityID(self):
        return self._grpcNodeResults.entityInformation.ID

    @property
    def PileID(self):
        return self._grpcNodeResults.indexToPattern



class PileForepoleElementResults:
    def __init__(self, grpcElementResults):
        self._grpcElementResults = grpcElementResults
        self._nodeResultsByDataType = self._buildNodeResultsByDataType(grpcElementResults)
        self._yieldedElement = YieldedElement(grpcElementResults.failurePoint, failureTypeEnum=BeamForepolePileGaussPointFailureType) if grpcElementResults.HasField('failurePoint') else None
        self._interfaceYieldedElement = YieldedElement(grpcElementResults.interfaceFailurePoint, failureTypeEnum=BeamForepolePileGaussPointFailureType) if grpcElementResults.HasField('interfaceFailurePoint') else None
    
    @property
    def EntityName(self):
        return self._grpcElementResults.entityInformation.name

    @property
    def EntityID(self):
        return self._grpcElementResults.entityInformation.ID

    @property
    def AttachedNodeIDs(self):
        return self._grpcElementResults.nodeIDs

    @property
    def PileID(self):
        return self._grpcElementResults.pileID

    @property
    def BeamID(self):
        return self._grpcElementResults.beamElementID

    @property
    def InterfaceID(self):
        return self._grpcElementResults.interfaceElementID

    def getNodeResult(self, dataType: Union[BeamsDataType, PileInterfaceDataType]) -> List[float]:
        key = (type(dataType), dataType)
        if key not in self._nodeResultsByDataType:
            raise ValueError(f"Data type {dataType} not found")
        return self._nodeResultsByDataType[key].ResultValues


    def getResultsInNodeDataTuple(self, dataType: Union[BeamsDataType, PileInterfaceDataType]) -> List[Tuple[int, float]]:
        key = (type(dataType), dataType)
        if key not in self._nodeResultsByDataType:
            raise ValueError(f"Data type {dataType} not found")
        return self._nodeResultsByDataType[key].NodeValuePairs


    @property
    def YieldedElement(self):
        return self._yieldedElement

    @property
    def InterfaceYieldedElement(self):
        return self._interfaceYieldedElement

    
    def _buildNodeResultsByDataType(self, grpcElementResults):
        nodeIDElementValuePairs = [(nodeID, nodeValue) for nodeID, nodeValue in zip(grpcElementResults.nodeIDs, grpcElementResults.nodeValues.elementNodeValues)]
        nodeIDInterfaceValuePairs = [(nodeID, nodeValue) for nodeID, nodeValue in zip(grpcElementResults.nodeIDs, grpcElementResults.nodeValues.interfaceNodeValues)]
        beamNodePairsByType: Dict[BeamsDataType, List[tuple[int, float]]] = {dt: [] for dt in BeamsDataType}
        for nodeID, nodeValue in nodeIDElementValuePairs:
            beamNodePairsByType[BeamsDataType.AXIS_FORCE].append((nodeID, nodeValue.axisForce))
            beamNodePairsByType[BeamsDataType.SHEAR_FORCE_MIN_AXIS].append((nodeID, nodeValue.shearForceMinAxis))
            beamNodePairsByType[BeamsDataType.SHEAR_FORCE_MAX_AXIS].append((nodeID, nodeValue.shearForceMaxAxis))
            beamNodePairsByType[BeamsDataType.MOMENT_MIN_AXIS].append((nodeID, nodeValue.momentMinAxis))
            beamNodePairsByType[BeamsDataType.MOMENT_MAX_AXIS].append((nodeID, nodeValue.momentMaxAxis))
            beamNodePairsByType[BeamsDataType.DISPLACEMENT_X].append((nodeID, nodeValue.displacementX))
            beamNodePairsByType[BeamsDataType.DISPLACEMENT_Y].append((nodeID, nodeValue.displacementY))
            beamNodePairsByType[BeamsDataType.DISPLACEMENT_Z].append((nodeID, nodeValue.displacementZ))
            beamNodePairsByType[BeamsDataType.DISPLACEMENT_TOTAL].append((nodeID, nodeValue.totalDisplacement))
        interfaceNodePairsByType: Dict[PileInterfaceDataType, List[tuple[int, float]]] = {dt: [] for dt in PileInterfaceDataType}
        for nodeID, nodeValue in nodeIDInterfaceValuePairs:
            interfaceNodePairsByType[PileInterfaceDataType.SHEAR_FORCE].append((nodeID, nodeValue.shearForce))
            interfaceNodePairsByType[PileInterfaceDataType.NORMAL_FORCE_MIN_AXIS].append((nodeID, nodeValue.normalForceMinAxis))
            interfaceNodePairsByType[PileInterfaceDataType.NORMAL_FORCE_MAX_AXIS].append((nodeID, nodeValue.normalForceMaxAxis))
            interfaceNodePairsByType[PileInterfaceDataType.CONFINING_STRESS].append((nodeID, nodeValue.confiningStress))
            interfaceNodePairsByType[PileInterfaceDataType.DISPLACEMENT_X].append((nodeID, nodeValue.rockDisplacementX))
            interfaceNodePairsByType[PileInterfaceDataType.DISPLACEMENT_Y].append((nodeID, nodeValue.rockDisplacementY))
            interfaceNodePairsByType[PileInterfaceDataType.DISPLACEMENT_Z].append((nodeID, nodeValue.rockDisplacementZ))
            interfaceNodePairsByType[PileInterfaceDataType.DISPLACEMENT_TOTAL].append((nodeID, nodeValue.rockTotalDisplacement))

        # Use (type(dt), dt) as key so BeamsDataType and PileInterfaceDataType entries with same
        # enum value (e.g. DISPLACEMENT_TOTAL) are stored separately; str Enum equality would
        # otherwise collapse them into one key.
        nodeResultsByType: Dict[Tuple[type, Union[BeamsDataType, PileInterfaceDataType]], _NodeValuePairCollection] = {}
        for dt, pairs in beamNodePairsByType.items():
            nodeResultsByType[(BeamsDataType, dt)] = _NodeValuePairCollection(pairs)
        for dt, pairs in interfaceNodePairsByType.items():
            nodeResultsByType[(PileInterfaceDataType, dt)] = _NodeValuePairCollection(pairs)

        return nodeResultsByType



class PileForepoleResults(_ResultsQueryBase):
    '''
    Entry point to query pile forepole nodal/element results for a given stage and SRF.

    Parameters:
        stageNumber (int): 1-based stage index.
        srfResultIndex (int): 0-based SRF value index. 0 is to query SRF-None values.

    Notes:
        - entityName is trimmed; empty strings are ignored.
        - region=None leaves the proto field unset (service returns all).
        - Exceptions from the underlying service are propagated as-is by the client.

    Examples:
        See :ref:`pile_result_example`.
    '''
    def __init__(self, client: Client, projectId: str, stageNumber: int, srfResultIndex: int):
        super().__init__(client, projectId, stageNumber, srfResultIndex)
        self._queryService = PileForepoleResultsQueryService_pb2_grpc.PileForepoleResultsQueryServiceStub(client.channel)

    
    def getPileForepoleNodeResults(self, entityName: Optional[str] = None, region: Optional[Union[Cube, Cylinder, Sphere]] = None, includeIntersecting: bool = True) -> list[PileNodeResults]:
        '''
        Query pile forepole node results at a specific stage and SRF value.
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
            list[PileNodeResults]: A list of pile forepole node results wrappers for the requested stage and SRF value.
        '''
        request = self._makeRequest(entityName, region, includeIntersecting)
        stream = self._queryService.QueryPileForepoleNodeResults(request)
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
        return [PileNodeResults(r) for r in allResults]
    

    def getPileForepoleElementResults(self, entityName: Optional[str] = None, region: Optional[Union[Cube, Cylinder, Sphere]] = None, includeIntersecting: bool = True) -> list[PileForepoleElementResults]:
        '''
        Query pile forepole element results at a specific stage and SRF value.
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
            list[PileForepoleElementResults]: A list of pile forepole element results wrappers for the requested stage and SRF value.
        '''
        request = self._makeRequest(entityName, region, includeIntersecting)
        stream = self._queryService.QueryPileForepoleElementResults(request)
        allResults = []
        totalQueriedElementsCount = None
        for chunk in stream:
            if chunk.HasField('header'):
                header = chunk.header
                totalQueriedElementsCount = header.totalQueriedElementsCount
            elif chunk.HasField('data'):
                allResults.extend(chunk.data.results)
        if totalQueriedElementsCount is not None and totalQueriedElementsCount != len(allResults):
            raise RuntimeError(f"Number of elements received does not match the expected total queried elements count. Expected {totalQueriedElementsCount}, but received {len(allResults)}.")
        return [PileForepoleElementResults(r) for r in allResults]
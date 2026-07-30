from typing import Optional, Union, List, Dict, Tuple

import rs3.generatedFiles.BoltsResultsQueryService_pb2_grpc as BoltsResultsQueryService_pb2_grpc

from rs3._client import Client

from rs3.results.ResultsCommon import _ResultsQueryBase, _NodeValuePairCollection
from rs3.results.YieldedElement import YieldedElement
from rs3.results.ResultEnums import BoltDataType, BoltGaussPointFailureType
from rs3.Geometry import Cube, Cylinder, Sphere


class BoltNodeResult:
    def __init__(self, grpcNodalResult):
        self._grpcNodalResult = grpcNodalResult

    @property
    def NodeID(self):
        return self._grpcNodalResult.nodeInformation.nodeID

    @property
    def XCoordinate(self):
        return self._grpcNodalResult.nodeInformation.location.x

    @property
    def YCoordinate(self):
        return self._grpcNodalResult.nodeInformation.location.y

    @property
    def ZCoordinate(self):
        return self._grpcNodalResult.nodeInformation.location.z

    @property
    def EntityName(self):
        return self._grpcNodalResult.entityInformation.name

    @property
    def EntityID(self):
        return self._grpcNodalResult.entityInformation.ID

    @property
    def BoltIndex(self) -> int:
        '''
        Get the bolt index for this node.
        
        The boltIndex is an integer index that identifies which bolt or bolt pattern instance
        this node belongs to. The indexing starts at 1 (1-based).
        
        - For a single bolt: The boltIndex is a sequential index (1, 2, 3, ...) that uniquely
          identifies each individual bolt in the model.
        - For a bolt pattern: The boltIndex represents the index of the bolt instance within
          the pattern. All nodes belonging to the same bolt instance in a pattern will
          have the same boltIndex value.
        
        Returns:
            int: The bolt index for this node, starting from 1.
        '''
        return self._grpcNodalResult.indexToPattern


class BoltElementResults:
    def __init__(self, grpcElementResults):
        self._grpcElementResults = grpcElementResults
        self._nodeResultsByDataType = self._buildNodeResultsByDataType(grpcElementResults)
        self._yieldedElement = YieldedElement(grpcElementResults.failurePoint, failureTypeEnum=BoltGaussPointFailureType) if grpcElementResults.HasField('failurePoint') else None

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
    def NodeIDs(self):
        return list(self._grpcElementResults.elementInformation.nodeIDs)

    def getNodeResult(self, dataType: BoltDataType) -> List[float]:
        if dataType not in self._nodeResultsByDataType:
            raise ValueError(f"Data type {dataType} not found")
        return self._nodeResultsByDataType[dataType].ResultValues

    def getResultsInNodeDataTuple(self, dataType: BoltDataType) -> List[Tuple[int, float]]:
        if dataType not in self._nodeResultsByDataType:
            raise ValueError(f"Data type {dataType} not found")
        return self._nodeResultsByDataType[dataType].NodeValuePairs

    @property
    def BoltIndex(self) -> int:
        '''
        Get the bolt index for this element.
        
        The boltIndex is an integer index that identifies which bolt or bolt pattern instance
        this element belongs to. The indexing starts at 1 (1-based).
        
        - For a single bolt: The boltIndex is a sequential index (1, 2, 3, ...) that uniquely
          identifies each individual bolt in the model.
        - For a bolt pattern: The boltIndex represents the index of the bolt instance within
          the pattern. All elements belonging to the same bolt instance in a pattern will
          have the same boltIndex value.
        
        Returns:
            int: The bolt index for this element, starting from 1.
        '''
        return self._grpcElementResults.boltID

    @property
    def YieldedElement(self):
        return self._yieldedElement


    def _buildNodeResultsByDataType(self, grpcElementResults):
        nodeIdResultPairs = [(nodeID, nodeValue) for nodeID, nodeValue in zip(grpcElementResults.elementInformation.nodeIDs, grpcElementResults.nodeValues)]
        pairsByType: Dict[BoltDataType, List[tuple[int, float]]] = {dt: [] for dt in BoltDataType}
        for nodeID, nodeValue in nodeIdResultPairs:
            pairsByType[BoltDataType.AXIAL_FORCE].append((nodeID, nodeValue.axisForce))
            pairsByType[BoltDataType.AXIAL_STRESS].append((nodeID, nodeValue.axisStress))
            pairsByType[BoltDataType.DISPLACEMENT_X].append((nodeID, nodeValue.displacementX))
            pairsByType[BoltDataType.DISPLACEMENT_Y].append((nodeID, nodeValue.displacementY))
            pairsByType[BoltDataType.DISPLACEMENT_Z].append((nodeID, nodeValue.displacementZ))
            pairsByType[BoltDataType.DISPLACEMENT_TOTAL].append((nodeID, nodeValue.displacementTotal))
            pairsByType[BoltDataType.INTERFACE_SHEAR_FORCE].append((nodeID, nodeValue.interfaceShearForce))
            pairsByType[BoltDataType.INTERFACE_DISPLACEMENT_X].append((nodeID, nodeValue.interfaceDisplacementX))
            pairsByType[BoltDataType.INTERFACE_DISPLACEMENT_Y].append((nodeID, nodeValue.interfaceDisplacementY))
            pairsByType[BoltDataType.INTERFACE_DISPLACEMENT_Z].append((nodeID, nodeValue.interfaceDisplacementZ))
            pairsByType[BoltDataType.INTERFACE_DISPLACEMENT_TOTAL].append((nodeID, nodeValue.interfaceDisplacementTotal))
        return {dt: _NodeValuePairCollection(pairs) for dt, pairs in pairsByType.items()}

class BoltResults(_ResultsQueryBase):
    '''
    Entry point to query bolt nodal results for a given stage and SRF.

    Parameters:
        stageNumber (int): 1-based stage index.
        srfResultIndex (int): 0-based SRF value index. 0 is to query SRF-None values.

    Notes:
        - entityName is trimmed; empty strings are ignored.
        - region=None leaves the proto field unset (service returns all).
        - Exceptions from the underlying service are propagated as-is by the client.

    Examples:
        See :ref:`bolt_result_example`.
    '''
    def __init__(self, client: Client, projectId: str, stageNumber: int, srfResultIndex: int):
        super().__init__(client, projectId, stageNumber, srfResultIndex)
        self._queryService = BoltsResultsQueryService_pb2_grpc.BoltResultsQueryServiceStub(client.channel)
        
    
    def getBoltNodeResults(self, entityName: Optional[str] = None, region: Optional[Union[Cube, Cylinder, Sphere]] = None, includeIntersecting: bool = True) -> list[BoltNodeResult]:
        '''
        Query bolt nodal results at a specific stage and SRF value.
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
            list[BoltNodeResult]: A list of bolt nodal results wrappers for the requested stage and SRF value.
        '''
        request = self._makeRequest(entityName, region, includeIntersecting)
        stream = self._queryService.QueryBoltNodalResults(request)
        allResults = []
        totalQueriedNodesCount = None
        for chunk in stream:
            if chunk.HasField('header'):
                header = chunk.header
                totalQueriedNodesCount = header.totalQueriedNodesCount
            elif chunk.HasField('data'):
                allResults.extend(chunk.data.results)
        if totalQueriedNodesCount != len(allResults):
            raise RuntimeError(f"Number of nodes received does not match the expected total queried nodes count. Expected {totalQueriedNodesCount}, but received {len(allResults)}.")
        return [BoltNodeResult(r) for r in allResults]


    def getBoltElementResults(self, entityName: Optional[str] = None, region: Optional[Union[Cube, Cylinder, Sphere]] = None, includeIntersecting: bool = True) -> list[BoltElementResults]:
        '''
        Query bolt element results at a specific stage and SRF value.
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
            list[BoltElementResults]: A list of bolt element results wrappers for the requested stage and SRF value.
        '''
        request = self._makeRequest(entityName, region, includeIntersecting)
        stream = self._queryService.QueryBoltElementResults(request)
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
        return [BoltElementResults(r) for r in allResults]
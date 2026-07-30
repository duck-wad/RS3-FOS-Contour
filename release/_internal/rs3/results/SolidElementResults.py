from typing import List, Dict
import rs3.generatedFiles.SolidsResultsQueryService_pb2 as SolidsResultsQueryService_pb2

class NodeUserDataResult:
    def __init__(self, nodeId: int, value: float):
        self._nodeId = nodeId
        self._value = value

    @property
    def NodeID(self) -> int:
        return self._nodeId
    
    @property
    def Value(self) -> float:
        return self._value

    def __str__(self) -> str:
        return f"Node {self._nodeId}: {self._value}"


class UserDataResults:
    '''
    Container for node-level user data.

    Notes:
        - NodeDataValues are sorted by NodeID and exposed as an immutable sequence (tuple).
        - FormattedDisplay joins items with commas; formatting is stable but not localized.
    '''
    def __init__(self, nodeDataValues: List[NodeUserDataResult]):
        self._nodeDataValues = sorted(nodeDataValues, key=lambda x: x.NodeID)
        self._nodeDataValuesDisplay = None

    @property
    def FormattedDisplay(self) -> str:
        if self._nodeDataValuesDisplay is None:
            self._nodeDataValuesDisplay = ",".join([str(nodeDataValue) for nodeDataValue in self._nodeDataValues])
        return self._nodeDataValuesDisplay

    @property
    def NodeDataValues(self) -> tuple[NodeUserDataResult, ...]:
        return tuple(self._nodeDataValues)


class UserDataResultsCollection:
    '''
    Lazily builds and caches user data series by name.

    Notes:
        - The first access to a given userDataName triggers computation and caching.
        - Raises ValueError if the userDataName does not exist in the mapping.
    '''
    def __init__(self, userDataNameToResultIndexMap: Dict[str, int], nodedUserDataResults: Dict[int, SolidsResultsQueryService_pb2.UserDataResults]):
        # Lazy construction: keep raw inputs and build per userDataName on-demand
        self._userDataNameToResultIndexMap: Dict[str, int] = dict(userDataNameToResultIndexMap)
        self._nodedUserDataResults: Dict[int, SolidsResultsQueryService_pb2.UserDataResults] = nodedUserDataResults
        self._userDataResultsByName : Dict[str, UserDataResults] = {}


    @staticmethod
    def _getNodeDataValues(resultIndex: int, nodedUserDataResults: Dict[int, SolidsResultsQueryService_pb2.UserDataResults]) -> List[NodeUserDataResult]:
        nodeData: List[NodeUserDataResult] = []
        for nodeId, userDataResults in nodedUserDataResults.items():
            values = userDataResults.values
            if resultIndex < 0 or resultIndex >= len(values):
                raise ValueError(
                    f"User data index {resultIndex} out of range for node {nodeId} (size {len(values)})"
                )
            nodeData.append(NodeUserDataResult(nodeId, values[resultIndex]))
        return nodeData

    
    def getResult(self, userDataName: str) -> List[NodeUserDataResult]:
        # Build and cache on first access
        cached = self._userDataResultsByName.get(userDataName)
        if cached is None:
            if userDataName not in self._userDataNameToResultIndexMap:
                raise ValueError(f"User data name {userDataName} not found")
            resultIndex = self._userDataNameToResultIndexMap[userDataName]
            nodeValues = UserDataResultsCollection._getNodeDataValues(resultIndex, self._nodedUserDataResults)
            cached = UserDataResults(nodeValues)
            self._userDataResultsByName[userDataName] = cached
        return cached.NodeDataValues


class FailurePoint:
    '''
    Wrapper for a failure point reported at a Gauss/integration point.

    Notes:
        - Coordinates (X/Y/Z) are in model units.
        - FailureTypes is a list of descriptive strings. Order has no priority semantics unless stated by the service.
    '''
    def __init__(self, grpcFailurePoint: SolidsResultsQueryService_pb2.FailurePoint):
        self._grpcFailurePoint = grpcFailurePoint

    @property
    def XCoordinate(self):
        return self._grpcFailurePoint.location.x
    
    @property
    def YCoordinate(self):
        return self._grpcFailurePoint.location.y
    
    @property
    def ZCoordinate(self):
        return self._grpcFailurePoint.location.z

    @property
    def FailureTypes(self):
        return list(self._grpcFailurePoint.failureTypes)


class YieldingResults:
    def __init__(self, grpcElementResults):
        self._failurePoints = [FailurePoint(fp) for fp in grpcElementResults.failurePoints]

    def getFailurePoints(self) -> tuple[FailurePoint, ...]:
        return tuple(self._failurePoints)



class SolidElementResults:
    '''
    Element-level results wrapper for a specific stage/SRF context.

    Notes:
        - getFailurePoints() returns an immutable sequence (tuple).
        - AttachedNodes returns a copy of node IDs; modifying it does not affect internal state.
        - YieldPercent is a value in [0, 100].
    '''
    def __init__(self, grpcElementResults, hasUserData: bool, userDataNameToResultIndexMap: Dict[str, int]):
        self._grpcElementResults = grpcElementResults
        self._userDataResultsCollection = UserDataResultsCollection(userDataNameToResultIndexMap, grpcElementResults.nodedUserDataResults) if hasUserData else None
        self._yieldingResults = YieldingResults(grpcElementResults)
    
    @property
    def ElementID(self):
        return self._grpcElementResults.elementInformation.elementID

    @property
    def EntityName(self):
        return self._grpcElementResults.entityName
    
    @property
    def EntityID(self):
        return self._grpcElementResults.entityID

    @property
    def AttachedNodes(self):
        return list(self._grpcElementResults.elementInformation.nodeIDs)
    
    @property
    def YieldPercent(self):
        return self._grpcElementResults.yieldPercent

    @property
    def YieldingResults(self):
        return self._yieldingResults

    '''
    Return node-level user data values for the given user data name.

    Parameters:
        userDataName: str
            The user data series to retrieve.

    Raises:
        ValueError: If the specified user data name does not exist.

    Returns:
        List[NodeUserDataResult]: Values sorted by NodeID. If the element has no
        user data, returns an empty list.
    '''
    def getUserData(self, userDataName: str) -> List[NodeUserDataResult]:
        return self._userDataResultsCollection.getResult(userDataName) if self._userDataResultsCollection is not None else []

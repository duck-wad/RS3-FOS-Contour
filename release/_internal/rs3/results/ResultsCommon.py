from typing import List, Optional, Union

import rs3.generatedFiles.ResultsQueryCommonMessage_pb2 as ResultsQueryCommonMessage_pb2

from rs3._proxyObject import _ProxyObject
from rs3._client import Client
from rs3.Geometry import Cube, Cylinder, Sphere


class _NodeValuePairCollection:
    '''
    Container for a collection of node value pairs.

    Notes:
        - FormattedDisplay joins items with commas; formatting is stable but not localized.
    '''
    def __init__(self, nodeValuePairs: List[tuple[int, float]]):
        self._nodeValuePairs: List[tuple[int, float]] = nodeValuePairs
        self._nodeValues: List[float] = [value for _, value in self._nodeValuePairs]
        self._nodeValuesDisplay = None

    @property
    def FormattedDisplay(self) -> str:
        if self._nodeValuesDisplay is None:
            self._nodeValuesDisplay = ",".join([f"Node {nodeId}: {value}" for nodeId, value in self._nodeValuePairs])
        return self._nodeValuesDisplay

    @property
    def NodeValuePairs(self) -> List[tuple[int, float]]:
        return self._nodeValuePairs

    
    @property
    def ResultValues(self) -> List[float]:
        return self._nodeValues



class _ResultsQueryBase(_ProxyObject):

    def __init__(self, client: Client, projectId: str, stageNumber: int, srfResultIndex: int):
        super().__init__(client, projectId)
        self._stageNumber = stageNumber
        self._srfResultIndex = srfResultIndex

    
    def _makeRequest(self, entityName: Optional[str], region: Optional[Union[Cube, Cylinder, Sphere]], includeIntersecting: bool = True) -> ResultsQueryCommonMessage_pb2.ResultsQueryRequest:       
        request = ResultsQueryCommonMessage_pb2.ResultsQueryRequest(
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

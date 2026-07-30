from typing import Optional, Union
import rs3.generatedFiles.CompositeLinerResultsQueryService_pb2_grpc as CompositeLinerResultsQueryService_pb2_grpc
import rs3.generatedFiles.CompositeLinerResultsQueryService_pb2 as CompositeLinerResultsQueryService_pb2
import rs3.generatedFiles.ResultsQueryCommonMessage_pb2 as ResultsQueryCommonMessage_pb2
from rs3._proxyObject import _ProxyObject
from rs3._client import Client
from rs3.Geometry import Cube, Cylinder, Sphere
from rs3.results.ResultEnums import *

class LinerNodalResults:
    """
    Nodal result wrapper with per-material data access.

    Notes:
        - EntityNames/EntityIDs correspond to owning entities for this node.
        
    """
    def __init__(self, grpcNodalResults):
        self._grpcNodalResults = grpcNodalResults

    @property
    def EntityName(self):
        return self._grpcNodalResults.entityInformation.name

    @property
    def EntityID(self):
        return self._grpcNodalResults.entityInformation.ID

    @property
    def LayerIndex(self):
        return self._grpcNodalResults.compositeLinerStructureInformation.layerIndex

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
    def AssignedPropertyName(self):
        return self._grpcNodalResults.compositeLinerStructureInformation.assignedPropertyName

    @property
    def AttachedLinerLayersAboveIndex(self):
        return list(self._grpcNodalResults.compositeLinerStructureInformation.attachedLinerLayerUpperIndex)

    @property
    def AttachedLinerLayersBelowIndex(self):
        return list(self._grpcNodalResults.compositeLinerStructureInformation.attachedLinerLayerLowerIndex)

    @property
    def AttachedInterfaceLayerAboveIndex(self):
        return self._grpcNodalResults.compositeLinerStructureInformation.attachedInterfaceLayerUpperIndex

    @property
    def AttachedInterfaceLayerBelowIndex(self):
        return self._grpcNodalResults.compositeLinerStructureInformation.attachedInterfaceLayerLowerIndex

    @property
    def NodeDetails(self):
        return {"NodeID" : self.NodeID,
                "XCoordinate": self.XCoordinate,
                "YCoordinate": self.YCoordinate,
                "ZCoordinate": self.ZCoordinate,
                "EntityName": self.EntityName,
                "LayerIndex": self.LayerIndex
                }

class LinerElementResults:
    """
    Element-level results wrapper for a specific stage/SRF context.

    Notes:
        - AttachedNodes returns a copy of node IDs; modifying it does not affect internal state.
        - getResult(dataType) returns the value of that node in the given element when it is in the global coordinate system.
          It returns the average across the elements about that node when the local axes is defined.

    """
    def __init__(self, grpcElementResults):
        self._grpcElementResults = grpcElementResults
        self._linerResults = grpcElementResults.linerNodalResults

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
    def EntityId(self):
        return self._grpcElementResults.entityInformation.ID

    @property
    def LayerIndex(self):
        return self._grpcElementResults.compositeLinerStructureInformation.layerIndex

    @property
    def AssignedPropertyName(self):
        return self._grpcElementResults.compositeLinerStructureInformation.assignedPropertyName

    @property
    def AttachedLinerLayersAboveIndex(self):
        return list(self._grpcElementResults.compositeLinerStructureInformation.attachedLinerLayerUpperID)

    @property
    def AttachedLinerLayersBelowIndex(self):
        return list(self._grpcElementResults.compositeLinerStructureInformation.attachedLinerLayerLowerID)

    @property
    def AttachedInterfaceLayerAboveIndex(self):
        return self._grpcElementResults.compositeLinerStructureInformation.attachedInterfaceLayerUpperID

    @property
    def AttachedInterfaceLayerBelowIndex(self):
        return self._grpcElementResults.compositeLinerStructureInformation.attachedInterfaceLayerLowerID

    @property
    def FailureType(self):
        return LinerGaussPointFailureCombinations(self._grpcElementResults.failureType)

    def getResults(self, dataType: LinerResultTypes) -> list[float]:
        if not self._linerResults:
            raise ValueError("No liner results available")

        result = self._linerResults[0]
        return getattr(result, dataType.value)   

class InterfaceNodalResults:
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
    def LayerIndex(self):
        return self._grpcNodalResults.compositeLinerLinerAttachmentInformation.layerIndex

    @property
    def AssignedPropertyName(self):
        return self._grpcNodalResults.compositeLinerLinerAttachmentInformation.assignedPropertyName

    @property
    def AttachedLinerLayersAboveIndex(self):
        return self._grpcNodalResults.compositeLinerLinerAttachmentInformation.attachedLinerLayerUpperIndex
    
    @property
    def AttachedLinerLayersBelowIndex(self):
        return self._grpcNodalResults.compositeLinerLinerAttachmentInformation.attachedLinerLayerLowerIndex

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

class InterfaceElementResults:
    '''
    Element-level results wrapper for a specific stage/SRF context.

    Notes:
        - AttachedNodes returns a copy of node IDs; modifying it does not affect internal state.
    '''
    def __init__(self, grpcElementResults):
        self._grpcElementResults = grpcElementResults
        self._interfaceResults = grpcElementResults.jointNodalResults
    
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
    def LayerIndex(self):
        return self._grpcElementResults.compositeLinerLinerAttachmentInformation.layerIndex

    @property
    def AssignedPropertyName(self):
        return self._grpcElementResults.compositeLinerLinerAttachmentInformation.assignedPropertyName

    @property
    def AttachedLinerLayersAboveIndex(self):
        return self._grpcElementResults.compositeLinerLinerAttachmentInformation.attachedLinerLayerUpperIndex
    
    @property
    def AttachedLinerLayersBelowIndex(self):
        return self._grpcElementResults.compositeLinerLinerAttachmentInformation.attachedLinerLayerLowerIndex
    
    @property
    def FailureType(self):
        return JointGaussPointFailureCombinations(self._grpcElementResults.failureType)
    
    def getResults(self, dataType: InterfaceResultTypes) -> list[float]:
        if not self._interfaceResults:
            raise ValueError("No liner results available")

        result = self._interfaceResults[0]
        return getattr(result, dataType.value)    

class CompositeLinerResults(_ProxyObject):
    '''
    Entry point to query composite liner nodal/element results for a given stage and SRF.

    Parameters:
        stageNumber (int): 1-based stage index.
        srfResultIndex (int): 0-based SRF value index. 0 is to query SRF-None values.

    Notes:
        - entityName is trimmed; empty strings are ignored.
        - region=None leaves the proto field unset (service returns all).
        - Exceptions from the underlying service are propagated as-is by the client.

    Examples:
        See :ref:`composite_liner_result_example`.
    '''

    def __init__(self, client: Client, projectId: str, stageNumber: list[int], srfResultIndex: int):
        super().__init__(client, projectId)
        self._queryService = CompositeLinerResultsQueryService_pb2_grpc.CompositeLinerResultsQueryServiceStub(self._client.channel)
        self._stageNumber = stageNumber
        self._srfResultIndex = srfResultIndex
    
    def getLinerNodeResults(self, entityName: Optional[str] = None, region: Optional[Union[Cube, Cylinder, Sphere]] = None, includeIntersecting: bool = True) -> list[LinerNodalResults]:
        request = self._makeRequest(entityName, region, includeIntersecting)        
        stream = self._queryService.GetLinerNodeResults(request)
        
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
                    
        return [LinerNodalResults(r) for r in results]

    def getLinerElementResults(self, entityName: Optional[str] = None, region: Optional[Union[Cube, Cylinder, Sphere]] = None, includeIntersecting: bool = True) -> list[LinerElementResults]:
        request = self._makeRequest(entityName, region, includeIntersecting)        
        stream = self._queryService.GetLinerElementResults(request)
        
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

        return [LinerElementResults(r) for r in results]
    
    def getInterfaceNodeResults(self, entityNames: Optional[list[str]] = None, region: Optional[Union[Cube, Cylinder, Sphere]] = None, includeIntersecting: bool = True) -> list[InterfaceNodalResults]:
        request = self._makeRequest(entityNames, region, includeIntersecting)        
        stream = self._queryService.GetInterfaceNodeResults(request)
        
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

        return [InterfaceNodalResults(r) for r in results]

    def getInterfaceElementResults(self, entityNames: Optional[list[str]] = None, region: Optional[Union[Cube, Cylinder, Sphere]] = None, includeIntersecting: bool = True) -> list[InterfaceElementResults]:
        request = self._makeRequest(entityNames, region, includeIntersecting)        
        stream = self._queryService.GetInterfaceElementResults(request)
        
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

        return [InterfaceElementResults(r) for r in results]
    
    def setCoordinateSystem(self, coordinateSystemName : str) -> None:
        request = CompositeLinerResultsQueryService_pb2.SetCoordinateSystemRequest(_projectId=self._objectId, coordinateSystemName=coordinateSystemName)       
        self._client.callFunction(self._queryService.SetCoordinateSystem, request)
        
    def getCoordinateSystem(self) -> str:
        request = CompositeLinerResultsQueryService_pb2.GetCoordinateSystemRequest(_projectId=self._objectId)       
        return self._client.callFunction(self._queryService.GetCoordinateSystem, request).coordinateSystemName
        
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

import rs3.generatedFiles.ExternalVolumesService_pb2_grpc as ExternalVolumesService_pb2_grpc
import rs3.generatedFiles.ExternalVolumesService_pb2 as ExternalVolumesService_pb2
import rs3.generatedFiles.CommonMessages_pb2 as CommonMessages_pb2
from rs3.CommonEnums import *
from rs3.properties._PropertyAccessor import PropertyAccessor
from rs3._proxyObject import _ProxyObject
from rs3._client import Client

class ExternalVolume(_ProxyObject):
    """
	Examples:
        See :ref:`external_volume_and_selection_example`.		
	"""
    def __init__(self, client : Client, projectID : str):
        super().__init__(client, projectID)
        self._externalVolumesService = ExternalVolumesService_pb2_grpc.ExternalVolumesServiceStub(self._client.channel)
        self._propertyAccessor = PropertyAccessor(client, projectID, self._externalVolumesService)
        
    def setName(self, name : str):    
        request = CommonMessages_pb2.SetPropertyRequest(objectId=self._objectId, propertyName="Name", value=CommonMessages_pb2.PropertyValue(stringValue=name))
        self._client.callFunction(self._externalVolumesService.SetExternalVolumeName, request)
    def getName(self) -> str:
        return self._propertyAccessor.getStringValue("Name")
    
    def setRole(self, role : ExternalVolumeRoles):
        request = CommonMessages_pb2.SetPropertyRequest(objectId=self._objectId, propertyName="Role", value=CommonMessages_pb2.PropertyValue(stringValue=role.value))
        self._client.callFunction(self._externalVolumesService.SetExternalVolumeRole, request)
    def getRole(self) -> ExternalVolumeRoles:
        return ExternalVolumeRoles(self._propertyAccessor.getStringValue("Role"))
    
    def setAppliedMaterialProperty(self, stageNum : int, materialName : str):
        """
        Assign material to the given stage by material name. If the external volume is excavated, "No Material" should be used as the materialName.
        """
        request = ExternalVolumesService_pb2.SetAppliedMaterialPropertyRequest(objectId=self._objectId, stageNum=stageNum, materialName=materialName)
        self._client.callFunction(self._externalVolumesService.SetAppliedMaterialProperty, request)
    def getAppliedMaterialProperty(self, stageNum : int):
        request = ExternalVolumesService_pb2.GetAppliedMaterialPropertyRequest(objectId=self._objectId, stageNum=stageNum)
        response : ExternalVolumesService_pb2.GetAppliedMaterialPropertyResponse = self._client.callFunction(self._externalVolumesService.GetAppliedMaterialProperty, request)
        return response.materialName
    
    def getVolume(self) -> str:
        return self._propertyAccessor.getDoubleProperty("Volume")
    
    def getTotalSurfaceArea(self) -> str:
        return self._propertyAccessor.getDoubleProperty("Area")
    
    
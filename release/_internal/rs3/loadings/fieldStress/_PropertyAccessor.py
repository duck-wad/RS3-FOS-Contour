from rs3.properties._PropertyAccessor import PropertyAccessor as BasePropertyAccessor
import rs3.generatedFiles.FieldStressSourceService_pb2_grpc as FieldStressSourceService_pb2_grpc
import rs3.generatedFiles.CommonMessages_pb2 as CommonMessages_pb2
import rs3.generatedFiles.FieldStressSourceService_pb2 as FieldStressSourceService_pb2
from rs3._client import Client
class PropertyAccessor(BasePropertyAccessor):
    def __init__(self, client : Client, objectId : str):
        super().__init__(client, objectId, FieldStressSourceService_pb2_grpc.FieldStressSourceServiceStub(client.channel))
        
class AdvancedPropertyAccessor(BasePropertyAccessor):
    def __init__(self, client : Client, objectId : str):
        super().__init__(client, objectId, FieldStressSourceService_pb2_grpc.FieldStressSourceServiceStub(client.channel))
        self._fieldStressSourceService = FieldStressSourceService_pb2_grpc.FieldStressSourceServiceStub(client.channel)
        self.projectId = objectId
        
    def _setProperty(self, materialName : str, propertyName : str, value : CommonMessages_pb2.PropertyValue):
        request = FieldStressSourceService_pb2.SetMaterialPropertyRequest(objectId=self.projectId, 
                                                                          materialName=materialName,
                                                                          propertyName=propertyName,
                                                                          value=value)
        self._client.callFunction(self._fieldStressSourceService.SetMaterialProperty, request)
        
    def _getProperty(self, materialName : str, propertyName : str) -> CommonMessages_pb2.PropertyValue:
        request = FieldStressSourceService_pb2.GetMaterialPropertyRequest(objectId=self.projectId, 
                                                                          materialName=materialName, 
                                                                          propertyName=propertyName)
        response : FieldStressSourceService_pb2.GetMaterialPropertyResponse = self._client.callFunction(self._fieldStressSourceService.GetMaterialProperty, request)
        return response.value
    
    def getDoubleProperty(self, materialName : str, propertyName : str) -> float:
        return self._getProperty(materialName, propertyName).doubleValue

    def setDoubleProperty(self, materialName : str, propertyName : str, value : float):
        self._setProperty(materialName, propertyName, CommonMessages_pb2.PropertyValue(doubleValue=value))
    
    def getBoolValue(self, materialName : str, propertyName : str) -> bool:
        return self._getProperty(materialName, propertyName).boolValue

    def setBoolValue(self, materialName : str, propertyName : str, value: bool):
        self._setProperty(materialName, propertyName, CommonMessages_pb2.PropertyValue(boolValue=value))


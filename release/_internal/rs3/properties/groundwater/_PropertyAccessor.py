from rs3.properties._PropertyAccessor import PropertyAccessor
import rs3.generatedFiles.WaterByLocationDataService_pb2 as WaterByLocationDataService_pb2
import rs3.generatedFiles.WaterPressureGridDataService_pb2 as WaterPressureGridDataService_pb2
import rs3.generatedFiles.CommonMessages_pb2 as CommonMessages_pb2
from rs3._client import Client
class WaterByLocationPropertyAccessor(PropertyAccessor):
    def __init__(self, client : Client, objectId : str, stub, projectId : str):
        super().__init__(client, objectId, stub)
        self.projectId = projectId    
    def _setProperty(self, propertyName : str, value : CommonMessages_pb2.PropertyValue):
        request = WaterByLocationDataService_pb2.SetProjectPropertyRequest(objectId=self.objectId, 
                                                                                propertyName=propertyName,
                                                                                value=value,
                                                                                projectId=self.projectId)
        self._client.callFunction(self._stub.SetProperty, request)
        
    def _getProperty(self, propertyName : str) -> CommonMessages_pb2.PropertyValue:
        request = WaterByLocationDataService_pb2.GetProjectPropertyRequest(objectId=self.objectId, propertyName=propertyName, projectId=self.projectId)
        response : WaterByLocationDataService_pb2.GetProjectPropertyResponse = self._client.callFunction(self._stub.GetProperty, request)
        return response.value
    
class WaterGridPropertyAccessor(PropertyAccessor):
    def __init__(self, client : Client, objectId : str, stub, projectId : str):
        super().__init__(client, objectId, stub)
        self.projectId = projectId    
    def _setProperty(self, propertyName : str, value : CommonMessages_pb2.PropertyValue):
        request = WaterPressureGridDataService_pb2.SetProjectPropertyRequest(objectId=self.objectId, 
                                                                                propertyName=propertyName,
                                                                                value=value,
                                                                                projectId=self.projectId)
        self._client.callFunction(self._stub.SetProperty, request)
        
    def _getProperty(self, propertyName : str) -> CommonMessages_pb2.PropertyValue:
        request = WaterPressureGridDataService_pb2.GetProjectPropertyRequest(objectId=self.objectId, propertyName=propertyName, projectId=self.projectId)
        response : WaterPressureGridDataService_pb2.GetProjectPropertyResponse = self._client.callFunction(self._stub.GetProperty, request)
        return response.value

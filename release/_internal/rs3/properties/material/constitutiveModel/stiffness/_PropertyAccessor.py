from rs3.properties._PropertyAccessor import PropertyAccessor as BasePropertyAccessor
import rs3.generatedFiles.MaterialStiffnessService_pb2_grpc as MaterialStiffnessService_pb2_grpc
import rs3.generatedFiles.MaterialStiffnessService_pb2 as MaterialStiffnessService_pb2
import rs3.generatedFiles.CommonMessages_pb2 as CommonMessages_pb2
from rs3._client import Client
class PropertyAccessor(BasePropertyAccessor):
    def __init__(self, client : Client, objectId : str):
        self._stub = MaterialStiffnessService_pb2_grpc.MaterialStiffnessServiceStub(client.channel)
        super().__init__(client, objectId, self._stub)

class LoadingPropertyAccessor(PropertyAccessor):
    def __init__(self, client : Client, objectId : str):
        super().__init__(client, objectId)
        self.isLoading = True
    def _getProperty(self, propertyName: str) -> CommonMessages_pb2.PropertyValue:
        request = MaterialStiffnessService_pb2.GetMaterialStiffnessPropertyRequest(propertyId=self.objectId, isLoading=self.isLoading, propertyName=propertyName)
        response : MaterialStiffnessService_pb2.GetMaterialStiffnessPropertyResponse = self._client.callFunction(self._stub.GetMaterialStiffnessProperty, request)
        return response.value
    def _setProperty(self, propertyName: str, value: CommonMessages_pb2.PropertyValue):
        request = MaterialStiffnessService_pb2.SetMaterialStiffnessPropertyRequest(propertyId=self.objectId, isLoading=self.isLoading, propertyName=propertyName, value=value)
        self._client.callFunction(self._stub.SetMaterialStiffnessProperty, request)

class UnloadingPropertyAccessor(PropertyAccessor):
    def __init__(self, client : Client, objectId : str):
        super().__init__(client, objectId)
        self.isLoading = False
    def _getProperty(self, propertyName: str) -> CommonMessages_pb2.PropertyValue:
        request = MaterialStiffnessService_pb2.GetMaterialStiffnessPropertyRequest(propertyId=self.objectId, isLoading=self.isLoading, propertyName=propertyName)
        response : MaterialStiffnessService_pb2.GetMaterialStiffnessPropertyResponse = self._client.callFunction(self._stub.GetMaterialStiffnessProperty, request)
        return response.value
    def _setProperty(self, propertyName: str, value: CommonMessages_pb2.PropertyValue):
        request = MaterialStiffnessService_pb2.SetMaterialStiffnessPropertyRequest(propertyId=self.objectId, isLoading=self.isLoading, propertyName=propertyName, value=value)
        self._client.callFunction(self._stub.SetMaterialStiffnessProperty, request)

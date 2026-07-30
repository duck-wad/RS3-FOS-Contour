from rs3.properties._PropertyAccessor import PropertyAccessor as BasePropertyAccessor
from rs3.properties.PropertyEnums import *
import rs3.generatedFiles.MaterialDatumService_pb2_grpc as MaterialDatumService_pb2_grpc
import rs3.generatedFiles.MaterialDatumService_pb2 as MaterialDatumService_pb2
import rs3.generatedFiles.CommonMessages_pb2 as CommonMessages_pb2
from rs3._client import Client
class PropertyAccessor(BasePropertyAccessor):
    def __init__(self, client : Client, objectId : str, upperPropertyName : DatumDependencyIndex):
        self._stub = MaterialDatumService_pb2_grpc.MaterialDatumServiceStub(client.channel)
        self._upperPropertyName = upperPropertyName
        super().__init__(client, objectId, self._stub)
        
    def _getProperty(self, propertyName : str) -> CommonMessages_pb2.PropertyValue:
        request = MaterialDatumService_pb2.GetDatumPropertyRequest(objectId=self.objectId, upperPropertyName=self._upperPropertyName.value, propertyName=propertyName)
        response : MaterialDatumService_pb2.GetDatumPropertyResponse = self._client.callFunction(self._stub.GetProperty, request)
        return response.value
    
    def _setProperty(self, propertyName : str, value : CommonMessages_pb2.PropertyValue):
        request = MaterialDatumService_pb2.SetDatumPropertyRequest(objectId=self.objectId, 
                                                                   upperPropertyName=self._upperPropertyName.value,
                                                                   propertyName=propertyName,
                                                                   value=value)
        self._client.callFunction(self._stub.SetProperty, request)
        
    


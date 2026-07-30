from rs3.properties._PropertyAccessor import PropertyAccessor
import rs3.generatedFiles.MaterialHydraulicDataService_pb2_grpc as MaterialHydraulicDataService_pb2_grpc
import rs3.generatedFiles.CommonMessages_pb2 as CommonMessages_pb2
from rs3._client import Client
class _HydraulicPropertyAccessor(PropertyAccessor):
    def __init__(self, client : Client, objectId : str):
        super().__init__(client, objectId, MaterialHydraulicDataService_pb2_grpc.MaterialHydraulicDataServiceStub(client.channel))

class BasePropertyAccessor(_HydraulicPropertyAccessor):
    pass

class PropertyAccessor(_HydraulicPropertyAccessor):
    pass

class PhreaticConditionsPropertyAccessor(PropertyAccessor):
    def __init__(self, client : Client, objectId : str):
        self._client = client
        self._stub = MaterialHydraulicDataService_pb2_grpc.MaterialHydraulicDataServiceStub(client.channel)
        self._object = objectId
        
    def _getProperty(self, propertyName : str) -> CommonMessages_pb2.PropertyValue:
        request = CommonMessages_pb2.GetPropertyRequest(objectId=self._object, propertyName=propertyName)
        response : CommonMessages_pb2.GetPropertyResponse = self._client.callFunction(self._stub.GetWaterConditionValue, request)
        return response.value
    
    def _setProperty(self, propertyName : str, value : CommonMessages_pb2.PropertyValue):
        request = CommonMessages_pb2.SetPropertyRequest(objectId=self._object, 
                                                        propertyName=propertyName,
                                                        value=value)
        self._client.callFunction(self._stub.SetWaterConditionValue, request)


from rs3.properties._PropertyAccessor import PropertyAccessor as CommonPropertyAccessor
import rs3.generatedFiles.MaterialHydraulicModelService_pb2_grpc as MaterialHydraulicModelService_pb2_grpc
import rs3.generatedFiles.MaterialHydraulicModelService_pb2 as MaterialHydraulicModelService_pb2
import rs3.generatedFiles.MaterialHydraulicDataService_pb2_grpc as MaterialHydraulicDataService_pb2_grpc
import rs3.generatedFiles.CommonMessages_pb2 as CommonMessages_pb2    
from rs3._client import Client
class BasePropertyAccessor(CommonPropertyAccessor):
    def __init__(self, client : Client, objectId : str):
        self._stub = MaterialHydraulicDataService_pb2_grpc.MaterialHydraulicDataServiceStub(client.channel)
        super().__init__(client, objectId, self._stub)
        
class PropertyAccessor(CommonPropertyAccessor):
    def __init__(self, client : Client, objectId : str):
        self._stub = MaterialHydraulicModelService_pb2_grpc.MaterialHydraulicModelServiceStub(client.channel)
        super().__init__(client, objectId, self._stub)


from rs3.properties._PropertyAccessor import PropertyAccessor as BasePropertyAccessor
import rs3.generatedFiles.MaterialInitialConditionsService_pb2_grpc as MaterialInitialConditionsService_pb2_grpc
import rs3.generatedFiles.MaterialHydraulicDataService_pb2_grpc as MaterialHydraulicDataService_pb2_grpc
from rs3._client import Client
class PropertyAccessor(BasePropertyAccessor):
    def __init__(self, client : Client, objectId : str):
        super().__init__(client, objectId, MaterialInitialConditionsService_pb2_grpc.MaterialInitialConditionsServiceStub(client.channel))

class HydraulicPropertyAccessor(BasePropertyAccessor):
    def __init__(self, client : Client, objectId : str):
        super().__init__(client, objectId, MaterialHydraulicDataService_pb2_grpc.MaterialHydraulicDataServiceStub(client.channel))
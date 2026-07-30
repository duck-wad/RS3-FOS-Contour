from rs3.properties._PropertyAccessor import PropertyAccessor
import rs3.generatedFiles.MaterialStageFactorsService_pb2_grpc as MaterialStageFactorsService_pb2_grpc
from rs3._client import Client
class PropertyAccessor(PropertyAccessor):
    def __init__(self, client : Client, objectId : str):
        super().__init__(client, objectId, MaterialStageFactorsService_pb2_grpc.MaterialStageFactorsServiceStub(client.channel))


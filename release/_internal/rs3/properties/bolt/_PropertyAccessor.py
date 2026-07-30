from rs3.properties._PropertyAccessor import PropertyAccessor
import rs3.generatedFiles.BoltService_pb2_grpc as BoltService_pb2_grpc
from rs3._client import Client
class PropertyAccessor(PropertyAccessor):
    def __init__(self, client : Client, objectId : str):
        super().__init__(client, objectId, BoltService_pb2_grpc.BoltServiceStub(client.channel))


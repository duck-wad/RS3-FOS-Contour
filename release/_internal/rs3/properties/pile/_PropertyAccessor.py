from rs3.properties._PropertyAccessor import PropertyAccessor
import rs3.generatedFiles.PileDataService_pb2_grpc as PileDataService_pb2_grpc
from rs3._client import Client
class PropertyAccessor(PropertyAccessor):
    def __init__(self, client : Client, objectId : str, serviceStub = None):
        if serviceStub is None:
            serviceStub = PileDataService_pb2_grpc.PileDataServiceStub(client.channel)
        super().__init__(client, objectId, serviceStub)


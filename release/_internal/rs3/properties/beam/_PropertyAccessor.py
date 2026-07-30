from rs3.properties._PropertyAccessor import PropertyAccessor
import rs3.generatedFiles.BeamService_pb2_grpc as BeamService_pb2_grpc
from rs3._client import Client
class PropertyAccessor(PropertyAccessor):
    def __init__(self, client : Client, objectId : str, serviceStub = None):
        if serviceStub is None:
            serviceStub = BeamService_pb2_grpc.BeamServiceStub(client.channel)
        super().__init__(client, objectId, serviceStub)


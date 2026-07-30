from rs3.properties._PropertyAccessor import PropertyAccessor
import rs3.generatedFiles.JointService_pb2_grpc as JointService_pb2_grpc
from rs3._client import Client
class PropertyAccessor(PropertyAccessor):
    def __init__(self, client : Client, objectId : str, serviceStub = None):
        if serviceStub is None:
            serviceStub = JointService_pb2_grpc.JointServiceStub(client.channel)
        super().__init__(client, objectId, serviceStub)


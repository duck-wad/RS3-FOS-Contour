from rs3.properties._PropertyAccessor import PropertyAccessor as BasePropertyAccessor
import rs3.generatedFiles.MeshSettingsService_pb2_grpc as MeshSettingsService_pb2_grpc
import rs3.generatedFiles.CommonMessages_pb2 as CommonMessages_pb2
import rs3.generatedFiles.MeshSettingsService_pb2 as MeshSettingsService_pb2
from rs3._client import Client
class PropertyAccessor(BasePropertyAccessor):
    def __init__(self, client : Client, objectId : str):
        super().__init__(client, objectId, MeshSettingsService_pb2_grpc.MeshSettingsServiceStub(client.channel))
        


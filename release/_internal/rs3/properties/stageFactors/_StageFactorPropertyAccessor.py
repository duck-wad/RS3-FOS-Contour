import rs3.generatedFiles.CommonMessages_pb2 as CommonMessages_pb2
from rs3._client import Client
from rs3.properties._PropertyAccessor import PropertyAccessor

class StageFactorPropertyAccessor(PropertyAccessor):
    def __init__(self, parentObjectId: str, stageFactorId : str, client: Client, stub):
        super().__init__(client, parentObjectId, stub)
        self.stageFactorId = stageFactorId
        
    def _getProperty(self, propertyName: str) -> CommonMessages_pb2.PropertyValue:
        request = CommonMessages_pb2.GetStageFactorPropertyRequest(propertyId=self.objectId, stageFactorId=self.stageFactorId, propertyName=propertyName)
        response : CommonMessages_pb2.GetStageFactorPropertyResponse = self._client.callFunction(self._stub.GetStageFactorProperty, request)
        return response.value

    def _setProperty(self, propertyName: str, value: CommonMessages_pb2.PropertyValue):
        request = CommonMessages_pb2.SetStageFactorPropertyRequest(propertyId=self.objectId, stageFactorId=self.stageFactorId, propertyName=propertyName, value=value)
        self._client.callFunction(self._stub.SetStageFactorProperty, request)
    
from rs3.properties._PropertyAccessor import PropertyAccessor as BasePropertyAccessor
import rs3.generatedFiles.CommonMessages_pb2 as CommonMessages_pb2
import rs3.generatedFiles.MaterialJointSetSlipCriterionService_pb2_grpc as MaterialJointSetSlipCriterionService_pb2_grpc
import rs3.generatedFiles.MaterialJointSetSlipCriterionService_pb2 as MaterialJointSetSlipCriterionService_pb2
import rs3.generatedFiles.MaterialJointStageFactorService_pb2_grpc as MaterialJointStageFactorService_pb2_grpc
import rs3.generatedFiles.MaterialJointStageFactorService_pb2 as MaterialJointStageFactorService_pb2
import rs3.generatedFiles.MaterialJointService_pb2_grpc as MaterialJointService_pb2_grpc
import rs3.generatedFiles.MaterialJointService_pb2 as MaterialJointService_pb2
from rs3._client import Client
from rs3.properties.PropertyEnums import *
class PropertyAccessor(BasePropertyAccessor):
    def __init__(self, client : Client, materialId : str, objectId : str):
        self._stub = MaterialJointSetSlipCriterionService_pb2_grpc.MaterialJointSetSlipCriterionServiceStub(client.channel)
        super().__init__(client, objectId, self._stub)
        self._materialId = materialId
        
    def _getProperty(self, propertyName : str) -> CommonMessages_pb2.PropertyValue:
        request = MaterialJointSetSlipCriterionService_pb2.GetJointPropertyRequest(materialId=self._materialId, objectId=self.objectId, propertyName=propertyName)
        response : MaterialJointSetSlipCriterionService_pb2.GetJointPropertyResponse = self._client.callFunction(self._stub.GetJointProperty, request)
        return response.value
    
    def _setProperty(self, propertyName : str, value : CommonMessages_pb2.PropertyValue):
        request = MaterialJointSetSlipCriterionService_pb2.SetJointPropertyRequest(materialId=self._materialId, objectId=self.objectId, 
                                                                    propertyName=propertyName,
                                                                    value=value)
        self._client.callFunction(self._stub.SetJointProperty, request)
        
class MaterialJointPropertyAccessor(BasePropertyAccessor):
    def __init__(self, client : Client, materialId : str, objectId : str):
        self._stub = MaterialJointService_pb2_grpc.MaterialJointServiceStub(client.channel)
        super().__init__(client, objectId, self._stub)
        self._materialId = materialId
        
    def _getProperty(self, propertyName : str) -> CommonMessages_pb2.PropertyValue:
        request = MaterialJointService_pb2.GetJointPropertyRequest(materialId=self._materialId, objectId=self.objectId, propertyName=propertyName)
        response : MaterialJointService_pb2.GetJointPropertyResponse = self._client.callFunction(self._stub.GetJointProperty, request)
        return response.value
    
    def _setProperty(self, propertyName : str, value : CommonMessages_pb2.PropertyValue):
        request = MaterialJointService_pb2.SetJointPropertyRequest(materialId=self._materialId, objectId=self.objectId, 
                                                                    propertyName=propertyName,
                                                                    value=value)
        self._client.callFunction(self._stub.SetJointProperty, request)
        
class JointOptionStageFactorPropertyAccessor(PropertyAccessor):
    def __init__(self, parentObjectId: str, stageFactorId : str, client: Client, stub, materialID: str):
        super().__init__(client, materialID, parentObjectId)
        self._stub = stub
        self.stageFactorId = stageFactorId
        self._materialId = materialID
        
    def _getProperty(self, propertyName: str) -> CommonMessages_pb2.PropertyValue:
        request = MaterialJointStageFactorService_pb2.GetMaterialJointStageFactorPropertyRequest(materialId=self._materialId, jointId=self.objectId, stageFactorId=self.stageFactorId, propertyName=propertyName)
        response : MaterialJointStageFactorService_pb2.GetMaterialJointStageFactorPropertyResponse = self._client.callFunction(self._stub.GetStageFactorProperty, request)
        return response.value

    def _setProperty(self, propertyName: str, value: CommonMessages_pb2.PropertyValue):
        request = MaterialJointStageFactorService_pb2.SetMaterialJointStageFactorPropertyRequest(materialId=self._materialId, jointId=self.objectId, stageFactorId=self.stageFactorId, propertyName=propertyName, value=value)
        self._client.callFunction(self._stub.SetStageFactorProperty, request)
    
    
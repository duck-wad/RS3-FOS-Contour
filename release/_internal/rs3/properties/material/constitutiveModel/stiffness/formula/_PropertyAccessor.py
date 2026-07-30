from rs3.properties._PropertyAccessor import PropertyAccessor as BasePropertyAccessor
import rs3.generatedFiles.MaterialStiffnessFormulaService_pb2_grpc as MaterialStiffnessFormulaService_pb2_grpc
import rs3.generatedFiles.MaterialStiffnessFormulaService_pb2 as MaterialStiffnessFormulaService_pb2
import rs3.generatedFiles.CommonMessages_pb2 as CommonMessages_pb2
from rs3._client import Client
class PropertyAccessor(BasePropertyAccessor):
    def __init__(self, client : Client, objectId : str):
        self._stub = MaterialStiffnessFormulaService_pb2_grpc.MaterialStiffnessFormulaServiceStub(client.channel)
        super().__init__(client, objectId, self._stub)

class LoadingMaterialStiffnessFormulaPropertyAccessor(PropertyAccessor):
    def __init__(self, client: Client, parentObjectId: str, formula : MaterialStiffnessFormulaService_pb2.IsotropicFormulaType):
        self._stub = MaterialStiffnessFormulaService_pb2_grpc.MaterialStiffnessFormulaServiceStub(client.channel)
        super().__init__(client, parentObjectId)
        self.isLoading = True
        self.formula = formula
    def _getProperty(self, propertyName: str) -> CommonMessages_pb2.PropertyValue:
        request = MaterialStiffnessFormulaService_pb2.GetMaterialStiffnessFormulaPropertyRequest(propertyId=self.objectId, isLoading=self.isLoading, propertyName=propertyName, formula=self.formula)
        response : MaterialStiffnessFormulaService_pb2.GetMaterialStiffnessFormulaPropertyResponse = self._client.callFunction(self._stub.GetFormulaProperty, request)
        return response.value
    def _setProperty(self, propertyName: str, value: CommonMessages_pb2.PropertyValue):
        request = MaterialStiffnessFormulaService_pb2.SetMaterialStiffnessFormulaPropertyRequest(propertyId=self.objectId, isLoading=self.isLoading, propertyName=propertyName, formula=self.formula, value=value)
        self._client.callFunction(self._stub.SetFormulaProperty, request)
        
class UnloadingMaterialStiffnessFormulaPropertyAccessor(PropertyAccessor):
    def __init__(self, client: Client, parentObjectId: str, formula : MaterialStiffnessFormulaService_pb2.IsotropicFormulaType):
        self._stub = MaterialStiffnessFormulaService_pb2_grpc.MaterialStiffnessFormulaServiceStub(client.channel)
        super().__init__(client, parentObjectId)
        self.isLoading = True
        self.formula = formula
    def _getProperty(self, propertyName: str) -> CommonMessages_pb2.PropertyValue:
        request = MaterialStiffnessFormulaService_pb2.GetMaterialStiffnessFormulaPropertyRequest(propertyId=self.objectId, isLoading=self.isLoading, propertyName=propertyName, formula=self.formula)
        response : MaterialStiffnessFormulaService_pb2.GetMaterialStiffnessFormulaPropertyResponse = self._client.callFunction(self._stub.GetFormulaProperty, request)
        return response.value
    def _setProperty(self, propertyName: str, value: CommonMessages_pb2.PropertyValue):
        request = MaterialStiffnessFormulaService_pb2.SetMaterialStiffnessFormulaPropertyRequest(propertyId=self.objectId, isLoading=self.isLoading, propertyName=propertyName, formula=self.formula, value=value)
        self._client.callFunction(self._stub.SetFormulaProperty, request)
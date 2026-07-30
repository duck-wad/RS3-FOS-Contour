from rs3.properties._PropertyAccessor import PropertyAccessor as ParentPropertyAccessor
import rs3.generatedFiles.MaterialStiffnessService_pb2_grpc as MaterialStiffnessService_pb2_grpc
import rs3.generatedFiles.MaterialStiffnessService_pb2 as MaterialStiffnessService_pb2
import rs3.generatedFiles.MaterialStrengthService_pb2_grpc as MaterialStrengthService_pb2_grpc
import rs3.generatedFiles.MaterialStrengthService_pb2 as MaterialStrengthService_pb2
import rs3.generatedFiles.MaterialUnsaturatedSoilDataService_pb2_grpc as MaterialUnsaturatedSoilDataService_pb2_grpc
import rs3.generatedFiles.MaterialUnsaturatedSoilDataService_pb2 as MaterialUnsaturatedSoilDataService_pb2
import rs3.generatedFiles.ModelFunctionService_pb2_grpc as ModelFunctionService_pb2_grpc
import rs3.generatedFiles.ModelFunctionService_pb2 as ModelFunctionService_pb2
import rs3.generatedFiles.CommonMessages_pb2 as CommonMessages_pb2
from rs3._client import Client
from rs3.properties.PropertyEnums import *
class StiffnessPropertyAccessor(ParentPropertyAccessor):
    def __init__(self, client : Client, objectId : str):
        self._stub = MaterialStiffnessService_pb2_grpc.MaterialStiffnessServiceStub(client.channel)
        super().__init__(client, objectId, self._stub)
        
class MaterialStffnessBeddingPlanePropertyAccessor(StiffnessPropertyAccessor):
    def __init__(self, client: Client, parentObjectId: str):
        super().__init__(client, parentObjectId)
    def _getProperty(self, propertyName: str) -> CommonMessages_pb2.PropertyValue:
        request = MaterialStiffnessService_pb2.GetMaterialStiffnessBeddingPlanePropertyRequest(objectId=self.objectId, propertyName=propertyName)
        response : MaterialStiffnessService_pb2.GetMaterialStiffnessBeddingPlanePropertyResponse = self._client.callFunction(self._stub.GetBeddingPlane, request)
        return response.value
    def _setProperty(self, propertyName: str, value: CommonMessages_pb2.PropertyValue):
        request = MaterialStiffnessService_pb2.SetMaterialStiffnessBeddingPlanePropertyRequest(objectId=self.objectId, propertyName=propertyName, value=value)
        self._client.callFunction(self._stub.SetBeddingPlane, request)

class PropertyAccessor(ParentPropertyAccessor):
    def __init__(self, client : Client, objectId : str):
        self._stub = MaterialStrengthService_pb2_grpc.MaterialStrengthServiceStub(client.channel)
        super().__init__(client, objectId, self._stub)

class StrengthPropertyAccessor(PropertyAccessor):
    def __init__(self, client : Client, objectId : str):
        super().__init__(client, objectId)
        
class BasePropertyAccessor(ParentPropertyAccessor):
    def __init__(self, client : Client, objectId : str):
        self._stub = MaterialUnsaturatedSoilDataService_pb2_grpc.MaterialUnsaturatedSoilDataServiceStub(client.channel)
        super().__init__(client, objectId, self._stub)

class MaterialStrengthFunctionPropertyAccessor(StrengthPropertyAccessor):
    def __init__(self, client: Client, parentObjectId: str):
        super().__init__(client, parentObjectId)

    def getSelectedFunctionProperty(self, functionType : ConstitutiveModelTypes, propertyName: str) -> CommonMessages_pb2.PropertyValue:
        request = MaterialStrengthService_pb2.GetSelectedFunctionPropertyRequest(objectId=self.objectId, functionType=functionType.value, propertyName=propertyName)
        response : MaterialStrengthService_pb2.GetSelectedFunctionPropertyResponse = self._client.callFunction(self._stub.GetSelectedFunctionProperty, request)
        return response.value.stringValue
    def setSelectedFunctionProperty(self, functionType : ConstitutiveModelTypes, propertyName: str, value: str):
        request = MaterialStrengthService_pb2.SetSelectedFunctionPropertyRequest(objectId=self.objectId, functionType=functionType.value, propertyName=propertyName, value=CommonMessages_pb2.PropertyValue(stringValue=value))
        self._client.callFunction(self._stub.SetSelectedFunctionProperty, request)

class MaterialStrengthFunctionDataPropertyAccessor(ParentPropertyAccessor):
    def __init__(self, client: Client, parentObjectId: str, functionType: ConstitutiveModelTypes):
        self._stub = ModelFunctionService_pb2_grpc.ModelFunctionServiceStub(client.channel)
        super().__init__(client, parentObjectId, self._stub)
        self.functionType = functionType

    def _getProperty(self, propertyName: str) -> CommonMessages_pb2.PropertyValue:
        request = ModelFunctionService_pb2.GetFunctionPropertyRequest(objectId=self.objectId, functionType=self.functionType.value, propertyName=propertyName)
        response : ModelFunctionService_pb2.GetFunctionPropertyResponse = self._client.callFunction(self._stub.GetProperty, request)
        return response.value
    def _setProperty(self, propertyName: str, value: CommonMessages_pb2.PropertyValue):
        request = ModelFunctionService_pb2.SetFunctionPropertyRequest(objectId=self.objectId, functionType=self.functionType.value, propertyName=propertyName, value=value)
        self._client.callFunction(self._stub.SetProperty, request)

class MaterialStrengthAnisotropicLinearPlanarAccessor(StrengthPropertyAccessor):
    def __init__(self, client: Client, parentObjectId: str):
        super().__init__(client, parentObjectId)

    def _getProperty(self, propertyName: str) -> CommonMessages_pb2.PropertyValue:
        request = MaterialStrengthService_pb2.GetAnisotropicLinearPlanarPropertyRequest(objectId=self.objectId, propertyName=propertyName)
        response : MaterialStrengthService_pb2.GetAnisotropicLinearPlanarPropertyResponse = self._client.callFunction(self._stub.GetAnisotropicLinearPlanarProperty, request)
        return response.value
    def _setProperty(self, propertyName : str, value : CommonMessages_pb2.PropertyValue):
        request = MaterialStrengthService_pb2.SetAnisotropicLinearPlanarPropertyRequest(objectId=self.objectId, propertyName=propertyName, value=value)
        self._client.callFunction(self._stub.SetAnisotropicLinearPlanarProperty, request)
        
class MaterialStrengthSnowdenAnisotropicLinearPropertyAccessor(ParentPropertyAccessor):
    def __init__(self, client: Client, parentObjectId: str, isBeddingFunction):
        self._stub = ModelFunctionService_pb2_grpc.ModelFunctionServiceStub(client.channel)
        self.isBeddingFunction = isBeddingFunction
        super().__init__(client, parentObjectId, self._stub)

    def _getProperty(self, propertyName: str) -> CommonMessages_pb2.PropertyValue:
        request = ModelFunctionService_pb2.GetSnowdenPropertyRequest(objectId=self.objectId, isBeddingFunction=self.isBeddingFunction, propertyName=propertyName)
        response : ModelFunctionService_pb2.GetSnowdenPropertyResponse = self._client.callFunction(self._stub.GetSnowdenProperty, request)
        return response.value
    def _setProperty(self, propertyName: str, value: CommonMessages_pb2.PropertyValue):
        request = ModelFunctionService_pb2.SetSnowdenPropertyRequest(materialId=self.objectId, isBeddingFunction=self.isBeddingFunction, propertyName=propertyName, value=value)
        self._client.callFunction(self._stub.SetSnowdenProperty, request)
        



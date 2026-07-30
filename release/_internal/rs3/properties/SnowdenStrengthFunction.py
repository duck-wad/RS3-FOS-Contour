from rs3.properties.material.constitutiveModel._PropertyAccessor import MaterialStrengthSnowdenAnisotropicLinearPropertyAccessor
import rs3.generatedFiles.ModelFunctionService_pb2_grpc as ModelFunctionService_pb2_grpc
import rs3.generatedFiles.ModelFunctionService_pb2 as ModelFunctionService_pb2
from rs3._client import Client
from rs3.properties.PropertyEnums import *
from rs3._proxyObject import _ProxyObject

class SnowdenStrengthFunction(_ProxyObject):
    def __init__(self, client : Client, materialID : str, isBeddingFunction : bool):
        super().__init__(client, materialID)
        self._stub = ModelFunctionService_pb2_grpc.ModelFunctionServiceStub(self._client.channel)
        self._propertyAccessor = MaterialStrengthSnowdenAnisotropicLinearPropertyAccessor(client, materialID, isBeddingFunction)
        self._isBeddingFunction = isBeddingFunction
        
    def getFunctionType(self) -> SnowdenStrengthFunctionType:
        return self._propertyAccessor.getEnumValue("BeddingFunctionType", SnowdenStrengthFunctionType)
    def setFunctionType(self, value: SnowdenStrengthFunctionType):
         self._propertyAccessor.setEnumValue("BeddingFunctionType", value.value)
         
    def getDilationRatio(self) -> float:
        return self._propertyAccessor.getDoubleProperty("DilationRatio")
    def setDilationRatio(self, dilationRatio: float):
        self._propertyAccessor.setDoubleProperty("DilationRatio", dilationRatio)

    def getTensileStrength(self) -> float:
        return self._propertyAccessor.getDoubleProperty("PeakTensileStrength")
    def setTensileStrength(self, tensileStrength: float):
        self._propertyAccessor.setDoubleProperty("PeakTensileStrength", tensileStrength)

    def getResidualTensileStrength(self) -> float:
        return self._propertyAccessor.getDoubleProperty("ResidualTensileStrength")
    def setResidualTensileStrength(self, residualTensileStrength: float):
        self._propertyAccessor.setDoubleProperty("ResidualTensileStrength", residualTensileStrength)
        
    def setShearNormalFunction(self, normalStress : list[float], shearStress : list[float]):
        request = ModelFunctionService_pb2.SetShearNormalFunctionRequest(objectId=self._objectId,
                                                                         isBeddingFunction=self._isBeddingFunction,
                                                                         isResidualFunction=False, 
                                                                         normalStress=normalStress, 
                                                                         shearStress=shearStress, 
                                                                         residualShearStress=shearStress)
        self._client.callFunction(self._stub.SetShearNormalFunction, request)

    def setShearNormalFunctionWithResidual(self, normalStress : list[float], shearStress : list[float], residualShearStress : list[float]):
        request = ModelFunctionService_pb2.SetShearNormalFunctionRequest(objectId=self._objectId,
                                                                         isBeddingFunction=self._isBeddingFunction,
                                                                         isResidualFunction=True, 
                                                                         normalStress=normalStress, 
                                                                         shearStress=shearStress, 
                                                                         residualShearStress=residualShearStress)
        self._client.callFunction(self._stub.SetShearNormalFunction, request)
    
    def setCohesionFrictionFunction(self, normalStress : list[float], cohesion : list[float], frictionAngle : list[float]):
        request = ModelFunctionService_pb2.SetCohesionFrictionFunctionRequest(objectId=self._objectId, 
                                                                              isBeddingFunction=self._isBeddingFunction,
                                                                              isResidualFunction=False, 
                                                                              normalStress=normalStress, 
                                                                              cohesion=cohesion, 
                                                                              frictionAngle=frictionAngle,
                                                                              residualCohesion=cohesion,
                                                                              residualFrictionAngle=frictionAngle)
        self._client.callFunction(self._stub.SetCohesionFrictionFunction, request)

    def setCohesionFrictionFunctionWithResidual(self, normalStress : list[float], cohesion : list[float], frictionAngle : list[float], residualCohesion : list[float], residualFrictionAngle : list[float]):
        request = ModelFunctionService_pb2.SetCohesionFrictionFunctionRequest(objectId=self._objectId, 
                                                                              isBeddingFunction=self._isBeddingFunction,
                                                                              isResidualFunction=True, 
                                                                              normalStress=normalStress, 
                                                                              cohesion=cohesion, 
                                                                              frictionAngle=frictionAngle,
                                                                              residualCohesion=residualCohesion,
                                                                              residualFrictionAngle=residualFrictionAngle)
        self._client.callFunction(self._stub.SetCohesionFrictionFunction, request)
        
    def getShearNormalFunctionNormalStress(self) -> list[float]:
        request = ModelFunctionService_pb2.GetSnowdenStrengthFunctionColumnRequest(objectId=self._objectId, propertyName="Normal", isBeddingFunction=self._isBeddingFunction, isShearNormal=True)
        response : ModelFunctionService_pb2.GetSnowdenStrengthFunctionColumnResponse = self._client.callFunction(self._stub.GetSnowdenStrengthFunctionColumn, request)
        return [v.doubleValue for v in response.value if v.WhichOneof("value") == "doubleValue"]
    
    def getShearStress(self) -> list[float]:
        request = ModelFunctionService_pb2.GetSnowdenStrengthFunctionColumnRequest(objectId=self._objectId, propertyName="Shear", isBeddingFunction=self._isBeddingFunction, isShearNormal=True)
        response : ModelFunctionService_pb2.GetSnowdenStrengthFunctionColumnResponse = self._client.callFunction(self._stub.GetSnowdenStrengthFunctionColumn, request)
        return [v.doubleValue for v in response.value if v.WhichOneof("value") == "doubleValue"]
    
    def getResidualShearStress(self) -> list[float]:
        request = ModelFunctionService_pb2.GetSnowdenStrengthFunctionColumnRequest(objectId=self._objectId, propertyName="ResidualShear", isBeddingFunction=self._isBeddingFunction, isShearNormal=True)
        response : ModelFunctionService_pb2.GetSnowdenStrengthFunctionColumnResponse = self._client.callFunction(self._stub.GetSnowdenStrengthFunctionColumn, request)
        return [v.doubleValue for v in response.value if v.WhichOneof("value") == "doubleValue"]
    
    def getCohesionFrictionFunctionNormalStress(self) -> list[float]:
        request = ModelFunctionService_pb2.GetSnowdenStrengthFunctionColumnRequest(objectId=self._objectId, propertyName="Normal", isBeddingFunction=self._isBeddingFunction, isShearNormal=False)
        response : ModelFunctionService_pb2.GetSnowdenStrengthFunctionColumnResponse = self._client.callFunction(self._stub.GetSnowdenStrengthFunctionColumn, request)
        return [v.doubleValue for v in response.value if v.WhichOneof("value") == "doubleValue"]
    
    def getCohesionStress(self) -> list[float]:
        request = ModelFunctionService_pb2.GetSnowdenStrengthFunctionColumnRequest(objectId=self._objectId, propertyName="Cohesion", isBeddingFunction=self._isBeddingFunction, isShearNormal=False)
        response : ModelFunctionService_pb2.GetSnowdenStrengthFunctionColumnResponse = self._client.callFunction(self._stub.GetSnowdenStrengthFunctionColumn, request)
        return [v.doubleValue for v in response.value if v.WhichOneof("value") == "doubleValue"]
    
    def getFrictionAngleStress(self) -> list[float]:
        request = ModelFunctionService_pb2.GetSnowdenStrengthFunctionColumnRequest(objectId=self._objectId, propertyName="FrictionAngle", isBeddingFunction=self._isBeddingFunction, isShearNormal=False)
        response : ModelFunctionService_pb2.GetSnowdenStrengthFunctionColumnResponse = self._client.callFunction(self._stub.GetSnowdenStrengthFunctionColumn, request)
        return [v.doubleValue for v in response.value if v.WhichOneof("value") == "doubleValue"]
    
    def getResidualCohesionStress(self) -> list[float]:
        request = ModelFunctionService_pb2.GetSnowdenStrengthFunctionColumnRequest(objectId=self._objectId, propertyName="ResidualCohesion", isBeddingFunction=self._isBeddingFunction, isShearNormal=False)
        response : ModelFunctionService_pb2.GetSnowdenStrengthFunctionColumnResponse = self._client.callFunction(self._stub.GetSnowdenStrengthFunctionColumn, request)
        return [v.doubleValue for v in response.value if v.WhichOneof("value") == "doubleValue"]
    
    def getResidualFrictionAngleStress(self) -> list[float]:
        request = ModelFunctionService_pb2.GetSnowdenStrengthFunctionColumnRequest(objectId=self._objectId, propertyName="ResidualFrictionAngle", isBeddingFunction=self._isBeddingFunction, isShearNormal=False)
        response : ModelFunctionService_pb2.GetSnowdenStrengthFunctionColumnResponse = self._client.callFunction(self._stub.GetSnowdenStrengthFunctionColumn, request)
        return [v.doubleValue for v in response.value if v.WhichOneof("value") == "doubleValue"]
        
        
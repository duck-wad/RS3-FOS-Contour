import rs3.generatedFiles.ModelFunctionService_pb2_grpc as ModelFunctionService_pb2_grpc
import rs3.generatedFiles.ModelFunctionService_pb2 as ModelFunctionService_pb2
from rs3._client import Client
from rs3.properties.PropertyEnums import *
from rs3._proxyObject import _ProxyObject
from rs3.properties.material.constitutiveModel._PropertyAccessor import MaterialStrengthFunctionDataPropertyAccessor

class ShearNormalFunction(_ProxyObject):
    def __init__(self, client : Client, shearNormalFunctionID : str):
        super().__init__(client, shearNormalFunctionID)
        self._shearNormalFunctionDataService = ModelFunctionService_pb2_grpc.ModelFunctionServiceStub(self._client.channel)
        self._propertyAccessor = MaterialStrengthFunctionDataPropertyAccessor(client, shearNormalFunctionID, ConstitutiveModelTypes.SHEAR_NORMAL_FUNCTION)

    def getName(self) -> str:
        return self._propertyAccessor.getStringValue("Name")
    def setName(self, name):
        self._propertyAccessor.setStringValue("Name", name)

    def setFunctionPoints(self, value: list[tuple[float, float]] | list[tuple[float, float, float]]):
        """
        Set shear-normal function data points.

        Parameters:
            value : list of tuples
                Each data point may be provided as:

                - (normal, shear) for elastic material
                - (normal, shear, residual_shear) for plastic material
        
        Example:
            >>> shearNormalFunction = self.model.getShearNormalFunctions()[0]
            >>> shearNormalFunction.setFunctionPoints([(1.1, 2.2), (4.4, 5.5), (7.7, 8.8)])
            >>> shearNormalFunction.setFunctionPoints([(1.1, 2.2, 3.3), (4.4, 5.5, 6.6), (7.7, 8.8, 9.9)])
            
        """
        pointlist = []
        for point in value:
            if len(point) == 2:
                normal, shear = point
                residualShear = 0.0
            elif len(point) == 3:
                normal, shear, residualShear = point
            else:
                raise ValueError("Each point must contain either 2 or 3 values: (normal, shear[, residual_shear])")

            pointlist.append(ModelFunctionService_pb2.ShearNormalPoints(normalVal=normal,shearVal=shear,residualShearVal=residualShear))
        request = ModelFunctionService_pb2.SetShearNormalFunctionDataPointsRequest(objectId=self._objectId, value=pointlist)
        self._client.callFunction(self._shearNormalFunctionDataService.SetShearNormalFunctionDataPointsProperty, request)
        
    def getFunctionPoints(self) -> list[tuple[float, float]] | list[tuple[float, float, float]]:
        """
        Get shear-normal function points.
        
        Return:
            - a list of (normal, shear) data points for elastic material
            - a list of (normal, shear, residual_shear) data points for plastic material
            
        """
        request = ModelFunctionService_pb2.GetShearNormalFunctionDataPointsRequest(objectId=self._objectId)
        response : ModelFunctionService_pb2.GetShearNormalFunctionDataPointsResponse = self._client.callFunction(self._shearNormalFunctionDataService.GetShearNormalFunctionDataPointsProperty, request)
        materialType = self.getMaterialType()
        if materialType == MaterialType.PLASTIC:
            return list((p.normalVal, p.shearVal, p.residualShearVal) for p in response.value)
        elif materialType == MaterialType.ELASTIC:
            return list((p.normalVal, p.shearVal) for p in response.value)
        else:
            raise ValueError("Invalid material type.")

    def getMaterialType(self) -> MaterialType:
        return MaterialType(self._propertyAccessor.getBoolValue("IsPlastic"))
    def setMaterialType(self, materialType: MaterialType):
        return self._propertyAccessor.setBoolValue("IsPlastic", materialType.value)

    def getAutoCalcTensile(self) -> bool:
        return self._propertyAccessor.getBoolValue("AutoCalcTensile")
    def setAutoCalcTensile(self, autoCalcTensile: bool):
        return self._propertyAccessor.setBoolValue("AutoCalcTensile", autoCalcTensile)

    def getTensileStrength(self) -> float:
        return self._propertyAccessor.getDoubleProperty("PeakTensile")
    def setTensileStrength(self, tensileStrength: float):
        return self._propertyAccessor.setDoubleProperty("PeakTensile", tensileStrength)

    def getResidualTensileStrength(self) -> float:
        return self._propertyAccessor.getDoubleProperty("ResidualTensile")
    def setResidualTensileStrength(self, residualTensileStrength: float):
        return self._propertyAccessor.setDoubleProperty("ResidualTensile", residualTensileStrength)

    def getDilationRatiio(self) -> float:
        return self._propertyAccessor.getDoubleProperty("DilationRatiio")
    def setDilationRatiio(self, dilationRatiio: float):
        return self._propertyAccessor.setDoubleProperty("DilationRatiio", dilationRatiio)



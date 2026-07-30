import rs3.generatedFiles.MaterialDataService_pb2_grpc as MaterialDataService_pb2_grpc
import rs3.generatedFiles.ModelFunctionService_pb2_grpc as ModelFunctionService_pb2_grpc
import rs3.generatedFiles.ModelFunctionService_pb2 as ModelFunctionService_pb2
import rs3.generatedFiles.CommonMessages_pb2 as CommonMessages_pb2
from rs3._client import Client
from rs3.properties.PropertyEnums import *
from rs3._proxyObject import _ProxyObject
from rs3.properties.material.constitutiveModel._PropertyAccessor import MaterialStrengthFunctionDataPropertyAccessor
from rs3.ColorPicker import ColorPicker

class DiscreteFunction(_ProxyObject):
    def __init__(self, client : Client, discreteFunctionID : str):
        super().__init__(client, discreteFunctionID)
        self._discreteFunctionDataService = ModelFunctionService_pb2_grpc.ModelFunctionServiceStub(self._client.channel)
        self._propertyAccessor = MaterialStrengthFunctionDataPropertyAccessor(client, discreteFunctionID, ConstitutiveModelTypes.DISCRETE_FUNCTION)
        
    def getName(self) -> str:
        return self._propertyAccessor.getStringValue("Name")
    def setName(self, name):
        self._propertyAccessor.setStringValue("Name", name)

    def setPointX(self, value: list[float]):
        request = ModelFunctionService_pb2.SetDiscreteFunctionDataPointsRequest(objectId=self._objectId, propertyName="X", value=value)
        self._client.callFunction(self._discreteFunctionDataService.SetDiscreteFunctionDataPointsProperty, request)
    def getPointX(self) -> list[float]:
        request = ModelFunctionService_pb2.GetDiscreteFunctionDataPointsRequest(objectId=self._objectId, propertyName="X")
        response : ModelFunctionService_pb2.GetDiscreteFunctionDataPointsResponse = self._client.callFunction(self._discreteFunctionDataService.GetDiscreteFunctionDataPointsProperty, request)
        return list(response.value)
    
    def setPointY(self, value: list[float]):
        request = ModelFunctionService_pb2.SetDiscreteFunctionDataPointsRequest(objectId=self._objectId, propertyName="Y", value=value)
        self._client.callFunction(self._discreteFunctionDataService.SetDiscreteFunctionDataPointsProperty, request)
    def getPointY(self) -> list[float]:
        request = ModelFunctionService_pb2.GetDiscreteFunctionDataPointsRequest(objectId=self._objectId, propertyName="Y")
        response : ModelFunctionService_pb2.GetDiscreteFunctionDataPointsResponse = self._client.callFunction(self._discreteFunctionDataService.GetDiscreteFunctionDataPointsProperty, request)
        return list(response.value)
    
    def setPointZ(self, value: list[float]):
        request = ModelFunctionService_pb2.SetDiscreteFunctionDataPointsRequest(objectId=self._objectId, propertyName="Z", value=value)
        self._client.callFunction(self._discreteFunctionDataService.SetDiscreteFunctionDataPointsProperty, request)
    def getPointZ(self) -> list[float]:
        request = ModelFunctionService_pb2.GetDiscreteFunctionDataPointsRequest(objectId=self._objectId, propertyName="Z")
        response : ModelFunctionService_pb2.GetDiscreteFunctionDataPointsResponse = self._client.callFunction(self._discreteFunctionDataService.GetDiscreteFunctionDataPointsProperty, request)
        return list(response.value)
    
    def setPointC(self, value: list[float]):
        request = ModelFunctionService_pb2.SetDiscreteFunctionDataPointsRequest(objectId=self._objectId, propertyName="C", value=value)
        self._client.callFunction(self._discreteFunctionDataService.SetDiscreteFunctionDataPointsProperty, request)
    def getPointC(self) -> list[float]:
        request = ModelFunctionService_pb2.GetDiscreteFunctionDataPointsRequest(objectId=self._objectId, propertyName="C")
        response : ModelFunctionService_pb2.GetDiscreteFunctionDataPointsResponse = self._client.callFunction(self._discreteFunctionDataService.GetDiscreteFunctionDataPointsProperty, request)
        return list(response.value)
    
    def setPointCu(self, value: list[float]):
        request = ModelFunctionService_pb2.SetDiscreteFunctionDataPointsRequest(objectId=self._objectId, propertyName="Cu", value=value)
        self._client.callFunction(self._discreteFunctionDataService.SetDiscreteFunctionDataPointsProperty, request)
    def getPointCu(self) -> list[float]:
        request = ModelFunctionService_pb2.GetDiscreteFunctionDataPointsRequest(objectId=self._objectId, propertyName="Cu")
        response : ModelFunctionService_pb2.GetDiscreteFunctionDataPointsResponse = self._client.callFunction(self._discreteFunctionDataService.GetDiscreteFunctionDataPointsProperty, request)
        return list(response.value)
    
    def setPointPhi(self, value: list[float]):
        request = ModelFunctionService_pb2.SetDiscreteFunctionDataPointsRequest(objectId=self._objectId, propertyName="Phi", value=value)
        self._client.callFunction(self._discreteFunctionDataService.SetDiscreteFunctionDataPointsProperty, request)
    def getPointPhi(self) -> list[float]:
        request = ModelFunctionService_pb2.GetDiscreteFunctionDataPointsRequest(objectId=self._objectId, propertyName="Phi")
        response : ModelFunctionService_pb2.GetDiscreteFunctionDataPointsResponse = self._client.callFunction(self._discreteFunctionDataService.GetDiscreteFunctionDataPointsProperty, request)
        return list(response.value)
    
    def setPointModulus(self, value: list[float]):
        request = ModelFunctionService_pb2.SetDiscreteFunctionDataPointsRequest(objectId=self._objectId, propertyName="Modulus", value=value)
        self._client.callFunction(self._discreteFunctionDataService.SetDiscreteFunctionDataPointsProperty, request)
    def getPointModulus(self) -> list[float]:
        request = ModelFunctionService_pb2.GetDiscreteFunctionDataPointsRequest(objectId=self._objectId, propertyName="Modulus")
        response : ModelFunctionService_pb2.GetDiscreteFunctionDataPointsResponse = self._client.callFunction(self._discreteFunctionDataService.GetDiscreteFunctionDataPointsProperty, request)
        return list(response.value)

    def getDrainageCondition(self) -> DiscreteDrainedMode:
        return self._propertyAccessor.getEnumValue("DiscreteFunctionType", DiscreteDrainedMode)
    def setDrainageCondition(self, IsDrained: DiscreteDrainedMode):
         self._propertyAccessor.setEnumValue("DiscreteFunctionType", IsDrained.value)

    def getIs3D(self) -> bool:
        return self._propertyAccessor.getBoolValue("Is3D")
    def setIs3D(self, Is3D: bool):
        self._propertyAccessor.setBoolValue("Is3D", Is3D)

    def getPlane2DType(self) -> Plane2DType:
        return self._propertyAccessor.getEnumValue("Plane2D_type", Plane2DType)
    def setPlane2DType(self, plane2D_type: Plane2DType):
        self._propertyAccessor.setEnumValue("Plane2D_type", plane2D_type.value)

    def getHasModulus(self) -> bool:
        return self._propertyAccessor.getBoolValue("HasModulus")
    def setHasModulus(self, hasModulus: bool):
        self._propertyAccessor.setBoolValue("HasModulus", hasModulus)

    def getResidualStrengthFactor(self) -> float:
        return self._propertyAccessor.getDoubleProperty("ResidualStrengthFactor")
    def setResidualStrengthFactor(self, residualStrengthFactor: float):
        self._propertyAccessor.setDoubleProperty("ResidualStrengthFactor", residualStrengthFactor)

    def getTensileStrength(self) -> float:
        return self._propertyAccessor.getDoubleProperty("TensileStrength")
    def setTensileStrength(self, tensileStrength: float):
        self._propertyAccessor.setDoubleProperty("TensileStrength", tensileStrength)

    def getResidualTensileStrength(self) -> float:
        return self._propertyAccessor.getDoubleProperty("TensileStrengthResidual")
    def setResidualTensileStrength(self, tensileStrengthResidual: float):
        self._propertyAccessor.setDoubleProperty("TensileStrengthResidual", tensileStrengthResidual)

    def getInterpolationMethod(self) -> DiscreteFunctionInterpolationMethodType:
        return self._propertyAccessor.getEnumValue("InterpolationMethod", DiscreteFunctionInterpolationMethodType)
    def setInterpolationMethod(self, interpolationMethod: DiscreteFunctionInterpolationMethodType):
        self._propertyAccessor.setEnumValue("InterpolationMethod", interpolationMethod.value)

    def setColor(self, *args):
        """
        Sets the RGBA color for the object.
        
        Notes:
            Accepted formats:
                - setColor(red, green, blue)
                - setColor(red, green, blue, alpha)
                - setColor("#RRGGBB")
                - setColor("#RRGGBBAA")
                - setColor(ColorType.Rose)
                - setColor(0xE1E4FF)  # Integer COLORREF

        Raises:
            ValueError: If inputs are invalid or out of range.
        """
        color_bytes = ColorPicker._setColorValidation(*args)
        request = ModelFunctionService_pb2.SetFunctionColorRequest(objectId=self._objectId, value=color_bytes)
        self._client.callFunction(self._discreteFunctionDataService.SetColorProperty, request)
    def getColor(self) -> tuple[int, int, int, int]:
        """
        Retrieves the RGBA color of the object.

        Returns:
            tuple[int, int, int, int]: A tuple of four integers representing the red, green, blue, and alpha components of the object's color, each in the range [0, 255].
        """
        request = ModelFunctionService_pb2.GetFunctionColorRequest(objectId=self._objectId)
        response : ModelFunctionService_pb2.GetFunctionColorResponse = self._client.callFunction(self._discreteFunctionDataService.GetColorProperty, request)
        red, green, blue, alpha = response.value
        return red, green, blue, alpha
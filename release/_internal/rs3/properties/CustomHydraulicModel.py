from rs3._proxyObject import _ProxyObject
from rs3._client import Client
import rs3.generatedFiles.MaterialHydraulicModelService_pb2_grpc as MaterialHydraulicModelService_pb2_grpc
import rs3.generatedFiles.MaterialHydraulicModelService_pb2 as MaterialHydraulicModelService_pb2
from ._PropertyAccessor import CustomHydraulicModelPropertyAccessor
from rs3.properties.PropertyEnums import *

class _CustomHydraulicFunctionTypes(Enum):
    PERMEABILITY_FUNCTION = "PermeabilityPoints"
    DEGREE_OF_SATURATION_FUNCTION = "DegreeSaturationPoints"
    WATER_CONTENT_FUNCTION = "WaterContentPoints"
    
class CustomHydraulicModel(_ProxyObject):
    """
	Examples:
		See :ref:`material_hydraulic_example`.
    """
    def __init__(self, client: Client, objectId: str, projectId : str):
        super().__init__(client, objectId)
        self._projectId = projectId
        self._stub = MaterialHydraulicModelService_pb2_grpc.MaterialHydraulicModelServiceStub(client.channel)
        self._propertyAccessor = CustomHydraulicModelPropertyAccessor(self._client, self._objectId, self._projectId)
        
    def getName(self) -> str:
        return self._propertyAccessor.getStringValue("Name")
    def setName(self, value: str):
        self._propertyAccessor.setStringValue("Name", value)
        
    def setWaterContentInputType(self, waterContentInputType : WCInputType):
        self._propertyAccessor.setEnumValue("WCInput", waterContentInputType.value)
    def getWaterContentInputType(self) -> WCInputType:
        return self._propertyAccessor.getEnumValue("WCInput", WCInputType)
        
    def setPermeabilityFunction(self, value : list[(float, float)]):
        """
        Set the user-defined permeability function with a list of (suction, permeability) data points for the current material.

        Args:
            value (list[tuple[float, float]]):
                A list of tuples, where each tuple contains:
                - suction (float): The suction value.
                - permeability (float): The corresponding permeability value.
        """
        pointList = []
        for suction, permeability in value:
            point = MaterialHydraulicModelService_pb2.UserDefinedFunctionPoint(suction=suction, value=permeability)
            pointList.append(point)
        request = MaterialHydraulicModelService_pb2.SetUserDefinedFunctionRequest(objectId=self._objectId, projectId=self._projectId, propertyName=_CustomHydraulicFunctionTypes.PERMEABILITY_FUNCTION.value, point=pointList)
        self._client.callFunction(self._stub.SetUserDefinedFunction, request)

    def getPermeabilityFunction(self) -> list[(float, float)]:
        """
        Retrieve the permeability function with a list of (suction, permeability) data points for the current material.
        
        Returns:
            list[tuple[float, float]]:
                A list of tuples, where each tuple contains:
                - suction (float): The suction value.
                - permeability (float): The corresponding permeability value.

        """
        request = MaterialHydraulicModelService_pb2.GetUserDefinedFunctionRequest(objectId=self._objectId, projectId=self._projectId, propertyName = _CustomHydraulicFunctionTypes.PERMEABILITY_FUNCTION.value)
        response : MaterialHydraulicModelService_pb2.GetUserDefinedFunctionResponse = self._client.callFunction(self._stub.GetUserDefinedFunction, request)
        return list((p.suction, p.value) for p in response.point)
    
    def setDegreeOfSaturationFunction(self, value : list[(float, float)]):
        """
        Set the user-defined degree of saturation function with a list of (suction, degree of saturation) data points for the current material.

        Args:
            value (list[tuple[float, float]]):
                A list of tuples, where each tuple contains:
                - suction (float): The suction value.
                - degree of saturation (float): The corresponding degree of saturation value.
        """
        pointList = []
        for suction, degreeOfSaturation in value:
            point = MaterialHydraulicModelService_pb2.UserDefinedFunctionPoint(suction=suction, value=degreeOfSaturation)
            pointList.append(point)
        request = MaterialHydraulicModelService_pb2.SetUserDefinedFunctionRequest(objectId=self._objectId, projectId=self._projectId, propertyName=_CustomHydraulicFunctionTypes.DEGREE_OF_SATURATION_FUNCTION.value, point=pointList)
        self._client.callFunction(self._stub.SetUserDefinedFunction, request)

    def getDegreeOfSaturationFunction(self) -> list[(float, float)]:
        """
        Retrieve the degree of saturation function with a list of (suction, degree of saturation) data points for the current material.
        
        Returns:
            list[tuple[float, float]]:
                A list of tuples, where each tuple contains:
                - suction (float): The suction value.
                - degree of saturation (float): The corresponding degree of saturation value.

        """
        request = MaterialHydraulicModelService_pb2.GetUserDefinedFunctionRequest(objectId=self._objectId, projectId=self._projectId, propertyName = _CustomHydraulicFunctionTypes.DEGREE_OF_SATURATION_FUNCTION.value)
        response : MaterialHydraulicModelService_pb2.GetUserDefinedFunctionResponse = self._client.callFunction(self._stub.GetUserDefinedFunction, request)
        return list((p.suction, p.value) for p in response.point)
    
    def setWaterContentFunction(self, value : list[(float, float)]):
        """
        Set the user-defined water content function with a list of (suction, water content) data points for the current material.

        Args:
            value (list[tuple[float, float]]):
                A list of tuples, where each tuple contains:
                - suction (float): The suction value.
                - water content (float): The corresponding water content value.
        """
        pointList = []
        for suction, waterContent in value:
            point = MaterialHydraulicModelService_pb2.UserDefinedFunctionPoint(suction=suction, value=waterContent)
            pointList.append(point)
        request = MaterialHydraulicModelService_pb2.SetUserDefinedFunctionRequest(objectId=self._objectId, projectId=self._projectId, propertyName = _CustomHydraulicFunctionTypes.WATER_CONTENT_FUNCTION.value, point=pointList)
        self._client.callFunction(self._stub.SetUserDefinedFunction, request)

    def getWaterContentFunction(self) -> list[(float, float)]:
        """
        Retrieve the water content function with a list of (suction, water content) data points for the current material.
        
        Returns:
            list[tuple[float, float]]:
                A list of tuples, where each tuple contains:
                - suction (float): The suction value.
                - water content (float): The corresponding water content value.

        """
        request = MaterialHydraulicModelService_pb2.GetUserDefinedFunctionRequest(objectId=self._objectId, projectId=self._projectId, propertyName = _CustomHydraulicFunctionTypes.WATER_CONTENT_FUNCTION.value)
        response : MaterialHydraulicModelService_pb2.GetUserDefinedFunctionResponse = self._client.callFunction(self._stub.GetUserDefinedFunction, request)
        return list((p.suction, p.value) for p in response.point)
        
from rs3._client import Client
from ._PropertyAccessor import PropertyAccessor
from rs3._proxyObject import _ProxyObject
from rs3.properties.IPropertyGroupAccessors import IPropertyGroupAccessors
class AdvancedGravityBase(_ProxyObject, IPropertyGroupAccessors):
    def __init__(self, client: Client, id: str):
        super().__init__(client, id)
        self._propertyAccessor = PropertyAccessor(client, id)
    def getGroundSurfaceElevation(self, materialName : str) -> float:
        return self._propertyAccessor.getDoubleProperty(materialName, "GroundSurfaceElevation")
    def setGroundSurfaceElevation(self, materialName : str, value: float):
        self._propertyAccessor.setDoubleProperty(materialName, "GroundSurfaceElevation", value)
    def getOverburdenUnitWeight(self, materialName : str) -> float:
        return self._propertyAccessor.getDoubleProperty(materialName, "OverburdenUnitWeight")
    def setOverburdenUnitWeight(self, materialName : str, value: float):
        self._propertyAccessor.setDoubleProperty(materialName, "OverburdenUnitWeight", value)
    def getSigmaH1K1(self, materialName : str) -> float:
        return self._propertyAccessor.getDoubleProperty(materialName, "SigmaH1K1")
    def setSigmaH1K1(self, materialName : str, value: float):
        self._propertyAccessor.setDoubleProperty(materialName, "SigmaH1K1", value)
    def getSigmaH1K1a(self, materialName : str) -> float:
        return self._propertyAccessor.getDoubleProperty(materialName, "SigmaH1K1a")
    def setSigmaH1K1a(self, materialName : str, value: float):
        self._propertyAccessor.setDoubleProperty(materialName, "SigmaH1K1a", value)
    def getSigmaH1K1b(self, materialName : str) -> float:
        return self._propertyAccessor.getDoubleProperty(materialName, "SigmaH1K1b")
    def setSigmaH1K1b(self, materialName : str, value: float):
        self._propertyAccessor.setDoubleProperty(materialName, "SigmaH1K1b", value)
    def getSigmaH1K1c(self, materialName : str) -> float:
        return self._propertyAccessor.getDoubleProperty(materialName, "SigmaH1K1c")
    def setSigmaH1K1c(self, materialName : str, value: float):
        self._propertyAccessor.setDoubleProperty(materialName, "SigmaH1K1c", value)
    def getSigmaH1LockedIn(self, materialName : str) -> float:
        return self._propertyAccessor.getDoubleProperty(materialName, "SigmaH1LockedIn")
    def setSigmaH1LockedIn(self, materialName : str, value: float):
        self._propertyAccessor.setDoubleProperty(materialName, "SigmaH1LockedIn", value)
    def getSigmaH2K2(self, materialName : str) -> float:
        return self._propertyAccessor.getDoubleProperty(materialName, "SigmaH2K2")
    def setSigmaH2K2(self, materialName : str, value: float):
        self._propertyAccessor.setDoubleProperty(materialName, "SigmaH2K2", value)
    def getSigmaH2K2a(self, materialName : str) -> float:
        return self._propertyAccessor.getDoubleProperty(materialName, "SigmaH2K2a")
    def setSigmaH2K2a(self, materialName : str, value: float):
        self._propertyAccessor.setDoubleProperty(materialName, "SigmaH2K2a", value)
    def getSigmaH2K2b(self, materialName : str) -> float:
        return self._propertyAccessor.getDoubleProperty(materialName, "SigmaH2K2b")
    def setSigmaH2K2b(self, materialName : str, value: float):
        self._propertyAccessor.setDoubleProperty(materialName, "SigmaH2K2b", value)
    def getSigmaH2K2c(self, materialName : str) -> float:
        return self._propertyAccessor.getDoubleProperty(materialName, "SigmaH2K2c")
    def setSigmaH2K2c(self, materialName : str, value: float):
        self._propertyAccessor.setDoubleProperty(materialName, "SigmaH2K2c", value)
    def getSigmaH2LockedIn(self, materialName : str) -> float:
        return self._propertyAccessor.getDoubleProperty(materialName, "SigmaH2LockedIn")
    def setSigmaH2LockedIn(self, materialName : str, value: float):
        self._propertyAccessor.setDoubleProperty(materialName, "SigmaH2LockedIn", value)
    def getProperties(self, materialName : str):
        return {
            "GroundSurfaceElevation": self.getGroundSurfaceElevation(materialName),
            "OverburdenUnitWeight": self.getOverburdenUnitWeight(materialName),
            "SigmaH1K1": self.getSigmaH1K1(materialName),
            "SigmaH1K1a": self.getSigmaH1K1a(materialName),
            "SigmaH1K1b": self.getSigmaH1K1b(materialName),
            "SigmaH1K1c": self.getSigmaH1K1c(materialName),
            "SigmaH1LockedIn": self.getSigmaH1LockedIn(materialName),
            "SigmaH2K2": self.getSigmaH2K2(materialName),
            "SigmaH2K2a": self.getSigmaH2K2a(materialName),
            "SigmaH2K2b": self.getSigmaH2K2b(materialName),
            "SigmaH2K2c": self.getSigmaH2K2c(materialName),
            "SigmaH2LockedIn": self.getSigmaH2LockedIn(materialName),
        }
    def setProperties(self, materialName : str, GroundSurfaceElevation: float = None, OverburdenUnitWeight: float = None, SigmaH1K1: float = None, SigmaH1K1a: float = None, SigmaH1K1b: float = None, SigmaH1K1c: float = None, SigmaH1LockedIn: float = None, SigmaH2K2: float = None, SigmaH2K2a: float = None, SigmaH2K2b: float = None, SigmaH2K2c: float = None, SigmaH2LockedIn: float = None):
        if GroundSurfaceElevation is not None:
            self.setGroundSurfaceElevation(materialName, GroundSurfaceElevation)
        if OverburdenUnitWeight is not None:
            self.setOverburdenUnitWeight(materialName, OverburdenUnitWeight)
        if SigmaH1K1 is not None:
            self.setSigmaH1K1(materialName, SigmaH1K1)
        if SigmaH1K1a is not None:
            self.setSigmaH1K1a(materialName, SigmaH1K1a)
        if SigmaH1K1b is not None:
            self.setSigmaH1K1b(materialName, SigmaH1K1b)
        if SigmaH1K1c is not None:
            self.setSigmaH1K1c(materialName, SigmaH1K1c)
        if SigmaH1LockedIn is not None:
            self.setSigmaH1LockedIn(materialName, SigmaH1LockedIn)
        if SigmaH2K2 is not None:
            self.setSigmaH2K2(materialName, SigmaH2K2)
        if SigmaH2K2a is not None:
            self.setSigmaH2K2a(materialName, SigmaH2K2a)
        if SigmaH2K2b is not None:
            self.setSigmaH2K2b(materialName, SigmaH2K2b)
        if SigmaH2K2c is not None:
            self.setSigmaH2K2c(materialName, SigmaH2K2c)
        if SigmaH2LockedIn is not None:
            self.setSigmaH2LockedIn(materialName, SigmaH2LockedIn)

from rs3.loadings.LoadingEnums import *
import rs3.generatedFiles.CommonMessages_pb2 as CommonMessages_pb2
import rs3.generatedFiles.FieldStressSourceService_pb2 as FieldStressSourceService_pb2
import rs3.generatedFiles.FieldStressSourceService_pb2_grpc as FieldStressSourceService_pb2_grpc
from ._PropertyAccessor import AdvancedPropertyAccessor
class AdvancedGravity(AdvancedGravityBase):
    """
	Examples:
		See :ref:`field_stress_example`.
    """
    def __init__(self, client: Client, id: str):
        super().__init__(client, id)
        self._fieldStressSourceService = FieldStressSourceService_pb2_grpc.FieldStressSourceServiceStub(self._client.channel)
        self._propertyAccessor = AdvancedPropertyAccessor(client, id)
        
    def getApplyCustomFieldStress(self, materialName : str) -> bool:
        return self._propertyAccessor.getBoolValue(materialName, "UseCustomFieldStress")
    
    def setApplyCustomFieldStress(self, materialName : str, value : bool):
        self._propertyAccessor.setBoolValue(materialName, "UseCustomFieldStress", value)     
    
    def getTrendPlungeOrientation(self, materialName : str) -> tuple[float, float, float]:
        """
        Retrieves the trend and plunge orientations of the vertical and horizontal stress axes.

        Returns:
            tuple[float, float, float]: A tuple containing:
                - vertical stress trend angle in degrees
                - vertical stress plunge angle in degrees
                - horizontal stress trend angle in degrees
        """
        request = FieldStressSourceService_pb2.GetMaterialTrendPlungePropertyRequest(objectId=self._objectId, materialName=materialName)
        response : FieldStressSourceService_pb2.GetMaterialTrendPlungePropertyResponse = self._client.callFunction(self._fieldStressSourceService.GetMaterialTrendPlungeProperty, request)
        return response.sigma1.trend, response.sigma1.plunge, response.sigma3.trend
    
    def setTrendPlungeOrientation(self, materialName : str, verticalStressTrend : float = 0, verticalStressPlunge : float = 90, horizontalStressTrend : float = 90):
        """
        Sets the trend and plunge orientations of the vertical and horizontal stress axes.

        Args:
            verticalStressTrend (float): Trend angle of the vertical stress in degrees. Default is 0.
            verticalStressPlunge (float): Plunge angle of the vertical stress in degrees. Default is 90. The valid data range is (0, 90].
            horizontalStressTrend (float): Trend angle of the horizontal stress in degrees. Default is 90.
        """
        verticalStressOrientation = CommonMessages_pb2.LinearDirection(trend=verticalStressTrend, plunge=verticalStressPlunge)
        horizontalStressOrientation = CommonMessages_pb2.LinearDirection(trend=horizontalStressTrend, plunge=0)
        request = FieldStressSourceService_pb2.SetMaterialTrendPlungePropertyRequest(objectId=self._objectId, materialName=materialName, sigma1=verticalStressOrientation, sigma3=horizontalStressOrientation)
        self._client.callFunction(self._fieldStressSourceService.SetMaterialTrendPlungeProperty, request)
        
    def getVectorOrientation(self, materialName : str) -> tuple[tuple[float, float, float], tuple[float, float, float]]:
        """
        Retrieves the vectors representing the directions of the horizontal and vertical stress axes.

        Returns:
            tuple[tuple[float, float, float], tuple[float, float, float]]:
                - First tuple: horizontal stress 1 vector (x, y, z)
                - Second tuple: vertical stress vector (x, y, z)
        """
        request = FieldStressSourceService_pb2.GetMaterialVectorPropertyRequest(objectId=self._objectId, materialName=materialName)
        response : FieldStressSourceService_pb2.GetMaterialVectorPropertyResponse = self._client.callFunction(self._fieldStressSourceService.GetMaterialVectorProperty, request)
        return [(response.sigma3.x, response.sigma3.y, response.sigma3.z), (response.sigma1.x, response.sigma1.y, response.sigma1.z)]
    
    def setVectorOrientation(self, materialName : str, horizontalStress1 = tuple[float, float, float], verticalStress = tuple[float, float, float]):
        """
        Sets the orientation vectors for the horizontal and vertical stress axes.

        Args:
            horizontalStress1 (tuple[float, float, float]): 3D vector representing horizontal stress 1.
            verticalStress (tuple[float, float, float]): 3D vector representing vertical stress.

        Note:
            The horizontal and vertical stress vectors must be orthogonal.
        """
        verticalStressOrientation = CommonMessages_pb2.Point3D(x=verticalStress[0], y=verticalStress[1], z=verticalStress[2])
        horizontalStressOrientation = CommonMessages_pb2.Point3D(x=horizontalStress1[0], y=horizontalStress1[1], z=horizontalStress1[2])
        request = FieldStressSourceService_pb2.SetMaterialVectorPropertyRequest(objectId=self._objectId, materialName=materialName, sigma1=verticalStressOrientation, sigma3=horizontalStressOrientation)
        self._client.callFunction(self._fieldStressSourceService.SetMaterialVectorProperty, request)
        
        
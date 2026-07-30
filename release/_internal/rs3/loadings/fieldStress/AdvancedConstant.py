from rs3._client import Client
from ._PropertyAccessor import PropertyAccessor
from rs3._proxyObject import _ProxyObject
from rs3.properties.IPropertyGroupAccessors import IPropertyGroupAccessors
class AdvancedConstantBase(_ProxyObject, IPropertyGroupAccessors):
    def __init__(self, client: Client, id: str):
        super().__init__(client, id)
        self._propertyAccessor = PropertyAccessor(client, id)
    def getSigma1(self, materialName : str) -> float:
        return self._propertyAccessor.getDoubleProperty(materialName, "Sigma1")
    def setSigma1(self, materialName : str, value: float):
        self._propertyAccessor.setDoubleProperty(materialName, "Sigma1", value)
    def getSigma2(self, materialName : str) -> float:
        return self._propertyAccessor.getDoubleProperty(materialName, "Sigma2")
    def setSigma2(self, materialName : str, value: float):
        self._propertyAccessor.setDoubleProperty(materialName, "Sigma2", value)
    def getSigma3(self, materialName : str) -> float:
        return self._propertyAccessor.getDoubleProperty(materialName, "Sigma3")
    def setSigma3(self, materialName : str, value: float):
        self._propertyAccessor.setDoubleProperty(materialName, "Sigma3", value)
    def getProperties(self, materialName : str):
        return {
            "Sigma1": self.getSigma1(materialName),
            "Sigma2": self.getSigma2(materialName),
            "Sigma3": self.getSigma3(materialName),
        }
    def setProperties(self, materialName: str, Sigma1: float = None, Sigma2: float = None, Sigma3: float = None):
        if Sigma1 is not None:
            self.setSigma1(materialName, Sigma1)
        if Sigma2 is not None:
            self.setSigma2(materialName, Sigma2)
        if Sigma3 is not None:
            self.setSigma3(materialName, Sigma3)

from rs3.loadings.LoadingEnums import *
import rs3.generatedFiles.CommonMessages_pb2 as CommonMessages_pb2
import rs3.generatedFiles.FieldStressSourceService_pb2 as FieldStressSourceService_pb2
import rs3.generatedFiles.FieldStressSourceService_pb2_grpc as FieldStressSourceService_pb2_grpc
from ._PropertyAccessor import AdvancedPropertyAccessor
class AdvancedConstant(AdvancedConstantBase):
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
        
    def getTrendPlungeOrientation(self, materialName : str) -> tuple[float, float, float, float]:
        """
        Retrieves the trend and plunge orientations of the sigma1 and sigma3 stress axes.

        Returns:
            tuple[float, float, float, float]: A tuple containing:
                - sigma1 trend (degrees)
                - sigma1 plunge (degrees)
                - sigma3 trend (degrees)
                - sigma3 plunge (degrees)
        """
        request = FieldStressSourceService_pb2.GetMaterialTrendPlungePropertyRequest(objectId=self._objectId, materialName=materialName)
        response : FieldStressSourceService_pb2.GetMaterialTrendPlungePropertyResponse = self._client.callFunction(self._fieldStressSourceService.GetMaterialTrendPlungeProperty, request)
        return response.sigma1.trend, response.sigma1.plunge, response.sigma3.trend, response.sigma3.plunge
    
    def setTrendPlungeOrientation(self, materialName : str, signma1Trend : float = 0, sigma1Plunge : float = 90, signma3Trend : float = 90, sigma3Plunge : float = 0):
        """
        Sets the trend and plunge orientations for the sigma1 and sigma3 stress axes.

        Args:
            signma1Trend (float): Trend angle of sigma1 in degrees. Default is 0.
            sigma1Plunge (float): Plunge angle of sigma1 in degrees. Default is 90.
            signma3Trend (float): Trend angle of sigma3 in degrees. Default is 90.
            sigma3Plunge (float): Plunge angle of sigma3 in degrees. Default is 0.
        """
        sigma1Orientation = CommonMessages_pb2.LinearDirection(trend=signma1Trend, plunge=sigma1Plunge)
        sigma3Orientation = CommonMessages_pb2.LinearDirection(trend=signma3Trend, plunge=sigma3Plunge)
        request = FieldStressSourceService_pb2.SetMaterialTrendPlungePropertyRequest(objectId=self._objectId, materialName=materialName, sigma1=sigma1Orientation, sigma3=sigma3Orientation)
        self._client.callFunction(self._fieldStressSourceService.SetMaterialTrendPlungeProperty, request)
        
    def getVectorOrientation(self, materialName : str) -> tuple[tuple[float, float, float], tuple[float, float, float]]:
        """
        Retrieves the vectors representing the orientations of sigma1 and sigma3.

        Returns:
            tuple[tuple[float, float, float], tuple[float, float, float]]:
                A tuple containing two 3D vectors:
                - sigma1 vector (x, y, z)
                - sigma3 vector (x, y, z)
        """
        request = FieldStressSourceService_pb2.GetMaterialVectorPropertyRequest(objectId=self._objectId, materialName=materialName)
        response : FieldStressSourceService_pb2.GetMaterialVectorPropertyResponse = self._client.callFunction(self._fieldStressSourceService.GetMaterialVectorProperty, request)
        return [(response.sigma1.x, response.sigma1.y, response.sigma1.z), (response.sigma3.x, response.sigma3.y, response.sigma3.z)]
    
    def setVectorOrientation(self, materialName : str, sigma1 = tuple[float, float, float], sigma3 = tuple[float, float, float]):
        """
        Sets the orientation vectors for sigma1 and sigma3.

        Args:
            sigma1 (tuple[float, float, float]): 3D vector representing sigma1 orientation (x, y, z).
            sigma3 (tuple[float, float, float]): 3D vector representing sigma3 orientation (x, y, z).
            
        Note:
            The sigma1 and sigma3 vectors must be orthogonal (i.e., their dot product should be zero)
        """
        sigma1Orientation = CommonMessages_pb2.Point3D(x=sigma1[0], y=sigma1[1], z=sigma1[2])
        sigma3Orientation = CommonMessages_pb2.Point3D(x=sigma3[0], y=sigma3[1], z=sigma3[2])
        request = FieldStressSourceService_pb2.SetMaterialVectorPropertyRequest(objectId=self._objectId, materialName=materialName, sigma1=sigma1Orientation, sigma3=sigma3Orientation)
        self._client.callFunction(self._fieldStressSourceService.SetMaterialVectorProperty, request)
        
from rs3._proxyObject import _ProxyObject
from rs3._client import Client
from ._PropertyAccessor import MaterialStrengthAnisotropicLinearPlanarAccessor
import rs3.generatedFiles.MaterialStrengthService_pb2_grpc as MaterialStrengthService_pb2_grpc
import rs3.generatedFiles.MaterialStrengthService_pb2 as MaterialStrengthService_pb2
from rs3.properties.PropertyEnums import *

class AnisotropicLinearPlanarBase(_ProxyObject):
    def __init__(self, client: Client, id: str):
        super().__init__(client, id)
        self._stub = MaterialStrengthService_pb2_grpc.MaterialStrengthServiceStub(client.channel)
        self._anisotropicLinearPropertyAccessor = MaterialStrengthAnisotropicLinearPlanarAccessor(client, id)
        
    def getPlanarDirectionDefinedBy(self) -> PlanarDirectionType:
        return self._anisotropicLinearPropertyAccessor.getEnumValue("DirectionType", PlanarDirectionType)
    def setPlanarDirectionDefinedBy(self, planarDirectionType: PlanarDirectionType):
        return self._anisotropicLinearPropertyAccessor.setEnumValue("DirectionType", planarDirectionType.value)
    
    def getNormalVector(self) -> tuple[float, float, float]:
        """
        Get the normal vector.

        Returns
        -------
        tuple[float, float, float]
            The normal direction defined as a 3D vector (nx, ny, nz),
            representing the X, Y, and Z components in the global
            coordinate system.
        """
        return self._anisotropicLinearPropertyAccessor.getVector3DValue("NormalDirection")
    def setNormalVector(self, value : tuple[float, float, float]):
        """
        Set the normal vector.

        Parameters
        ----------
        value : tuple[float, float, float]
            A 3D vector (nx, ny, nz) representing the normal direction
            in the global coordinate system.
        """
        self._anisotropicLinearPropertyAccessor.setVector3DValue("NormalDirection", value)
        
    def getDip(self) -> float:
        return self._anisotropicLinearPropertyAccessor.getDoubleProperty("Dip")
    def setDip(self, value: float):
        self._anisotropicLinearPropertyAccessor.setDoubleProperty("Dip", value)
        
    def getDipDirection(self) -> float:
        return self._anisotropicLinearPropertyAccessor.getDoubleProperty("DipDirection")
    def setDipDirection(self, value: float):
        self._anisotropicLinearPropertyAccessor.setDoubleProperty("DipDirection", value)
    
    def getSurface(self) -> str:
        """
        Get defined anisotropic surface for this material.
        
        Note:
            At least one anisotropic surface needs to be defined to get anisotropy by surface. 
        """
        request = MaterialStrengthService_pb2.GetAnisotropicSurfacePropertyRequest(objectId=self._objectId)
        response : MaterialStrengthService_pb2.GetAnisotropicSurfacePropertyResponse = self._client.callFunction(self._stub.GetAnisotropicSurfaceProperty, request)
        return response.surfaceName
    def setSurface(self, value: str):
        """
        Set anisotropic surface for this material.
        
        At least one anisotropic surface needs to be defined to define anisotropy by surface. 
        See Materials > Add Anisotropic Surface or Add Anisotropic Surface by Location for setting 
        anisotropic surfaces.
        """
        request = MaterialStrengthService_pb2.SetAnisotropicSurfacePropertyRequest(objectId=self._objectId, surfaceName=value)
        self._client.callFunction(self._stub.SetAnisotropicSurfaceProperty, request)
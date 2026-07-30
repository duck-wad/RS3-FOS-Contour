from rs3._client import Client
from rs3.properties.PropertyEnums import *
from rs3._proxyObject import _ProxyObject
from rs3.properties.material.constitutiveModel._PropertyAccessor import MaterialStrengthFunctionDataPropertyAccessor
import rs3.generatedFiles.ModelFunctionService_pb2_grpc as ModelFunctionService_pb2_grpc
import rs3.generatedFiles.ModelFunctionService_pb2 as ModelFunctionService_pb2

class GeneralizedAnisotropicFunction(_ProxyObject):
    """
    Examples:
        See :ref:`generalized_anisotropic_function_example`.
    """
    def __init__(self, client : Client, generalizedAnisotropicFunctionID : str, projectID : str):
        super().__init__(client, generalizedAnisotropicFunctionID)
        self._stub = ModelFunctionService_pb2_grpc.ModelFunctionServiceStub(self._client.channel)
        self._propertyAccessor = MaterialStrengthFunctionDataPropertyAccessor(client, generalizedAnisotropicFunctionID, ConstitutiveModelTypes.GENERALIZED_ANISOTROPIC)
        self.projectId = projectID

    def getName(self) -> str:
        return self._propertyAccessor.getStringValue("Name")
    def setName(self, name):
        self._propertyAccessor.setStringValue("Name", name)

    def getDipDipDirectionFunctionPoints(self) -> list[tuple[float, float, float, float, str]]:
        """
        Get a list of dip-dip direction function points.

        Returns:
            list[tuple[float, float, float, float, str]]: A list of (dip, dip_direction, A, B, material_name) data points.
        """
        request = ModelFunctionService_pb2.GetGeneralizedAnisotropicFunctionDipDataPointsRequest(objectId=self._objectId, projectId=self.projectId)
        response : ModelFunctionService_pb2.GetGeneralizedAnisotropicFunctionDipDataPointsResponse = self._client.callFunction(self._stub.GetGeneralizedAnisotropicFunctionDipDataPointsProperty, request)
        return list((p.dip, p.dipDirection, p.A, p.B, p.materialName) for p in response.value)

    def setDipDipDirectionFunctionPoints(self, value: list[tuple[float, float, float, float, str]]):
        """
        Set a list of dip-dip direction function points.

        Parameters:
            value : list[tuple[float, float, float, float, str]]: A list of (dip, dip_direction, A, B, material_name) data points.

        Example:
            >>> generalizedAnisotropicFunction = self.model.getGeneralizedAnisotropicFunctions()[0]
            >>> dipDipDirectionPoints = [(15.5, 2.1, 0.4, 0.5, "Material 3"), (13.2, 24.1, 1.4, 1.5, "Material 5")]
            >>> generalizedAnisotropicFunction.setDipDipDirectionFunctionPoints(dipDipDirectionPoints)
        
        """
        pointlist = []
        for dip, dipDirection, A, B, materialName in value:
            point = ModelFunctionService_pb2.DipDipDirectionPoints(dip=dip, dipDirection=dipDirection, A=A, B=B, materialName=materialName)
            pointlist.append(point)
        request = ModelFunctionService_pb2.SetGeneralizedAnisotropicFunctionDipDataPointsRequest(objectId=self._objectId, projectId=self.projectId, value=pointlist)
        self._client.callFunction(self._stub.SetGeneralizedAnisotropicFunctionDipDataPointsProperty, request)

    def getSurfaceFunctionPoints(self) -> list[tuple[str, float, float, str]]:
        """
        Get a list of surface function points.

        Returns:
            list[tuple[str, float, float, str]]: A list of (surface_name, A, B, material_name) data points.
        """
        request = ModelFunctionService_pb2.GetGeneralizedAnisotropicFunctionSurfaceDataPointsRequest(objectId=self._objectId, projectId=self.projectId)
        response : ModelFunctionService_pb2.GetGeneralizedAnisotropicFunctionSurfaceDataPointsResponse = self._client.callFunction(self._stub.GetGeneralizedAnisotropicFunctionSurfaceDataPointsProperty, request)
        return list((p.surfaceName, p.A, p.B, p.materialName) for p in response.value)

    def setSurfaceFunctionPoints(self, value: list[tuple[str, float, float, str]]):
        """
        Set a list of surface function points.

        Parameters:
            value : list[tuple[str, float, float, str]]: A list of (surface_name, A, B, material_name) data points.

        Example:
            >>> generalizedAnisotropicFunction = self.model.getGeneralizedAnisotropicFunctions()[0]
            >>> surfacePoints = [("Anisotropic Surface 2", 0.4, 0.5, "Material 4"), ("Anisotropic Surface 1", 1.4, 1.5, "Material 2")]
            >>> generalizedAnisotropicFunction.setSurfaceFunctionPoints(surfacePoints)
        
        """
        pointlist = []
        for surfaceName, A, B, materialName in value:
            point = ModelFunctionService_pb2.SurfacePoints(surfaceName=surfaceName, A=A, B=B, materialName=materialName)
            pointlist.append(point)
        request = ModelFunctionService_pb2.SetGeneralizedAnisotropicFunctionSurfaceDataPointsRequest(objectId=self._objectId, projectId=self.projectId, value=pointlist)
        self._client.callFunction(self._stub.SetGeneralizedAnisotropicFunctionSurfaceDataPointsProperty, request)

    def getBaseMaterial(self) -> str:
        request = ModelFunctionService_pb2.GetGeneralizedAnisotropicBaseMaterialRequest(objectId=self._objectId)
        response : ModelFunctionService_pb2.GetGeneralizedAnisotropicBaseMaterialResponse = self._client.callFunction(self._stub.GetGeneralizedAnisotropicBaseMaterialProperty, request)
        return response.baseMaterial

    def setBaseMaterial(self, value: str):
        request = ModelFunctionService_pb2.SetGeneralizedAnisotropicBaseMaterialRequest(objectId=self._objectId, projectId=self.projectId, baseMaterial=value)
        self._client.callFunction(self._stub.SetGeneralizedAnisotropicBaseMaterialProperty, request)

    def getAnisotropyDefinition(self) -> GeneralizedAnisotropyDefinitionType:
        return self._propertyAccessor.getEnumValue("anisotropyDefinition", GeneralizedAnisotropyDefinitionType)
    def setAnisotropyDefinition(self, anisotropyDefinition: GeneralizedAnisotropyDefinitionType):
        return self._propertyAccessor.setEnumValue("anisotropyDefinition", anisotropyDefinition.value)

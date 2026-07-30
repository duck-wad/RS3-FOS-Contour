import rs3.generatedFiles.MeshSettingsService_pb2_grpc as MeshSettingsService_pb2_grpc
import rs3.generatedFiles.MeshSettingsService_pb2 as MeshSettingsService_pb2
from rs3.properties._PropertyAccessor import PropertyAccessor
from rs3._proxyObject import _ProxyObject
from rs3._client import Client
from rs3.mesh.MeshEnums import *
from rs3.mesh.Graded import Graded
from rs3.mesh.Uniform import Uniform

class Mesh(_ProxyObject):
    """
    Edit the mesh settings and generate the mesh.

    Attributes:
        Graded (Graded): Reference object for modifying property.
        Uniform (Uniform): Reference object for modifying property.

    Examples:
        See :ref:`mesh_example`.

    """
    def __init__(self, client : Client, projectID : str):
        super().__init__(client, projectID)
        self._meshSettingsService = MeshSettingsService_pb2_grpc.MeshSettingsServiceStub(self._client.channel)
        self._propertyAccessor = PropertyAccessor(client, projectID, self._meshSettingsService)
        self.Graded = Graded(client, projectID)
        self.Uniform = Uniform(client, projectID)

    def getElementType(self) -> MeshElementType:
        """
        Get mesh element type set in the model.
        """
        return self._propertyAccessor.getEnumValue("ElementType", MeshElementType)
    def setElementType(self, elementType : MeshElementType):
        """
        Set 4-noded, 10-noded or hybrid tetrahedral elements.
        """
        self._propertyAccessor.setEnumValue("ElementType", elementType.value)

    def getMeshGradation(self) -> MeshGradation:
        return self._propertyAccessor.getEnumValue("MeshGradation", MeshGradation)
    def setMeshGradation(self, meshGradation : MeshGradation):
        self._propertyAccessor.setEnumValue("MeshGradation", meshGradation.value)

    def mesh(self):
        """
        Generate finite element mesh for this model. 
        """
        request = MeshSettingsService_pb2.MeshRequest(projectId=self._objectId)
        self._client.callFunction(self._meshSettingsService.Mesh, request)

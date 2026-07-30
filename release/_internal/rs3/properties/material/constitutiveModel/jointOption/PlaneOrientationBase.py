from rs3._proxyObject import _ProxyObject
from rs3._client import Client
from ._PropertyAccessor import PropertyAccessor
import rs3.generatedFiles.MaterialJointSetSlipCriterionService_pb2_grpc as MaterialJointSetSlipCriterionService_pb2_grpc
import rs3.generatedFiles.MaterialJointSetSlipCriterionService_pb2 as MaterialJointSetSlipCriterionService_pb2
import rs3.generatedFiles.CommonMessages_pb2 as CommonMessages_pb2
from rs3.properties.PropertyEnums import *

class PlaneOrientationBase(_ProxyObject):
    def __init__(self, client: Client, materialId: str, objectId : str):
        super().__init__(client, objectId)
        self._stub = MaterialJointSetSlipCriterionService_pb2_grpc.MaterialJointSetSlipCriterionServiceStub(client.channel)
        self._propertyAccessor = PropertyAccessor(client, materialId, objectId)
        self._materialId = materialId
        
    def getPlaneOrientationDefinedBy(self) -> PlaneOrientationType:
        return self._propertyAccessor.getEnumValue("SelectedDirectionType", PlaneOrientationType)
    def setPlaneOrientationDefinedBy(self, planarDirectionType: PlaneOrientationType):
        return self._propertyAccessor.setEnumValue("SelectedDirectionType", planarDirectionType.value)
    
    def getVector(self) -> tuple[float, float, float]:
        """
        Returns:
            tuple[float, float, float]:
                A 3D vector `(x, y, z)` representing the direction in model coordinates.
        """
        request = MaterialJointSetSlipCriterionService_pb2.GetJointOptionVectorPropertyRequest(materialId=self._materialId, objectId=self._objectId)
        response : MaterialJointSetSlipCriterionService_pb2.GetJointOptionVectorPropertyResponse = self._client.callFunction(self._stub.GetJointOptionVectorProperty, request)
        return (response.value.x, response.value.y, response.value.z)
    def setVector(self, value : tuple[float, float, float]):
        """
        Args:
            NormalDirection (tuple[float, float, float]):
                A 3D vector `(x, y, z)` representing the normal direction in model coordinates.
        """
        vector = CommonMessages_pb2.Vector3D(x=value[0], y=value[1], z=value[2])
        request = MaterialJointSetSlipCriterionService_pb2.SetJointOptionVectorPropertyRequest(materialId=self._materialId, objectId=self._objectId, value=vector)
        self._client.callFunction(self._stub.SetJointOptionVectorProperty, request)
        
    def getTrendPlunge(self) -> tuple[float, float]:
        """
        Retrieve the orientation in trend-plunge format.

        Returns:
            tuple[float, float]:
                - trend (float): The compass direction of the horizontal projection of the line (in degrees).
                - plunge (float): The angle between the line and the horizontal plane (in degrees).
        """
        request = MaterialJointSetSlipCriterionService_pb2.GetJointOptionTrendPlungePropertyRequest(materialId=self._materialId, objectId=self._objectId)
        response : MaterialJointSetSlipCriterionService_pb2.GetJointOptionTrendPlungePropertyResponse = self._client.callFunction(self._stub.GetJointOptionTrendPlungeProperty, request)
        return (response.trend, response.plunge)
    def setTrendPlunge(self, trend : float, plunge : float):
        """
        Set the orientation in trend-plunge format.

        Args:
            trend (float):
                The compass direction of the horizontal projection of the line (in degrees).
            plunge (float):
                The angle between the line and the horizontal plane (in degrees).
        """
        request = MaterialJointSetSlipCriterionService_pb2.SetJointOptionTrendPlungePropertyRequest(materialId=self._materialId, objectId=self._objectId, trend=trend, plunge=plunge)
        self._client.callFunction(self._stub.SetJointOptionTrendPlungeProperty, request)
        
    def getDipDipDirection(self) -> tuple[float, float]:
        """
        Retrieve the orientation in dip-dip direction format.

        Returns:
            tuple[float, float]:
                - dip (float): The angle between the plane and the horizontal plane (in degrees).
                - dipDirection (float): The compass direction in which the plane is dipping (in degrees).

        """
        request = MaterialJointSetSlipCriterionService_pb2.GetJointOptionDipDipDirectionPropertyRequest(materialId=self._materialId, objectId=self._objectId)
        response : MaterialJointSetSlipCriterionService_pb2.GetJointOptionDipDipDirectionPropertyResponse = self._client.callFunction(self._stub.GetJointOptionDipDipDirectionProperty, request)
        return (response.dip, response.dipDirection)
    def setDipDipDirection(self, dip : float, dipDirection : float):
        """
        Set the orientation in dip-dip direction format.

        Args:
            dip (float):
                The angle between the plane and the horizontal plane (in degrees).
            dipDirection (float):
                The compass direction in which the plane is dipping (in degrees).

        """
        request = MaterialJointSetSlipCriterionService_pb2.SetJointOptionDipDipDirectionPropertyRequest(materialId=self._materialId, objectId=self._objectId, dip=dip, dipDirection=dipDirection)
        self._client.callFunction(self._stub.SetJointOptionDipDipDirectionProperty, request)
        
                
from rs3._client import Client
from rs3._proxyObject import _ProxyObject
from rs3.properties.material.constitutiveModel.jointOption.MaterialJoint import MaterialJoint
import rs3.generatedFiles.MaterialJointService_pb2_grpc as MaterialJointService_pb2_grpc
import rs3.generatedFiles.MaterialJointService_pb2 as MaterialJointService_pb2
import rs3.generatedFiles.MaterialDataService_pb2_grpc as MaterialDataService_pb2_grpc
from ._PropertyAccessor import BasePropertyAccessor
class MaterialJointOptions(_ProxyObject):
    """
    Define material joint properites.
    
    Example:
        See :ref:`joint_control_examples`.
    """
    def __init__(self, client: Client, id: str):
        super().__init__(client, id)
        self._stub = MaterialJointService_pb2_grpc.MaterialJointServiceStub(client.channel)
        self._materialDataService = MaterialDataService_pb2_grpc.MaterialDataServiceStub(self._client.channel)
        self._propertyAccessor = BasePropertyAccessor(client, self._objectId, self._materialDataService)
    
    def getJoint(self, jointIndex: int) -> MaterialJoint:
        """
        Get joint of the joint material. jointIndex can be 0, 1, and 2.
        """
        request = MaterialJointService_pb2.GetJointRequest(objectId=self._objectId,jointIndex=jointIndex)
        result : MaterialJointService_pb2.GetJointResponse = self._client.callFunction(self._stub.GetJoint, request)
        return MaterialJoint(self._client, self._objectId, result.jointId)
    
    def setNumberOfJoint(self, value: int):
        self._propertyAccessor.setIntProperty("JointsCount", value)
    def getNumberOfJoint(self) -> int:
        return self._propertyAccessor.getIntProperty("JointsCount")
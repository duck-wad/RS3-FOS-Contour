import rs3.generatedFiles.FieldStressService_pb2_grpc as FieldStressService_pb2_grpc
from rs3.properties._PropertyAccessor import PropertyAccessor
from rs3._proxyObject import _ProxyObject
from rs3._client import Client
from rs3.loadings.LoadingEnums import *
from rs3.loadings.fieldStress.Constant import Constant
from rs3.loadings.fieldStress.Gravity import Gravity
from rs3.loadings.fieldStress.AdvancedConstant import AdvancedConstant
from rs3.loadings.fieldStress.AdvancedGravity import AdvancedGravity

class FieldStress(_ProxyObject):
    """
    Modify field stress parameters.

    Attributes:
        Constant (Constant): Reference object for modifying property.
        Gravity (Gravity): Reference object for modifying property.
        AdvancedConstant (AdvancedConstant): Reference object for modifying property.
        AdvancedGravity (AdvancedGravity): Reference object for modifying property.

    Examples:
        See :ref:`field_stress_example`.

    """
    def __init__(self, client : Client, projectID : str):
        super().__init__(client, projectID)
        self._fieldStressService = FieldStressService_pb2_grpc.FieldStressServiceStub(self._client.channel)
        self._propertyAccessor = PropertyAccessor(client, projectID, self._fieldStressService)
        self.Constant = Constant(client, projectID)
        self.Gravity = Gravity(client, projectID)
        self.AdvancedConstant = AdvancedConstant(client, projectID)
        self.AdvancedGravity = AdvancedGravity(client, projectID)

    def getType(self) -> FieldStressType:
        return self._propertyAccessor.getEnumValue("StressType", FieldStressType)

    def setType(self, fieldStressType : FieldStressType):
        self._propertyAccessor.setEnumValue("StressType", fieldStressType.value)

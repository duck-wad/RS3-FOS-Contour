from rs3._client import Client
from rs3.properties.PropertyEnums import *
from rs3._proxyObject import _ProxyObject
from ._PropertyAccessor import MaterialStrengthFunctionPropertyAccessor
from rs3.properties.material.constitutiveModel.stiffness.LinearIsotropic import LinearIsotropic
from rs3.properties.material.constitutiveModel.stiffness.TransverselyIsotropic import TransverselyIsotropic
from rs3.properties.material.constitutiveModel.stiffness.Orthotropic import Orthotropic
from rs3.properties.material.constitutiveModel.stiffness.DuncanChangHyperbolic import DuncanChangHyperbolic
from rs3.properties.material.constitutiveModel.stiffness.NonlinearIsotropic import NonlinearIsotropic
from rs3.properties.material.constitutiveModel.UnsaturatedZoneCalculations import UnsaturatedZoneCalculations
from rs3.properties._PropertyAccessor import PropertyAccessor as BasePropertyAccessor
import rs3.generatedFiles.MaterialDataService_pb2_grpc as MaterialDataService_pb2_grpc

class DiscreteFunction(_ProxyObject):
    def __init__(self, client: Client, id: str):
        super().__init__(client, id)
        self._propertyAccessor = MaterialStrengthFunctionPropertyAccessor(client, id)
        self._stiffnessPropertyAccessor = BasePropertyAccessor(client, id, MaterialDataService_pb2_grpc.MaterialDataServiceStub(self._client.channel))
        self.LinearIsotropicStiffness = LinearIsotropic(client, id)
        self.TransverselyIsotropicStiffness = TransverselyIsotropic(client, id)
        self.OrthotropicStiffness = Orthotropic(client, id)
        self.DuncanChangHyperbolicStiffness = DuncanChangHyperbolic(client, id)
        self.NonlinearIsotropicStiffness = NonlinearIsotropic(client, id)
        self.UnsaturatedZoneCalculations = UnsaturatedZoneCalculations(client, id)
        
    def getElasticType(self) -> MaterialElasticityTypes:
        return self._stiffnessPropertyAccessor.getEnumValue("StiffnessType", MaterialElasticityTypes)
    def setElasticType(self, StiffnessType : MaterialElasticityTypes):
        self._stiffnessPropertyAccessor.setEnumValue("StiffnessType", StiffnessType.value)
        
    def getDiscreteFunctionName(self) -> str:
        return self._propertyAccessor.getSelectedFunctionProperty(ConstitutiveModelTypes.DISCRETE_FUNCTION, "SelectedFunctionID")
    def setDiscreteFunctionByName(self, name: str):
        self._propertyAccessor.setSelectedFunctionProperty(ConstitutiveModelTypes.DISCRETE_FUNCTION, "SelectedFunctionID", name)

    def getApplySSRShearStrengthReduction(self) -> bool:
        return self._propertyAccessor.getBoolValue("UseSSR")
    def setApplySSRShearStrengthReduction(self, value: bool):
        self._propertyAccessor.setBoolValue("UseSSR", value)
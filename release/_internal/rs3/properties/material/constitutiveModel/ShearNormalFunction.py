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

class ShearNormalFunction(_ProxyObject):
    def __init__(self, client : Client, materialID : str):
        super().__init__(client, materialID)
        self._propertyAccessor = MaterialStrengthFunctionPropertyAccessor(client, materialID)
        self._stiffnessPropertyAccessor = BasePropertyAccessor(client, materialID, MaterialDataService_pb2_grpc.MaterialDataServiceStub(self._client.channel))
        self.LinearIsotropicStiffness = LinearIsotropic(client, materialID)
        self.TransverselyIsotropicStiffness = TransverselyIsotropic(client, materialID)
        self.OrthotropicStiffness = Orthotropic(client, materialID)
        self.DuncanChangHyperbolicStiffness = DuncanChangHyperbolic(client, materialID)
        self.NonlinearIsotropicStiffness = NonlinearIsotropic(client, materialID)
        self.UnsaturatedZoneCalculations = UnsaturatedZoneCalculations(client, materialID)
        
    def getElasticType(self) -> MaterialElasticityTypes:
        return self._stiffnessPropertyAccessor.getEnumValue("StiffnessType", MaterialElasticityTypes)
    def setElasticType(self, StiffnessType : MaterialElasticityTypes):
        self._stiffnessPropertyAccessor.setEnumValue("StiffnessType", StiffnessType.value)

    def getShearNormalFunctionName(self) -> str:
        return self._propertyAccessor.getSelectedFunctionProperty(ConstitutiveModelTypes.SHEAR_NORMAL_FUNCTION, "SelectedFunctionID")
    def setShearNormalFunctionByName(self, name: str):
        self._propertyAccessor.setSelectedFunctionProperty(ConstitutiveModelTypes.SHEAR_NORMAL_FUNCTION, "SelectedFunctionID", name)
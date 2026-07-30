import rs3.generatedFiles.MaterialDataService_pb2_grpc as MaterialDataService_pb2_grpc
from rs3._client import Client
from rs3.properties.PropertyEnums import *
from rs3._proxyObject import _ProxyObject
from rs3.properties._PropertyAccessor import PropertyAccessor
from rs3.properties.material.constitutiveModel.AnisotropicLinear import AnisotropicLinear
from rs3.properties.material.constitutiveModel.BarcelonaBasic import BarcelonaBasic
from rs3.properties.material.constitutiveModel.BartonBandis import BartonBandis
from rs3.properties.material.constitutiveModel.BoundingSurfacePlasticity import BoundingSurfacePlasticity
from rs3.properties.material.constitutiveModel.CamClay import CamClay
from rs3.properties.material.constitutiveModel.ChSoil import ChSoil
from rs3.properties.material.constitutiveModel.CySoil import CySoil
from rs3.properties.material.constitutiveModel.DiscreteFunction import DiscreteFunction
from rs3.properties.material.constitutiveModel.DoubleYield import DoubleYield
from rs3.properties.material.constitutiveModel.DruckerPrager import DruckerPrager
from rs3.properties.material.constitutiveModel.GeneralizedAnisotropic import GeneralizedAnisotropic
from rs3.properties.material.constitutiveModel.GeneralizedHoekBrown import GeneralizedHoekBrown
from rs3.properties.material.constitutiveModel.HardeningSoil import HardeningSoil
from rs3.properties.material.constitutiveModel.HardeningSoilWithSmallStrain import HardeningSoilWithSmallStrain
from rs3.properties.material.constitutiveModel.HoekBrown import HoekBrown
from rs3.properties.material.constitutiveModel.Hyperbolic import Hyperbolic
from rs3.properties.material.constitutiveModel.JointedGeneralizedHoekBrown import JointedGeneralizedHoekBrown
from rs3.properties.material.constitutiveModel.JointedMohrCoulomb import JointedMohrCoulomb
from rs3.properties.material.constitutiveModel.ManzariAndDafalias import ManzariAndDafalias
from rs3.properties.material.constitutiveModel.ModifiedCamClay import ModifiedCamClay
from rs3.properties.material.constitutiveModel.MohrCoulomb import MohrCoulomb
from rs3.properties.material.constitutiveModel.MohrCoulombWithCap import MohrCoulombWithCap
from rs3.properties.material.constitutiveModel.Norsand import Norsand
from rs3.properties.material.constitutiveModel.PowerCurve import PowerCurve
from rs3.properties.material.constitutiveModel.Shansep import Shansep
from rs3.properties.material.constitutiveModel.ShearNormalFunction import ShearNormalFunction
from rs3.properties.material.constitutiveModel.SnowdenAnisotropicLinear import SnowdenAnisotropicLinear
from rs3.properties.material.constitutiveModel.SofteningHardening import SofteningHardening
from rs3.properties.material.constitutiveModel.SoftSoil import SoftSoil
from rs3.properties.material.constitutiveModel.SoftSoilCreep import SoftSoilCreep
from rs3.properties.material.constitutiveModel.SwellingRock import SwellingRock
from rs3.properties.material.constitutiveModel.VerticalStressRatio import VerticalStressRatio

class ConstitutiveModel(_ProxyObject):
    """
	Examples:
		See :ref:`material_constitutive_models_example`.
    """
    def __init__(self, client : Client, materialID : str):
        super().__init__(client, materialID)
        self._materialDataService = MaterialDataService_pb2_grpc.MaterialDataServiceStub(self._client.channel)
        self._propertyAccessor = PropertyAccessor(client, materialID, self._materialDataService)
        self.AnisotropicLinear = AnisotropicLinear(client, materialID)
        self.BarcelonaBasic = BarcelonaBasic(client, materialID)
        self.BartonBandis = BartonBandis(client, materialID)
        self.BoundingSurfacePlasticity = BoundingSurfacePlasticity(client, materialID)
        self.CamClay = CamClay(client, materialID)
        self.ChSoil = ChSoil(client, materialID)
        self.CySoil = CySoil(client, materialID)
        self.DiscreteFunction = DiscreteFunction(client, materialID)
        self.DoubleYield = DoubleYield(client, materialID)
        self.DruckerPrager = DruckerPrager(client, materialID)
        self.GeneralizedAnisotropic = GeneralizedAnisotropic(client, materialID)
        self.GeneralizedHoekBrown = GeneralizedHoekBrown(client, materialID)
        self.HardeningSoil = HardeningSoil(client, materialID)
        self.HardeningSoilWithSmallStrain = HardeningSoilWithSmallStrain(client, materialID)
        self.HoekBrown = HoekBrown(client, materialID)
        self.Hyperbolic = Hyperbolic(client, materialID)
        self.JointedGeneralizedHoekBrown = JointedGeneralizedHoekBrown(client, materialID)
        self.JointedMohrCoulomb = JointedMohrCoulomb(client, materialID)
        self.ManzariAndDafalias = ManzariAndDafalias(client, materialID)
        self.ModifiedCamClay = ModifiedCamClay(client, materialID)
        self.MohrCoulomb = MohrCoulomb(client, materialID)
        self.MohrCoulombWithCap = MohrCoulombWithCap(client, materialID)
        self.Norsand = Norsand(client, materialID)
        self.PowerCurve = PowerCurve(client, materialID)
        self.Shansep = Shansep(client, materialID)
        self.ShearNormalFunction = ShearNormalFunction(client, materialID)
        self.SnowdenAnisotropicLinear = SnowdenAnisotropicLinear(client, materialID)
        self.SofteningHardening = SofteningHardening(client, materialID)
        self.SoftSoil = SoftSoil(client, materialID)
        self.SoftSoilCreep = SoftSoilCreep(client, materialID)
        self.SwellingRock = SwellingRock(client, materialID)
        self.VerticalStressRatio = VerticalStressRatio(client, materialID)
        
        
    def getConstitutiveModel(self) -> ConstitutiveModelTypes:
        return self._propertyAccessor.getEnumValue("StrengthType", ConstitutiveModelTypes)
    def setConstitutiveModel(self, constitutiveModelTypes : ConstitutiveModelTypes):
        self._propertyAccessor.setEnumValue("StrengthType", constitutiveModelTypes.value)
        
    
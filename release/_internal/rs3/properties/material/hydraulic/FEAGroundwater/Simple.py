from rs3._client import Client
from ._PropertyAccessor import PropertyAccessor
from rs3._proxyObject import _ProxyObject
from rs3.properties.stageFactors.IStageFactorBase import IStageFactorBase
from rs3.properties.stageFactors.StageFactorBaseInterfaces import AbsoluteStageFactorInterface
from rs3.properties.PropertyEnums import *
from rs3.properties.material.hydraulic.FEAGroundwater.HydraulicParametersCommon import HydraulicParametersCommon, HydraulicParametersCommonStageFactor, HydraulicParametersCommonDefinedStageFactor

class SimpleStageFactor(HydraulicParametersCommonStageFactor):
    """
	Examples:
		See :ref:`material_hydraulic_example`.
    """
    def __init__(self, id: str, stageFactorId: str, client: Client):
        super().__init__(id, stageFactorId, client)
        
class SimpleStageFactor(SimpleStageFactor, HydraulicParametersCommonDefinedStageFactor):
    """
	Examples:
		See :ref:`material_hydraulic_example`.
    """
    pass

class Simple(HydraulicParametersCommon):
    """
	Examples:
		See :ref:`material_hydraulic_example`.
    """
    def __init__(self, client: Client, id: str):
        super().__init__(client, id)
        self._propertyAccessor = PropertyAccessor(client, id)
        self.StageFactorInterface = AbsoluteStageFactorInterface[SimpleStageFactor, SimpleStageFactor](id, client, SimpleStageFactor, SimpleStageFactor)
    
    def setSoilType(self, simpleSoilType : EnhancedSimpleSoilTypes):
        self._propertyAccessor.setEnumValue("SoilType", simpleSoilType.value)
    def getSoilType(self) -> EnhancedSimpleSoilTypes:
        return self._propertyAccessor.getEnumValue("SoilType", EnhancedSimpleSoilTypes)
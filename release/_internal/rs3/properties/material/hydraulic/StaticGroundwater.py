from rs3._client import Client
from ._PropertyAccessor import PropertyAccessor
from rs3.properties.PropertyEnums import *
from rs3.properties.material.hydraulic.PhreaticConditions import PhreaticConditions
from rs3.properties.material.hydraulic.WaterConditions import WaterConditions
from rs3.properties.stageFactors.IStageFactorBase import IStageFactorBase
import rs3.generatedFiles.MaterialHydraulicDataService_pb2_grpc as MaterialHydraulicDataService_pb2_grpc
import rs3.generatedFiles.HydraulicStageFactorService_pb2_grpc as HydraulicStageFactorService_pb2_grpc
import rs3.generatedFiles.HydraulicStageFactorService_pb2 as HydraulicStageFactorService_pb2
from rs3.properties.stageFactors.StageFactorBaseInterfaces import AbsoluteStageFactorInterface
class StaticGroundwaterStageFactor(IStageFactorBase):
    """
	Examples:
		See :ref:`material_hydraulic_example`.
    """
    def __init__(self, id : str, stageFactorID : str, client : Client):
        self._stub = HydraulicStageFactorService_pb2_grpc.HydraulicStageFactorServiceStub(client.channel)
        super().__init__(id, stageFactorID, client, self._stub)
        self._propertyAccessor = PropertyAccessor(client, id)
    def getWaterCondition(self) -> str:
        """
        Retrieve the name of the current default water condition in phreatic surface method and initial water condition in the steady state or trainsient state methods of the current material for each stage.

        Returns:
            str: The name of the initial water condition or "Dry" if the waterType is `DRY`.
        """
        request = HydraulicStageFactorService_pb2.GetInitialWaterConditionRequest(propertyId=self.parentID, stageFactorId=self._objectId)
        response : HydraulicStageFactorService_pb2.GetInitialWaterConditionResponse = self._client.callFunction(self._stub.GetInitialWaterCondition, request)
        return response.waterTableName

class StaticGroundwaterDefinedStageFactor(StaticGroundwaterStageFactor):
    """
    Examples:
        :ref:`material_hydraulic_example`
    """
    def setWaterCondition(self, waterType : StaticWaterModes, name : str = ""):
        """
        Set the default water condition in phreatic surface method and initial water condition in the steady state or trainsient state methods of the current material for each stage.

        This defines the starting water condition used in hydraulic calculations.

        - If `waterType` is `DRY`, no `name` is required.  
        - If `waterType` refers to a water surface, PWP interpolation surface, or PWP point set, the `name` must match an existing water table.  
        - If `waterType` is `USER_DEFINED_VALUE`, the `name` must match an existing user-defined pore water pressure (PWP) or Ru entry.

        Args:
            waterType (WaterConditionWaterType):
                The type of water condition to set.
            name (str, optional):
                The name of the water table, PWP dataset, or user-defined PWP to use. Required for all types except `DRY`. Defaults to an empty string.

        Raises:
            ValueError: If `name` is required for the given `waterType` but is not provided.
        """
        request = HydraulicStageFactorService_pb2.SetInitialWaterConditionRequest(propertyId=self.parentID, stageFactorId=self._objectId, waterType=waterType.value, waterTableName=name)
        self._client.callFunction(self._stub.SetInitialWaterCondition, request)
        
class StaticGroundwater(WaterConditions):
    """
	Examples:
		See :ref:`material_hydraulic_example`.
    """
    def __init__(self, client: Client, id: str):
        super().__init__(client, id)
        self._stub = MaterialHydraulicDataService_pb2_grpc.MaterialHydraulicDataServiceStub(client.channel)
        self.StageFactorInterface = AbsoluteStageFactorInterface[StaticGroundwaterDefinedStageFactor, StaticGroundwaterStageFactor](id, client, StaticGroundwaterDefinedStageFactor, StaticGroundwaterStageFactor)
    
    def getStaticWaterModeByName(self, waterConditionName: str) -> PhreaticConditions:
        return super().getWaterConditionPropertyByName(waterConditionName=waterConditionName)
    def getAllStaticWaterModes(self) -> list[PhreaticConditions]:
        return super().getWaterConditionProperties()
    
    def setStaticWaterMode(self, waterType : StaticWaterModes, name : str = ""):
        """
        Set the default water condition in phreatic surface method of the current material.

        This defines the starting water condition used in hydraulic calculations.

        - If `waterType` is `DRY`, no `name` is required.  
        - If `waterType` refers to a water surface, PWP interpolation surface, or PWP point set, the `name` must match an existing water table.  
        - If `waterType` is `USER_DEFINED_VALUE`, the `name` must match an existing user-defined pore water pressure (PWP) or Ru entry.

        Args:
            waterType (WaterConditionWaterType):
                The type of water condition to set.
            name (str, optional):
                The name of the water table, PWP dataset, or user-defined PWP to use. Required for all types except `DRY`. Defaults to an empty string.

        Raises:
            ValueError: If `name` is required for the given `waterType` but is not provided.
        """
        super().setWaterConditions(waterType=waterType, name=name)
    def getStaticWaterMode(self) -> str:
        """
        Retrieve the name of the current default water condition in phreatic surface method of the current material.

        Returns:
            str: The name of the initial water condition or "Dry" if the waterType is `DRY`.
        """
        return super().getWaterConditions()
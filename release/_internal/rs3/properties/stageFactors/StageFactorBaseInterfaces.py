from rs3.properties.stageFactors._StageFactorInterface import _AbsoluteStageFactorInterface
from rs3.properties.PropertyEnums import *
from rs3._client import Client
from typing import TypeVar

DefinedStageFactor = TypeVar('DefinedStageFactor')
StageFactor = TypeVar('StageFactor')

class AbsoluteStageFactorInterface(_AbsoluteStageFactorInterface[DefinedStageFactor, StageFactor]):
    def __init__(self, propertyID : str, client : Client, definedStageFactorClass, stageFactorClass, useJointOptions : bool = False, materialId : str = None):
        super().__init__(propertyID, client, definedStageFactorClass, stageFactorClass, useJointOptions, materialId)

    def getDefinedStageFactors(self) -> dict[int, DefinedStageFactor]:
        """
		Returns a map of stage factors. The key is the absolute or relative stage at which the stage factor is applied. The value is the stage factor object
		"""
        return self._getDefinedStageFactors()
    
    def getStageFactor(self, stage : int) -> StageFactor:
        """
		Returns the stage factor for the given stage.
		"""
        return self._getStageFactor(stage)
    
import rs3.generatedFiles.StageFactorService_pb2 as StageFactorService_pb2
import rs3.generatedFiles.RelativeStageFactorService_pb2 as RelativeStageFactorService_pb2
import rs3.generatedFiles.RelativeStageFactorService_pb2_grpc as RelativeStageFactorService_pb2_grpc
from rs3.properties.stageFactors.StageFactorBaseInterfaces import AbsoluteStageFactorInterface as StageFactorBaseInterfaces
from rs3.properties.PropertyEnums import *
from rs3._client import Client
from typing import TypeVar

DefinedStageFactor = TypeVar('DefinedStageFactor')
StageFactor = TypeVar('StageFactor')

class AbsoluteStageFactorInterface(StageFactorBaseInterfaces[DefinedStageFactor, StageFactor]):
    def __init__(self, propertyID : str, client : Client, definedStageFactorClass, stageFactorClass, useJointOptions : bool = False, materialId : str = None):
        super().__init__(propertyID, client, definedStageFactorClass, stageFactorClass, useJointOptions, materialId)
        
    def createStageFactor(self, stage : int) -> DefinedStageFactor:
        """
        Creates a stage factor for the given stage.

        Note: 
            Invalidates any existing stage factor proxies. Get them again using getDefinedStageFactors or getStageFactor.
        """
        return self._createStageFactor(stage)

    def setDefinedStageFactors(self, stageFactors : dict[int, StageFactor]):
        """
        Sets the defined stage factors to those given.

        Note: 
            Invalidates any existing stage factor proxies. Get them again using getDefinedStageFactors or getStageFactor.
        """
        convertedStageFactors = {}
        for stageNum, stageFactor in stageFactors.items():
            convertedStageFactors[stageNum] = StageFactorService_pb2.StageFactorProperty(stageFactorID = stageFactor._objectId)
        self._setDefinedStageFactors(StageFactorMethodType.ABSOLUTE_STAGE_FACTOR, convertedStageFactors)

    def getStageFactorMethod(self) -> StageFactorMethodType:
        """
        Returns the method used when defining stage factors.
        """
        return StageFactorMethodType.ABSOLUTE_STAGE_FACTOR
    
class RelativeStageFactorInterface(AbsoluteStageFactorInterface[DefinedStageFactor, StageFactor]):
    def __init__(self, propertyID : str, client : Client, definedStageFactorClass, stageFactorClass):
        super().__init__(propertyID, client, definedStageFactorClass, stageFactorClass)
        self._relativeStageFactorServiceStub = RelativeStageFactorService_pb2_grpc.RelativeStageFactorServiceStub(self._client.channel)
    def _getIsRelativeStaging(self) -> bool:
        getIsRelativeStagingRequest = RelativeStageFactorService_pb2.GetIsRelativeStagingRequest(propertyID = self._propertyID)
        getIsRelativeStagingResponse : RelativeStageFactorService_pb2.GetIsRelativeStagingResponse = self._client.callFunction(self._relativeStageFactorServiceStub.GetIsRelativeStaging, getIsRelativeStagingRequest)
        return getIsRelativeStagingResponse.isRelativeStaging
    

    def setDefinedStageFactors(self, method : StageFactorMethodType, stageFactors : dict[int, StageFactor]):
        """
        Sets the defined stage factors to those given. The method indicates if the stages in the keys of the map are absolute or relative.

        Note: 
            - Invalidates any existing stage factor proxies. Get them again using getDefinedStageFactors or getStageFactor.
            - If the 'stageFactors' dictionary is empty (stageFactors = {}), the stage factor at the installed stage (stage 0) will remain, and its factor values will be reset to their defaults.
        """
        convertedStageFactors = {}
        for stageNum, stageFactor in stageFactors.items():
            convertedStageFactors[stageNum] = StageFactorService_pb2.StageFactorProperty(stageFactorID = stageFactor._objectId)
        self._setDefinedStageFactors(method, convertedStageFactors)

    def getStageFactorMethod(self) -> StageFactorMethodType:
        """
        Returns the method used when defining stage factors.
        """
        return StageFactorMethodType.RELATIVE_STAGE_FACTOR if self._getIsRelativeStaging() else StageFactorMethodType.ABSOLUTE_STAGE_FACTOR
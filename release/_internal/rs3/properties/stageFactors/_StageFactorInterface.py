import rs3.generatedFiles.StageFactorService_pb2 as StageFactorService_pb2
import rs3.generatedFiles.StageFactorService_pb2_grpc as StageFactorService_pb2_grpc
from rs3.properties.PropertyEnums import *
from rs3._client import Client
from typing import TypeVar, Generic

DefinedStageFactor = TypeVar('DefinedStageFactor')
StageFactor = TypeVar('StageFactor')

class _AbsoluteStageFactorInterface(Generic[DefinedStageFactor, StageFactor]):
    def __init__(self, propertyID : str, client : Client, definedStageFactorClass, stageFactorClass, useJointOptions : bool = False, materialId : str = None):
        self._propertyID = propertyID
        self._client = client
        self._definedStageFactorClass = definedStageFactorClass
        self._stageFactorClass = stageFactorClass
        self._stageFactorServiceStub = StageFactorService_pb2_grpc.StageFactorServiceStub(self._client.channel)
        self._useJointOptions = useJointOptions
        self._materialId = materialId

    def _getDefinedStageFactors(self) -> dict[int, DefinedStageFactor]:
        getDefinedStageFactorsRequest = StageFactorService_pb2.GetDefinedStageFactorsRequest(propertyID = self._propertyID)
        getDefinedStageFactorsResponse : StageFactorService_pb2.GetDefinedStageFactorsResponse = self._client.callFunction(self._stageFactorServiceStub.GetDefinedStageFactors, getDefinedStageFactorsRequest)
        definedStageFactors = {}
        if(self._useJointOptions):
            for stageFactorProp in getDefinedStageFactorsResponse.stageFactors:
                definedStageFactors[stageFactorProp.stageAppliedTo] = self._definedStageFactorClass(self._propertyID, stageFactorProp.stageFactorID, self._client, self._materialId)
        else:  
            for stageFactorProp in getDefinedStageFactorsResponse.stageFactors:
                definedStageFactors[stageFactorProp.stageAppliedTo] = self._definedStageFactorClass(self._propertyID, stageFactorProp.stageFactorID, self._client)
        return definedStageFactors
    def _getStageFactor(self, stage : int) -> StageFactor:
        getStageFactorRequest = StageFactorService_pb2.GetStageFactorRequest(propertyID = self._propertyID, stage = stage)
        if(self._useJointOptions):
            getStageFactorResponse : StageFactorService_pb2.GetStageFactorResponse = self._client.callFunction(self._stageFactorServiceStub.GetStageFactor, getStageFactorRequest)
            return self._stageFactorClass(self._propertyID, getStageFactorResponse.stageFactor.stageFactorID, self._client, self._materialId)
        else:  
            getStageFactorResponse : StageFactorService_pb2.GetStageFactorResponse = self._client.callFunction(self._stageFactorServiceStub.GetStageFactor, getStageFactorRequest)
            return self._stageFactorClass(self._propertyID, getStageFactorResponse.stageFactor.stageFactorID, self._client)
    def _createStageFactor(self, stage : int) -> DefinedStageFactor:
        createStageFactorRequest = StageFactorService_pb2.CreateStageFactorRequest(propertyID = self._propertyID, stage = stage, useJointOptions=self._useJointOptions)
        createStageFactorResponse : StageFactorService_pb2.CreateStageFactorResponse = self._client.callFunction(self._stageFactorServiceStub.CreateStageFactor, createStageFactorRequest)
        if(self._useJointOptions):
            return self._definedStageFactorClass(self._propertyID, createStageFactorResponse.stageFactor.stageFactorID, self._client, self._materialId)
        else:
            return self._definedStageFactorClass(self._propertyID, createStageFactorResponse.stageFactor.stageFactorID, self._client)
    def _setDefinedStageFactors(self, method : StageFactorMethodType, stageFactors : dict[int, StageFactorService_pb2.StageFactorProperty]):
        setDefinedStageFactorsRequest = StageFactorService_pb2.SetDefinedStageFactorsRequest(propertyID = self._propertyID, stageFactorDictionary = stageFactors, isRelativeStageFactors = method == StageFactorMethodType.RELATIVE_STAGE_FACTOR, useJointOptions=self._useJointOptions)
        self._client.callFunction(self._stageFactorServiceStub.SetDefinedStageFactors, setDefinedStageFactorsRequest)
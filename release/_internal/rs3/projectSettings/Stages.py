from rs3.projectSettings.ProjectSettingEnums import *
from rs3._client import Client
from ._PropertyAccessor import StagesPropertyAccessor
import rs3.generatedFiles.ProjectSettingsDataService_pb2_grpc as ProjectSettingsDataService_pb2_grpc
import rs3.generatedFiles.ProjectSettingsDataService_pb2 as ProjectSettingsDataService_pb2
from rs3._proxyObject import _ProxyObject


class Stages(_ProxyObject):
    """
    Edit the number of stages and define time, PWP method and dynamic analysis.
    
    Examples:
        See :ref:`project_settings_example`.

    """
    def __init__(self, client: Client, projectId: str):
        super().__init__(client, projectId)
        self._propertyAccessor = StagesPropertyAccessor(client, projectId)
        self._stagesService = ProjectSettingsDataService_pb2_grpc.ProjectSettingsDataServiceStub(self._client.channel)

    def getDefinedStageNames(self) -> list[str]:
        request = ProjectSettingsDataService_pb2.GetDefinedStageNamesRequest(_projectId=self._objectId)
        result_ = self._client.callFunction(self._stagesService.GetDefinedStageNames, request)
        result = [obj for obj in result_.result]
        return result

    def setTotalNumberOfStages(self, numberOfStages: int):
        request = ProjectSettingsDataService_pb2.SetTotalNumberOfStagesRequest(_projectId=self._objectId, numberOfStages=numberOfStages)
        self._client.callFunction(self._stagesService.SetTotalNumberOfStages, request)

    def addStages(self, numberOfStages: int, referenceStage: int = -1):
        """
        Add one or more new stages to the project.

        Parameters:
            numberOfStages (int): The number of stages to add. Must be a positive integer. Default is 1.
            referenceStage (int): The index of the stage **after which** new stages will be inserted.
                                If -1 (default), stages are added at the end.

        Behavior:
            - Each value is interpreted as the actual stage number (not zero-based index).
            - If referenceStage is -1 (or omitted), new stages are appended at the end of the current stage list.
            - If referenceStage is a valid index (1-based), new stages are inserted after that stage.

        Raises:
            Exception if the number of stages is invalid or the reference index is out of bounds.

        Examples:
            >>> # Add 2 stages at the end of the project
            >>> model.ProjectSettings.Stages.addStages(2, -1)

            >>> # Add 3 stages after the stage 2
            >>> model.ProjectSettings.Stages.addStages(3, 2)

            >>> # Add 2 stages at the end (same as passing -1)
            >>> model.ProjectSettings.Stages.addStages(numberOfStages=2)

            >>> # Add 1 stage after the stage 5
            >>> model.ProjectSettings.Stages.addStages(numberOfStages=1, referenceStage=5)
            
        """
        request = ProjectSettingsDataService_pb2.AddStagesRequest(_projectId=self._objectId, referenceStage=referenceStage, numberOfStages=numberOfStages)
        self._client.callFunction(self._stagesService.AddStages, request)

    def removeStages(self, numberOfStages: int, startingStage: int = -1):
        """
        Remove one or more stages from the project.

        Parameters:
            numberOfStages (int): The number of stages to remove. Must be a non-negative integer. Default is 1.
            startingStage (int): The index of the first stage to remove. If -1 (default), stages are removed from the end.

        Behavior:
            - Each value is interpreted as the actual stage number (not zero-based index).
            - If `startingStage` is -1, the last `numberOfStages` stages are removed from the end of the stage list.
            - If `startingStage` is a valid index (1-based), removal begins at that starting stage and removes the next 
              `numberOfStages` stages (including the stage at `startingStage`).

        Raises:
            Exception if:
                - `numberOfStages` is negative
                - `startingStage` is less than -1
                - The range defined by `startingStage` and `numberOfStages` exceeds the available stages

        Examples:
            >>> # Remove 2 stages from the end
            >>> model.ProjectSettings.Stages.removeStages(2, -1)

            >>> # Remove 3 stages starting from stage 3 (removes stages 3, 4, 5)
            >>> model.ProjectSettings.Stages.removeStages(3, 3)

            >>> # Remove 1 stage at stage 3
            >>> model.ProjectSettings.Stages.removeStages(startingStage=3)

            >>> # Remove 2 stages from the end (same as passing -1 explicitly)
            >>> model.ProjectSettings.Stages.removeStages(numberOfStages=2)
            
        """
        request = ProjectSettingsDataService_pb2.DeleteStagesRequest(_projectId=self._objectId, startingStage=startingStage, numberOfStages=numberOfStages)
        self._client.callFunction(self._stagesService.DeleteStages, request)

    def removeStagesByList(self, list: list[int]):
        """
        Remove specific stages from the project by specifying their stage numbers (1-based).

        Parameters:
            list (list[int]): A list of **actual stage numbers** (not zero-based index) to be removed.
                            The order of stage numbers in the list does not matter.
                            Duplicates are ignored. An empty list will raise an exception.

        Behavior:
            - Each value in the list is interpreted as the actual stage number (not zero-based index).
            - If any stage number is invalid (less than 1 or greater than total number of stages), an exception will be raised.
            - Valid and unique stages in the list will be removed from the project.

        Raises:
            Exception if:
                - The list is empty
                - Any stage number is less than 1
                - Any stage number exceeds the total number of defined stages

        Examples:
            >>> # Assume there are 13 stages in the model.
            >>> # Remove stages 3, 8, and 2
            >>> model.ProjectSettings.Stages.removeStagesByList([3, 8, 2])

            >>> # Raises exception: list is empty
            >>> model.ProjectSettings.Stages.removeStagesByList([])

            >>> # Raises exception: -2 is not a valid stage number
            >>> model.ProjectSettings.Stages.removeStagesByList([5, 8, -2])

            >>> # Raises exception: 15 exceeds current stage count
            >>> model.ProjectSettings.Stages.removeStagesByList([1, 15, 2])
        """
        request = ProjectSettingsDataService_pb2.DeleteStagesByListRequest( _projectId=self._objectId, stageIndices=list)
        self._client.callFunction(self._stagesService.DeleteStagesByList, request)

    def setName(self, stageNumber: int, name: str):
        self._propertyAccessor.setStringValue("Name", stageNumber, name)

    def getName(self, stageNumber: int) -> str:
        return self._propertyAccessor.getStringValue("Name", stageNumber)

    def setTime(self, stageNumber: int, value: float):
        self._propertyAccessor.setDoubleProperty("Time", stageNumber, value)

    def getTime(self, stageNumber: int) -> float:
        return self._propertyAccessor.getDoubleProperty("Time", stageNumber)

    def setPWPMethod(self, stageNumber: int, value: PWPMethod):
        self._propertyAccessor.setEnumValue("pwp_method", stageNumber, value.value)

    def getPWPMethod(self, stageNumber: int) -> PWPMethod:
        return self._propertyAccessor.getEnumValue("pwp_method", stageNumber, PWPMethod)

    def setIsDynamicStage(self, stageNumber: int, value: bool):
        self._propertyAccessor.setBoolValue("IsDynamic", stageNumber, value)

    def getIsDynamicStage(self, stageNumber: int) -> bool:
        return self._propertyAccessor.getBoolValue("IsDynamic", stageNumber)

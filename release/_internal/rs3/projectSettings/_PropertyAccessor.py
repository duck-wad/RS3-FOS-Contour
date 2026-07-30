from rs3.properties._PropertyAccessor import PropertyAccessor as BasePropertyAccessor
import rs3.generatedFiles.ProjectSettingsDataService_pb2_grpc as ProjectSettingsDataService_pb2_grpc
import rs3.generatedFiles.ProjectSettingsDataService_pb2 as ProjectSettingsDataService_pb2
import rs3.generatedFiles.CommonMessages_pb2 as CommonMessages_pb2
from rs3._client import Client
class PropertyAccessor(BasePropertyAccessor):
    def __init__(self, client : Client, projectId : str):
        super().__init__(client, projectId, ProjectSettingsDataService_pb2_grpc.ProjectSettingsDataServiceStub(client.channel))
        self._projectSettingsDataService = ProjectSettingsDataService_pb2_grpc.ProjectSettingsDataServiceStub(self._client.channel)
        self.projectId = projectId

class UnitsPropertyAccessor(PropertyAccessor):
    def __init__(self, client : Client, projectId : str):
        super().__init__(client, projectId)
        
    def _setProperty(self, propertyName : str, value : CommonMessages_pb2.PropertyValue, resetProperties : bool):
        request = ProjectSettingsDataService_pb2.SetProjectUnitRequest(objectId=self.projectId, 
                                                        propertyName=propertyName,
                                                        value=value,
                                                        resetProperties=resetProperties)
        self._client.callFunction(self._projectSettingsDataService.SetProjectUnits, request)
        
    def _getProperty(self, propertyName : str) -> CommonMessages_pb2.PropertyValue:
        request = CommonMessages_pb2.GetPropertyRequest(objectId=self.projectId, propertyName=propertyName)
        response : CommonMessages_pb2.GetPropertyResponse = self._client.callFunction(self._projectSettingsDataService.GetProjectUnits, request)
        return response.value

    def setEnumValue(self, propertyName: str, value: str, resetProperties : bool):
        self._setProperty(propertyName, CommonMessages_pb2.PropertyValue(enumValue=value), resetProperties)
    
class StagesPropertyAccessor(PropertyAccessor):
    def __init__(self, client : Client, projectId : str):
        super().__init__(client, projectId)
        
    def _setProperty(self, propertyName : str, stageNumber : int, value : CommonMessages_pb2.PropertyValue):
        request = ProjectSettingsDataService_pb2.SetStagePropertyRequest(objectId=self.projectId, 
                                                        propertyName=propertyName,
                                                        stageNumber=stageNumber,
                                                        value=value)
        self._client.callFunction(self._projectSettingsDataService.SetStageProperties, request)
        
    def _getProperty(self, propertyName : str, stageNumber : int) -> CommonMessages_pb2.PropertyValue:
        request = ProjectSettingsDataService_pb2.GetStagePropertyRequest(objectId=self.projectId, propertyName=propertyName, stageNumber=stageNumber)
        response : ProjectSettingsDataService_pb2.GetStagePropertyResponse = self._client.callFunction(self._projectSettingsDataService.GetStageProperties, request)
        return response.value
    
    def getDoubleProperty(self, propertyName : str, stageNumber: int) -> float:
        return self._getProperty(propertyName, stageNumber).doubleValue

    def setDoubleProperty(self, propertyName : str, stageNumber: int, value : float):
        self._setProperty(propertyName, stageNumber, CommonMessages_pb2.PropertyValue(doubleValue=value))
    
    def getBoolValue(self, propertyName: str, stageNumber: int) -> bool:
        return self._getProperty(propertyName, stageNumber).boolValue

    def setBoolValue(self, propertyName: str, stageNumber: int, value: bool):
        self._setProperty(propertyName, stageNumber, CommonMessages_pb2.PropertyValue(boolValue=value))
        
    def getStringValue(self, propertyName: str, stageNumber: int) -> str:
        return self._getProperty(propertyName, stageNumber).stringValue

    def setStringValue(self, propertyName: str, stageNumber: int, value: str):
        self._setProperty(propertyName, stageNumber, CommonMessages_pb2.PropertyValue(stringValue=value))
        
    def getEnumValue(self, propertyName: str, stageNumber: int, enumType):
        return enumType(self._getProperty(propertyName, stageNumber).enumValue)
    
    def setEnumValue(self, propertyName: str, stageNumber: int, value: str):
        self._setProperty(propertyName, stageNumber, CommonMessages_pb2.PropertyValue(enumValue=value))
    
class StressAnalysisPropertyAccessor(PropertyAccessor):
    def __init__(self, client : Client, projectId : str):
        super().__init__(client, projectId)
        
    def _setProperty(self, propertyName : str, value : CommonMessages_pb2.PropertyValue):
        request = CommonMessages_pb2.SetPropertyRequest(objectId=self.projectId, 
                                                        propertyName=propertyName,
                                                        value=value)
        self._client.callFunction(self._projectSettingsDataService.SetStressAnalysis, request)
        
    def _getProperty(self, propertyName : str) -> CommonMessages_pb2.PropertyValue:
        request = CommonMessages_pb2.GetPropertyRequest(objectId=self.projectId, propertyName=propertyName)
        response : CommonMessages_pb2.GetPropertyResponse = self._client.callFunction(self._projectSettingsDataService.GetStressAnalysis, request)
        return response.value
    
class GroundwaterPropertyAccessor(PropertyAccessor):
    def __init__(self, client : Client, projectId : str):
        super().__init__(client, projectId)
        
    def _setProperty(self, propertyName : str, value : CommonMessages_pb2.PropertyValue):
        request = CommonMessages_pb2.SetPropertyRequest(objectId=self.projectId, 
                                                        propertyName=propertyName,
                                                        value=value)
        self._client.callFunction(self._projectSettingsDataService.SetGroundwater, request)
        
    def _getProperty(self, propertyName : str) -> CommonMessages_pb2.PropertyValue:
        request = CommonMessages_pb2.GetPropertyRequest(objectId=self.projectId, propertyName=propertyName)
        response : CommonMessages_pb2.GetPropertyResponse = self._client.callFunction(self._projectSettingsDataService.GetGroundwater, request)
        return response.value
    
class SSRPropertyAccessor(PropertyAccessor):
    def __init__(self, client : Client, projectId : str):
        super().__init__(client, projectId)
        
    def _setProperty(self, propertyName : str, value : CommonMessages_pb2.PropertyValue):
        request = CommonMessages_pb2.SetPropertyRequest(objectId=self.projectId, 
                                                        propertyName=propertyName,
                                                        value=value)
        self._client.callFunction(self._projectSettingsDataService.SetShearStrengthReduction, request)
        
    def _getProperty(self, propertyName : str) -> CommonMessages_pb2.PropertyValue:
        request = CommonMessages_pb2.GetPropertyRequest(objectId=self.projectId, propertyName=propertyName)
        response : CommonMessages_pb2.GetPropertyResponse = self._client.callFunction(self._projectSettingsDataService.GetShearStrengthReduction, request)
        return response.value
    
class DynamicPropertyAccessor(PropertyAccessor):
    def __init__(self, client : Client, projectId : str):
        super().__init__(client, projectId)
        
    def _setProperty(self, propertyName : str, value : CommonMessages_pb2.PropertyValue):
        request = CommonMessages_pb2.SetPropertyRequest(objectId=self.projectId, 
                                                        propertyName=propertyName,
                                                        value=value)
        self._client.callFunction(self._projectSettingsDataService.SetDynamic, request)
        
    def _getProperty(self, propertyName : str) -> CommonMessages_pb2.PropertyValue:
        request = CommonMessages_pb2.GetPropertyRequest(objectId=self.projectId, propertyName=propertyName)
        response : CommonMessages_pb2.GetPropertyResponse = self._client.callFunction(self._projectSettingsDataService.GetDynamic, request)
        return response.value
    
    



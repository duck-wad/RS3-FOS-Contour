from rs3.properties.PropertyEnums import *
class BaseStiffness():
    def getUseUnloadingCondition(self) -> bool:
        return self._basePropertyAccessor.getBoolValue("UseUnloading")
    def setUseUnloadingCondition(self, value: bool):
        self._basePropertyAccessor.setBoolValue("UseUnloading", value)
        
    def getUnloadingCondition(self) -> UnloadingConditions:
        return self._basePropertyAccessor.getEnumValue("UnloadingStiffness", UnloadingConditions)  
    def setUnloadingCondition(self, UnloadingCondition : UnloadingConditions):
        self._basePropertyAccessor.setEnumValue("UnloadingStiffness", UnloadingCondition.value)
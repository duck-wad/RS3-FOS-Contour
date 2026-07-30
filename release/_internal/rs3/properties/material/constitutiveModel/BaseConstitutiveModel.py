from rs3.properties.PropertyEnums import *
class BaseConstitutiveModel():
    def getElasticType(self) -> MaterialElasticityTypes:
        return self._stiffnessPropertyAccessor.getEnumValue("StiffnessType", MaterialElasticityTypes)
    def setElasticType(self, StiffnessType : MaterialElasticityTypes):
        self._stiffnessPropertyAccessor.setEnumValue("StiffnessType", StiffnessType.value)
        
    def getMaterialType(self) -> MaterialType:
        return MaterialType(self._propertyAccessor.getBoolValue("IsPlastic"))
    def setMaterialType(self, materialType: MaterialType):
        return self._propertyAccessor.setBoolValue("IsPlastic", materialType.value)
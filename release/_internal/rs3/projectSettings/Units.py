from rs3.projectSettings.ProjectSettingEnums import *
from rs3._client import Client
from ._PropertyAccessor import UnitsPropertyAccessor
from rs3._proxyObject import _ProxyObject

class Units(_ProxyObject):
    """
    Modify the units of a model.
    
    Examples:
		See :ref:`project_settings_example`.
    """
    def __init__(self, client: Client, projectId: str):
        super().__init__(client, projectId)
        self._propertyAccessor = UnitsPropertyAccessor(client, projectId)
        self.projectId = projectId
        
    def setUnitSystem(self, value : UnitSystemType, resetProperties : bool = True):
        """
        Sets the unit system for the current project.

        By default, if the unit is changed, script will reset all unit-dependent
        property values in the project to their default values. This will reset the 
        Field Stress settings, and ALL properties for Material, Bolts, Liners, and Joints.
        To preserve existing values when changing the unit, set `resetProperties` to False.

        It is recommended to set the desired unit at the beginning of the script or project
        to avoid unintended resets.

        Parameters:
            value (UnitSystemType): The unit system to apply.
            resetProperties (bool, optional): Whether to reset unit-dependent property values to
                their defaults. Defaults to True.
        """
        self._propertyAccessor.setEnumValue("Unit_System", value.value, resetProperties)
        
    def getUnitSystem(self) -> UnitSystemType:
        return self._propertyAccessor.getEnumValue("Unit_System", UnitSystemType)
    
    def setTimeUnits(self, value : TimeUnitsType, resetProperties : bool = True):
        """
        Sets the time unit for the current project.

        By default, if the unit is changed, script will reset all unit-dependent
        property values in the project to their default values. This will reset the 
        Field Stress settings, and ALL properties for Material, Bolts, Liners, and Joints.
        To preserve existing values when changing the unit, set `resetProperties` to False.

        It is recommended to set the desired unit at the beginning of the script or project
        to avoid unintended resets.

        Parameters:
            value (TimeUnitsType): The unit system to apply.
            resetProperties (bool, optional): Whether to reset unit-dependent property values to
                their defaults. Defaults to True.
        """
        self._propertyAccessor.setEnumValue("TimeUnit", value.value, resetProperties)
        
    def getTimeUnits(self) -> TimeUnitsType:
        return self._propertyAccessor.getEnumValue("TimeUnit", TimeUnitsType)
    
    def setPermeabilityUnits(self, value : PermeabilityUnitsType, resetProperties : bool = True):
        """
        Sets the permeability unit for the current project.

        By default, if the unit is changed, script will reset all unit-dependent
        property values in the project to their default values. This will reset the 
        Field Stress settings, and ALL properties for Material, Bolts, Liners, and Joints.
        To preserve existing values when changing the unit, set `resetProperties` to False.

        It is recommended to set the desired unit at the beginning of the script or project
        to avoid unintended resets.

        Parameters:
            value (PermeabilityUnitsType): The unit system to apply.
            resetProperties (bool, optional): Whether to reset unit-dependent property values to
                their defaults. Defaults to True.
        """
        self._propertyAccessor.setEnumValue("Permeability_Units", value.value, resetProperties)
    
    def getPermeabilityUnits(self) -> PermeabilityUnitsType:
        return self._propertyAccessor.getEnumValue("Permeability_Units", PermeabilityUnitsType)
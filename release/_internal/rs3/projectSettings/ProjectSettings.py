import rs3.generatedFiles.ProjectSettingsDataService_pb2_grpc as ProjectSettingsDataService_pb2_grpc
import rs3.generatedFiles.ProjectSettingsDataService_pb2 as ProjectSettingsDataService_pb2
from rs3._client import Client
from rs3.projectSettings.ProjectSettingEnums import *
from rs3.projectSettings.Units import Units
from rs3.projectSettings.Stages import Stages
from rs3.projectSettings.StressAnalysis import StressAnalysis
from rs3.projectSettings.SolverOptions import SolverOptions
from rs3.projectSettings.Groundwater import Groundwater
from rs3.projectSettings.ShearStrengthReduction import ShearStrengthReduction
from rs3.projectSettings.Dynamic import Dynamic
from rs3.properties._PropertyAccessor import PropertyAccessor
from rs3._proxyObject import _ProxyObject

class ProjectSettings(_ProxyObject):
    """
    Set up the project parameters.
    
    Attributes:
        Units (Units): Reference object for modifying property.
        Stages (Stages): Reference object for modifying property.
        StressAnalysis (StressAnalysis): Reference object for modifying property.
        SolverOptions (SolverOptions): Reference object for modifying property.
        Groundwater (Groundwater): Reference object for modifying property.
        ShearStrengthReduction (ShearStrengthReduction): Reference object for modifying property.
        Dynamic (Dynamic): Reference object for modifying property.
    
    Examples:
		See :ref:`project_settings_example`.
  
    """
    def __init__(self, client : Client, id : str):
        super().__init__(client, id)
        self._projectSettingsDataService = ProjectSettingsDataService_pb2_grpc.ProjectSettingsDataServiceStub(self._client.channel)
        self._propertyAccessor = PropertyAccessor(client, id, self._projectSettingsDataService)
        self.projectId = id
        self.Units = Units(client, id)
        self.Stages = Stages(client, id)
        self.StressAnalysis = StressAnalysis(client, id)
        self.SolverOptions = SolverOptions(client, id)
        self.Groundwater = Groundwater(client, id)
        self.ShearStrengthReduction = ShearStrengthReduction(client, id)
        self.Dynamic = Dynamic(client, id)
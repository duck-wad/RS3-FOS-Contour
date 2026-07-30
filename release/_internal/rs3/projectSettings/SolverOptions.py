from rs3.projectSettings.ProjectSettingEnums import *
from rs3._client import Client
from ._PropertyAccessor import StressAnalysisPropertyAccessor
from rs3._proxyObject import _ProxyObject


class SolverOptions(_ProxyObject):
    """
    Set the solid and fluid interaction type and solver type.
    
    Examples:
        See :ref:`project_settings_example`.
        
    """
    def __init__(self, client: Client, projectId: str):
        super().__init__(client, projectId)
        self._propertyAccessor = StressAnalysisPropertyAccessor(client, projectId)

    def getAnalysisType(self) -> AnalysisType:
        """
        Get the interaction between fluid pore pressure and solid stresses and deformation.
        """
        return self._propertyAccessor.getEnumValue("Method", AnalysisType)

    def setAnalysisType(self, value: AnalysisType):
        """
        Set the interaction between fluid pore pressure and solid stresses and deformation.
        """
        self._propertyAccessor.setEnumValue("Method", value.value)

    def getSolverType(self) -> SolverType:
        """
        Get the currently configured solver type for solving the matrix representing the
        system of equations defined by your model.

        Returns:
            SolverType: The solver type currently set for this model.

        Notes:
            - DIRECT_CPU: Direct solver running on CPU.
            - ITERATIVE_CPU: Iterative CPU solver (PCG with ICT preconditioner).
            - FGMRES_AMG_PRECONDITIONER_CPU: FGMRES solver on CPU with AMG preconditioner.
            - FGMRESG_ILU_PRECONDITIONER_CPU: FGMRES(G) solver on CPU with ILU preconditioner.
            - DIRECT_GPU: Direct solver running on GPU.
            - FGMRES_AMG_GPU: FGMRES solver on GPU with AMG preconditioner.
            - AUTO: Automatically select the solver based on the problem configuration.

        """
        return self._propertyAccessor.getEnumValue("Solver", SolverType)

    def setSolverType(self, value: SolverType):
        """
        Set the currently configured solver type for solving the matrix representing the
        system of equations defined by your model.

        Args:
            value (SolverType): The solver type to configure.

        Notes:
            - ITERATIVE_CPU corresponds to a CPU-based PCG solver with an ICT preconditioner.
            - GPU-based solvers require compatible GPU hardware.
            - AUTO allows the system to determine the most appropriate solver.

        """
        self._propertyAccessor.setEnumValue("Solver", value.value)

    def getMemoryFillLevel(self) -> float:
        return self._propertyAccessor.getDoubleProperty("SolverFillLevel")

    def setMemoryFillLevel(self, value: float):
        self._propertyAccessor.setDoubleProperty("SolverFillLevel", value)

    def getRelativeTolerance(self) -> float:
        return self._propertyAccessor.getDoubleProperty("Tolerance")

    def setRelativeTolerance(self, value: float):
        self._propertyAccessor.setDoubleProperty("Tolerance", value)

    def getProperties(self):
        return {
            "AnalysisMethod": self.getAnalysisType(),
            "Solver": self.getSolverType(),
        }
    def setProperties(self, AnalysisMethod: AnalysisType = None, Solver: SolverType = None):
        if AnalysisMethod is not None:
            self.setAnalysisType(AnalysisMethod)
        if Solver is not None:
            self.setSolverType(Solver)

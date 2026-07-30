from rs3._client import Client
import rs3.generatedFiles.ComputeService_pb2 as ComputeService
import rs3.generatedFiles.ComputeService_pb2_grpc as ComputeServiceGrpc
from rs3._proxyObject import _ProxyObject
from rs3.ModelEnums import *

class StageSRFValueConvergenceStatus:
    def __init__(self, isRecovery: bool, stagesConvergence: list[ComputeService.convergenceStatus], srfValuesConvergence: list[ComputeService.convergenceStatus]):
        self._isRecovery = isRecovery
        # Convert IndexConvergenceStatusPair objects to tuples
        self._stagesConvergence = [(pair.index, pair.converged) for pair in stagesConvergence]
        self._srfValuesConvergence = [(pair.index, pair.converged) for pair in srfValuesConvergence]

    @property
    def IsRecovery(self):
        return self._isRecovery
    
    @property
    def StagesConvergence(self):
        return self._stagesConvergence
    
    @property
    def SrfValuesConvergence(self):
        return self._srfValuesConvergence

    @property
    def Printable(self):
        return self._srfValuesConvergencePrintable() or self._stagesConvergencePrintable()

    def _stagesConvergencePrintable(self):
        return len(self._stagesConvergence) > 0

    def _printStagesConvergence(self):
        if not self._stagesConvergencePrintable():
            return
        print("Stages Convergence:")
        print(f"{'Stage':<8} {'Status':<8}")
        print("-" * 16)
        for stage, converged in self._stagesConvergence:
            status = "Yes" if converged else "No"
            print(f"{stage:<8} {status:<8}")

    def _srfValuesConvergencePrintable(self):
        return len(self._srfValuesConvergence) > 0

    def _printSrfValuesConvergence(self):
        if not self._srfValuesConvergencePrintable():
            return
        print("SRF Values Convergence:")
        print(f"{'SRF Value':<8} {'Status':<8}")
        print("-" * 16)
        for srfValue, converged in self._srfValuesConvergence:
            status = "Yes" if converged else "No"
            print(f"{srfValue:<8} {status:<8}")

    def Print(self):
        if not self.Printable:
            return
        print(f"Recovery: {self._isRecovery}")
        self._printStagesConvergence()
        self._printSrfValuesConvergence()

class Compute(_ProxyObject):
    """
    Example:
        See :ref:`compute_example`.
    """
    def __init__(self, client: Client, projectId: str):
        super().__init__(client, projectId)
        self._computeService = ComputeServiceGrpc.ComputeServiceStub(self._client.channel)

    def compute(self, computeType : ComputeType = ComputeType.ALL, computeStart : ComputeStart = ComputeStart.AFTER_LAST_COMPUTED_STAGE) -> tuple[bool, str]:
        """
        Compute stress results (automatically compute groundwater too, if required). Mesh is required before compute.
        """
        request = ComputeService.computeRequest(_projectId=self._objectId, computeType=computeType.value, computeStart=computeStart.value)
        response = self._client.callFunction(self._computeService.compute, request)
        success = response.result == ""
        if success:
            self.printConvergenceStatus()
     
        return success, response.result
    
    def computeGroundWater(self) -> tuple[bool, str]:
        """
        Compute groundwater only (stress analysis will not be computed). Mesh is required before compute.
        """
        return self.compute(computeType=ComputeType.GROUNDWATER_ONLY, computeStart=ComputeStart.AFTER_LAST_COMPUTED_STAGE)    

    def printConvergenceStatus(self):
        success, errorMessage, convergenceStatus = self.readConvergenceStatus()
        if success and convergenceStatus.Printable:
            convergenceStatus.Print()
        elif not success:
            print(f"Error: {errorMessage}")

    def readConvergenceStatus(self) -> tuple[bool, str, StageSRFValueConvergenceStatus]:
        """
        This function returns the availability of convergence status, error message if there is any, and convergence status. To check
        the convergence of each stage, users may check StagesConvergence and SrfValuesConvergence of StageSRFValueConvergenceStatus.
        """
        request = ComputeService.readStagesSSRConvergenceStatusRequest(_projectId=self._objectId)
        response = self._client.callFunction(self._computeService.readStagesSRFValuesConvergence, request)
        convergenceStatus = StageSRFValueConvergenceStatus(response.isRecovery, response.stagesConvergence, response.srfValuesConvergence)
        return response.success, response.errorMessage, convergenceStatus
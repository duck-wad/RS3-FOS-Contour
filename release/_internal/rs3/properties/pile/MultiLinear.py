from rs3._client import Client
from ._PropertyAccessor import PropertyAccessor
import rs3.generatedFiles.PileDataService_pb2 as PileDataService_pb2
import rs3.generatedFiles.PileDataService_pb2_grpc as PileDataService_pb2_grpc
from rs3.properties.stageFactors.StageFactorInterfaces import AbsoluteStageFactorInterface
from rs3.properties.pile.PileCommon import PileCommon, PileCommonStageFactor, PileCommonDefinedStageFactor
class MultiLinearStageFactor(PileCommonStageFactor):
    """
	Examples:
		See :ref:`pile_example`.
	"""
    def __init__(self, id : str, stageFactorID : str, client : Client):
        super().__init__(id, stageFactorID, client)
    def getMultiLinearFactor(self) -> float:
        return self._stageFactorPropertyAccessor.getDoubleProperty("MultiLinear_MultiLinear")
class MultiLinearDefinedStageFactor(PileCommonDefinedStageFactor, MultiLinearStageFactor):
    """
	Examples:
		See :ref:`pile_example`.
	"""
    def setMultiLinearFactor(self, value: float):
        self._stageFactorPropertyAccessor.setDoubleProperty("MultiLinear_MultiLinear", value)        
class MultiLinear(PileCommon):
    """
	Examples:
		See :ref:`pile_example`.
	"""
    def __init__(self, client: Client, id: str):
        super().__init__(client, id)
        self._pileDataService = PileDataService_pb2_grpc.PileDataServiceStub(self._client.channel)
        self._propertyAccessor = PropertyAccessor(client, id)
        self.StageFactorInterface = AbsoluteStageFactorInterface[MultiLinearDefinedStageFactor, MultiLinearStageFactor](id, client, MultiLinearDefinedStageFactor, MultiLinearStageFactor)
    def getMultiLinearGrid(self) -> list[tuple[float, float]]:
        """
        Get a list of multi-linear skin resistance (distance to top, max traction) data points.
        
        Returns:
            list[tuple[float, float]]
            A list of (distance_to_top, max_traction) data points.

            - distance_to_top : float
                Distance measured from the top of the pile.
            - max_traction : float
                Maximum skin resistance (traction) at the corresponding distance.

        """
        request = PileDataService_pb2.GetMultiLinearGridRequest(pileId=self._objectId)
        response : PileDataService_pb2.GetMultiLinearGridResponse = self._client.callFunction(self._pileDataService.GetMultiLinearGrid, request)
        return [(dtv.distances, dtv.tractions) for dtv in response.distanceTractionValues]
    def setMultiLinearGrid(self, value: list[tuple[float, float]]):
        """
        Set a list of multi-linear skin resistance (distance to top, max traction) data points.

        Parameters:
            value : list[tuple[float, float]]
                A list of (distance_to_top, max_traction) data points.

                - distance_to_top : float
                    Distance measured from the top of the pile.
                - max_traction : float
                    Maximum skin resistance (traction) at that distance.

        Example:
            >>> list = [(1.1, 2.2), (3.3, 4.4), (5.5, 6.6)]
            >>> MultiLinearPile.setMultiLinearGrid(list)
            
        """
        request = PileDataService_pb2.SetMultiLinearGridRequest(pileId=self._objectId, 
                                                                       distanceTractionValues=[PileDataService_pb2.DistanceTractionValues(distances=d, tractions=t)for d, t in value])
        self._client.callFunction(self._pileDataService.SetMultiLinearGrid, request)

from rs3._client import Client
from rs3.properties.stageFactors._StageFactorPropertyAccessor import StageFactorPropertyAccessor
from rs3._proxyObject import _ProxyObject

class IStageFactorBase(_ProxyObject) :
    def __init__(self, parentID : str, stageFactorID : str, client : Client, stub):
        super().__init__(client, stageFactorID)
        self.parentID = parentID
        self._stub = stub
        self._stageFactorPropertyAccessor = StageFactorPropertyAccessor(parentID, stageFactorID, client, stub)
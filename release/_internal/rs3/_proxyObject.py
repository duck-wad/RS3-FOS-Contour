from rs3._client import Client
class _ProxyObject():
    def __init__(self, client: Client, objectId: str):
        self._client = client
        self._objectId = objectId
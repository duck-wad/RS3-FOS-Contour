from rs3._client import Client
from rs3.properties.PropertyEnums import *
from rs3.properties.material.constitutiveModel.CamClay import CamClay

class ModifiedCamClay(CamClay):
    """
    See CamClay.py for parameters
    Modified Cam Clay model shares the same set of parameters as Cam Clay
    """
    def __init__(self, client : Client, materialID : str):
        super().__init__(client, materialID)

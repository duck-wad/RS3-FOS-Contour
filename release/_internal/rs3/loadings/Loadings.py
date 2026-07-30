from rs3._client import Client
from rs3.projectSettings.ProjectSettingEnums import *
from rs3.loadings.fieldStress.FieldStress import FieldStress
from rs3._proxyObject import _ProxyObject

class Loadings(_ProxyObject):
    """
    Modify load related properties.
    
    Attributes:
        FieldStress (FieldStress): Reference object for modifying property.
    """
    def __init__(self, client : Client, id : str):
        super().__init__(client, id)
        self.FieldStress = FieldStress(client, id)
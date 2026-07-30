import rs3.generatedFiles.LinerDataService_pb2_grpc as LinerDataService_pb2_grpc
import rs3.generatedFiles.CommonMessages_pb2 as CommonMessages_pb2
from rs3._client import Client
from rs3.properties.PropertyEnums import *
from rs3.properties.liner.Standard import Standard
from rs3.properties.liner.Geosynthetic import Geosynthetic
from rs3.properties.liner.ReinforcedConcrete import ReinforcedConcrete
from rs3.properties._PropertyAccessor import PropertyAccessor
from rs3._proxyObject import _ProxyObject
from rs3.ColorPicker import ColorPicker

class LinerProperty(_ProxyObject):
    """
    Define liner properties.

    Attributes:
        Standard (Standard): Reference object for modifying property.
        Geosynthetic (Geosynthetic): Reference object for modifying property.
        ReinforcedConcrete (ReinforcedConcrete): Reference object for modifying property.

    Examples:
        See :ref:`liner_example`.
        
    """
    def __init__(self, client : Client, linerID : str):
        super().__init__(client, linerID)
        self._linerDataService = LinerDataService_pb2_grpc.LinerDataServiceStub(self._client.channel)
        self._propertyAccessor = PropertyAccessor(client, linerID, self._linerDataService)
        self.Standard = Standard(client, linerID)
        self.Geosynthetic = Geosynthetic(client, linerID)
        self.ReinforcedConcrete = ReinforcedConcrete(client, linerID)

    def getLinerName(self) -> str:
        return self._propertyAccessor.getStringValue("Name")
    def setLinerName(self, name):
        self._propertyAccessor.setStringValue("Name", name)
    def getLinerType(self) -> LinerTypes:
        return self._propertyAccessor.getEnumValue("LayerType", LinerTypes)
    def setLinerType(self, linerType : LinerTypes):
        self._propertyAccessor.setEnumValue("LayerType", linerType.value)
    def setLinerColor(self, *args):
        """
        Sets the RGBA color for the object.

        Raises:
            ValueError: If inputs are invalid or out of range.
            
        Notes:
            Accepted formats:
                - setColor(red, green, blue)
                - setColor(red, green, blue, alpha)
                - setColor("#RRGGBB")
                - setColor("#RRGGBBAA")
                - setColor(ColorType.Rose)
                - setColor(0xE1E4FF)  # Integer COLORREF

        """
        color_bytes = ColorPicker._setColorValidation(*args)
        request = CommonMessages_pb2.SetColorRequest(objectId=self._objectId, value=color_bytes)
        self._client.callFunction(self._linerDataService.SetColorProperty, request)
    def getLinerColor(self) -> tuple[int, int, int, int]:
        """
        Retrieves the RGBA color of the object.

        Returns:
            tuple[int, int, int, int]: A tuple of four integers representing the red, green, blue, and alpha components of the object's color, each in the range [0, 255].
        """
        request = CommonMessages_pb2.GetColorRequest(objectId=self._objectId)
        response : CommonMessages_pb2.GetColorResponse = self._client.callFunction(self._linerDataService.GetColorProperty, request)
        red, green, blue, alpha = response.value
        return red, green, blue, alpha
    def getApplyStageFactors(self) -> bool:
        """
        UI Label:
            Stage Liner Properties
        """
        return self._propertyAccessor.getBoolValue("IsStagePropOn")
    def setApplyStageFactors(self, value: bool):
        """
        UI Label:
            Stage Liner Properties
        """
        self._propertyAccessor.setBoolValue("IsStagePropOn", value)

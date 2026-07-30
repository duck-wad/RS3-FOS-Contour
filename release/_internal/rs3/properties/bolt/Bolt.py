import rs3.generatedFiles.BoltDataService_pb2_grpc as BoltDataService_pb2_grpc
import rs3.generatedFiles.CommonMessages_pb2 as CommonMessages_pb2
from rs3._client import Client
from rs3.properties.PropertyEnums import *
from rs3.properties.bolt.EndAnchored import EndAnchored
from rs3.properties.bolt.FullyBonded import FullyBonded
from rs3.properties.bolt.PlainStrandCable import PlainStrandCable
from rs3.properties.bolt.Swellex import Swellex
from rs3.properties.bolt.Tieback import Tieback
from rs3.properties._PropertyAccessor import PropertyAccessor
from rs3._proxyObject import _ProxyObject
from rs3.ColorPicker import ColorPicker

class BoltProperty(_ProxyObject):
    """
    Define bolt properties.

    Attributes:
        EndAnchored (EndAnchored): Reference object for modifying property.
        FullyBonded (FullyBonded): Reference object for modifying property.
        PlainStrandCable (PlainStrandCable): Reference object for modifying property.
        Swellex (Swellex): Reference object for modifying property.
        Tieback (Tieback): Reference object for modifying property.

    Examples:
        See :ref:`bolt_example`.
        
    """
    def __init__(self, client : Client, boltID : str):
        super().__init__(client, boltID)
        self._boltDataService = BoltDataService_pb2_grpc.BoltDataServiceStub(self._client.channel)
        self._propertyAccessor = PropertyAccessor(client, boltID, self._boltDataService)
        self.EndAnchored = EndAnchored(client, boltID)
        self.FullyBonded = FullyBonded(client, boltID)
        self.PlainStrandCable = PlainStrandCable(client, boltID)
        self.Swellex = Swellex(client, boltID)
        self.Tieback = Tieback(client, boltID)

    def getBoltName(self) -> str:
        return self._propertyAccessor.getStringValue("Name")

    def setBoltName(self, name):
        self._propertyAccessor.setStringValue("Name", name)

    def getBoltType(self) -> BoltTypes:
        return self._propertyAccessor.getEnumValue("BoltType", BoltTypes)

    def setBoltType(self, boltType : BoltTypes):
        self._propertyAccessor.setEnumValue("BoltType", boltType.value)

    def setBoltColor(self, *args):
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
        self._client.callFunction(self._boltDataService.SetColorProperty, request)
    def getBoltColor(self) -> tuple[int, int, int, int]:
        """
        Retrieves the RGBA color of the object.

        Returns:
            tuple[int, int, int, int]: A tuple of four integers representing the red, green, blue, and alpha components of the object's color, each in the range [0, 255].
        """
        request = CommonMessages_pb2.GetColorRequest(objectId=self._objectId)
        response : CommonMessages_pb2.GetColorResponse = self._client.callFunction(self._boltDataService.GetColorProperty, request)
        red, green, blue, alpha = response.value
        return red, green, blue, alpha

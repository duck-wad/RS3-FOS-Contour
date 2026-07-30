import rs3.generatedFiles.WaterByLocationDataService_pb2_grpc as WaterByLocationDataService_pb2_grpc
import rs3.generatedFiles.WaterByLocationDataService_pb2 as WaterByLocationDataService_pb2
import rs3.generatedFiles.CommonMessages_pb2 as CommonMessages_pb2
from rs3._client import Client
from rs3.properties.PropertyEnums import *
from ._PropertyAccessor import WaterByLocationPropertyAccessor
from rs3._proxyObject import _ProxyObject
from rs3.ColorPicker import ColorPicker

class WaterByLocationProperty(_ProxyObject):
    """
    Edit water surface defined by locations.

    Examples:
        See :ref:`water_by_location_example`.
        
    """
    def __init__(self, client : Client, waterSurfaceID : str, projectID: str):
        super().__init__(client, waterSurfaceID)
        self._waterByLocationDataService = WaterByLocationDataService_pb2_grpc.WaterByLocationDataServiceStub(self._client.channel)
        self._propertyAccessor = WaterByLocationPropertyAccessor(client, waterSurfaceID, self._waterByLocationDataService, projectID)
        self.projectID = projectID

    def setName(self, name):
        self._propertyAccessor.setStringValue("Name", name)
    def getName(self) -> str:
        return self._propertyAccessor.getStringValue("Name")
    def setColor(self, *args):
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
        request = WaterByLocationDataService_pb2.SetProjectColorRequest(objectId=self._objectId, value=color_bytes, projectId=self.projectID)
        self._client.callFunction(self._waterByLocationDataService.SetColorProperty, request)
    def getColor(self) -> tuple[int, int, int, int]:
        """
        Retrieves the RGBA color of the object.

        Returns:
            tuple[int, int, int, int]: A tuple of four integers representing the red, green, blue, and alpha components of the object's color, each in the range [0, 255].
        """
        request = WaterByLocationDataService_pb2.GetProjectColorRequest(objectId=self._objectId, projectId=self.projectID)
        response : WaterByLocationDataService_pb2.GetProjectColorResponse = self._client.callFunction(self._waterByLocationDataService.GetColorProperty, request)
        red, green, blue, alpha = response.value
        return red, green, blue, alpha
    def setInterpolationMethod(self, interpolationMethod : GroundwaterInterpolationMethodType):
        self._propertyAccessor.setEnumValue("interpolation_method", interpolationMethod.value)
    def getInterpolationMethod(self) -> GroundwaterInterpolationMethodType:
        return self._propertyAccessor.getEnumValue("interpolation_method", GroundwaterInterpolationMethodType)
    def setResolutionMethod(self, resolutionMethod : GroundwaterResolutionMethodType):
        self._propertyAccessor.setEnumValue("resolution_method", resolutionMethod.value)
    def getResolutionMethod(self) -> GroundwaterResolutionMethodType:
        return self._propertyAccessor.getEnumValue("resolution_method", GroundwaterResolutionMethodType)
    def setIsExtrapolate(self, value: bool):
        self._propertyAccessor.setBoolValue("is_extrapolate_on", value)
    def getIsExtrapolate(self) -> bool:
        return self._propertyAccessor.getBoolValue("is_extrapolate_on")
    def setWaterSurfaceLocation(self, value: list[tuple[float, float, float]]):
        """Each water surface is defined by at least 3 points to form a surface"""
        point3Dlist = []
        for x, y, z in value:
            point3D = CommonMessages_pb2.Point3D(x=x, y=y, z=z)
            point3Dlist.append(point3D)
        request = WaterByLocationDataService_pb2.SetWaterByLocationsRequest(waterSurfaceId=self._objectId, waterSurfaceLocation=point3Dlist, projectId=self.projectID)
        self._client.callFunction(self._waterByLocationDataService.SetWaterByLocations, request)
    def getWaterSurfaceLocation(self) -> list[tuple[float, float, float]]:
        """Each water surface is defined by at least 3 points to form a surface"""
        request = WaterByLocationDataService_pb2.GetWaterByLocationsRequest(waterSurfaceId=self._objectId, projectId=self.projectID)
        response : WaterByLocationDataService_pb2.GetWaterByLocationsResponse = self._client.callFunction(self._waterByLocationDataService.GetWaterByLocations, request)
        return list((p.x, p.y, p.z) for p in response.waterSurfaceLocation)

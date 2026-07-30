import rs3.generatedFiles.WaterPressureGridDataService_pb2_grpc as WaterPressureGridDataService_pb2_grpc
import rs3.generatedFiles.WaterPressureGridDataService_pb2 as WaterPressureGridDataService_pb2
import rs3.generatedFiles.CommonMessages_pb2 as CommonMessages_pb2
from rs3._client import Client
from rs3.properties.PropertyEnums import *
from ._PropertyAccessor import WaterGridPropertyAccessor
from rs3._proxyObject import _ProxyObject
from rs3.ColorPicker import ColorPicker

class WaterGridProperty(_ProxyObject):
    """
    Edit a pore water pressure defined by locations.

    Examples:
        See :ref:`water_grid_example`.
        
    """
    def __init__(self, client : Client, waterSurfaceID : str, projectID: str):
        super().__init__(client, waterSurfaceID)
        self._waterGridDataService = WaterPressureGridDataService_pb2_grpc.WaterPressureGridDataServiceStub(self._client.channel)
        self._propertyAccessor = WaterGridPropertyAccessor(client, waterSurfaceID, self._waterGridDataService, projectID)
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
        request = WaterPressureGridDataService_pb2.SetProjectColorRequest(objectId=self._objectId, value=color_bytes, projectId=self.projectID)
        self._client.callFunction(self._waterGridDataService.SetColorProperty, request)
    def getColor(self) -> tuple[int, int, int, int]:
        """
        Retrieves the RGBA color of the object.

        Returns:
            tuple[int, int, int, int]: A tuple of four integers representing the red, green, blue, and alpha components of the object's color, each in the range [0, 255].
        """
        request = WaterPressureGridDataService_pb2.GetProjectColorRequest(objectId=self._objectId, projectId=self.projectID)
        response : WaterPressureGridDataService_pb2.GetProjectColorResponse = self._client.callFunction(self._waterGridDataService.GetColorProperty, request)
        red, green, blue, alpha = response.value
        return red, green, blue, alpha
    def setIs3D(self, value: bool):
        self._propertyAccessor.setBoolValue("Is3D", value)
    def getIs3D(self) -> bool:
        return self._propertyAccessor.getBoolValue("Is3D")
    def set2DPlaneType(self, plane2DType : WaterGridPlane2DType):
        self._propertyAccessor.setEnumValue("Plane2D_type", plane2DType.value)
    def get2DPlaneType(self) -> WaterGridPlane2DType:
        return self._propertyAccessor.getEnumValue("Plane2D_type", WaterGridPlane2DType)
    def setInterpolationMethod(self, interpolationMethod : WaterGridInterpolationMethodType):
        self._propertyAccessor.setEnumValue("InterpolationMethod", interpolationMethod.value)
    def getInterpolationMethod(self) -> WaterGridInterpolationMethodType:
        return self._propertyAccessor.getEnumValue("InterpolationMethod", WaterGridInterpolationMethodType)
    def setWaterGridPointSetType(self, type : WaterGridPointSetType):
        self._propertyAccessor.setEnumValue("Type", type.value)
    def getWaterGridPointSetType(self) -> WaterGridPointSetType:
        return self._propertyAccessor.getEnumValue("Type", WaterGridPointSetType)
    def setWaterGridPoints(self, value: list[tuple[float, float, float, float]]):
        """
        Set water grid point values.

        Parameters
        ----------
        value : list[tuple[float, float, float, float]]
            A list of water grid points defined as (x, y, z, value).

            Important:
            - The coordinates must always be provided as 3D (x, y, z),
            regardless of whether the water grid is defined as 2D or 3D.
            - For 2D grids, the unused coordinate must still be supplied
            (typically set to 0.0).

            The meaning of `value` depends on the water grid point set type:
            - Pore pressure
            - Pressure head
            - Total head

            The interpretation is determined by the configured water grid type.
        """
        waterGridlist = []
        for x, y, z, value in value:
            waterGridPoint = WaterPressureGridDataService_pb2.WaterGridSet(x=x, y=y, z=z, commonValue=value)
            waterGridlist.append(waterGridPoint)
        request = WaterPressureGridDataService_pb2.SetPWPPointSetRequest(waterGridId=self._objectId, PWPPointSet=waterGridlist, projectId=self.projectID)
        self._client.callFunction(self._waterGridDataService.SetPWPPointSet, request)
    def getWaterGridPoints(self) -> list[tuple[float, float, float, float]]:
        """
        Retrieve water grid point values.

        Returns
        -------
        list[tuple[float, float, float, float]]
            A list of water grid points in the format (x, y, z, value).

            Important:
            - Coordinates are always returned in 3D format.
            - The returned `value` represents pore pressure, pressure head,
            or total head, depending on the water grid point set type.

        """
        request = WaterPressureGridDataService_pb2.GetPWPPointSetRequest(waterGridId=self._objectId, projectId=self.projectID)
        response : WaterPressureGridDataService_pb2.GetPWPPointSetResponse = self._client.callFunction(self._waterGridDataService.GetPWPPointSet, request)
        return list((p.x, p.y, p.z, p.commonValue) for p in response.PWPPointSet)

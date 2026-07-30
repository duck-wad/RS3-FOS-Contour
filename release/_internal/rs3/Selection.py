import rs3.generatedFiles.SelectionService_pb2_grpc as SelectionServiceGrpc
import rs3.generatedFiles.SelectionService_pb2 as SelectionService
from rs3._client import Client
from rs3.ExternalVolume import ExternalVolume
from rs3.Geometry import *
from typing import Union

class Selection:
    def __init__(self, client: Client, projectId: str):
        self._client = client
        self._projectId = projectId
        self._SelectionService = SelectionServiceGrpc.SelectionServiceStub(self._client.channel)

    def _getExternalVolumesByPoint(self, point: Point) -> list[str]:
        _projectId_ = self._projectId
        geometry_ = point.toCommonGeometryObject()
        request = SelectionService._getExternalVolumesByGeometryRequest(_projectId=_projectId_, geometry=geometry_, includeIntersecting=False)
        result_ = self._client.callFunction(self._SelectionService._getExternalVolumesByPoint, request)
        result = [obj for obj in result_.result]
        return result

    def _getExternalVolumesByPolyline(self, polyline: Polyline) -> list[str]:
        _projectId_ = self._projectId
        geometry_ = polyline.toCommonGeometryObject()
        request = SelectionService._getExternalVolumesByGeometryRequest(_projectId=_projectId_, geometry=geometry_, includeIntersecting=False)
        result_ = self._client.callFunction(self._SelectionService._getExternalVolumesByPolyline, request)
        result = [obj for obj in result_.result]
        return result

    def _getExternalVolumesByBoundingVolume(self, volume: Union[Cube, Cylinder, Sphere], includeIntersecting: bool) -> list[str]:
        _projectId_ = self._projectId
        includeIntersecting_ = includeIntersecting
        geometry_ = volume.toCommonGeometryObject()
        request = SelectionService._getExternalVolumesByGeometryRequest(_projectId=_projectId_, geometry=geometry_, includeIntersecting=includeIntersecting_)
        result_ = self._client.callFunction(self._SelectionService._getExternalVolumesByBoundingVolume, request)
        result = [obj for obj in result_.result]
        return result

    def getExternalVolumes(self, sampleRegion : Geometry, includeIntersecting : bool = True) -> list[ExternalVolume]:
        """
        Retrieve external volumes that intersect with or are contained within a specified geometric region.

        This method performs spatial queries to find external volumes based on different geometric
        sample regions. The function supports various geometric shapes and can optionally include
        or exclude volumes that only partially intersect with the sample region.

        Args:
            sampleRegion (Geometry): The geometric region to use for volume selection. Supported types:
                - Point: Selects volumes containing the specified point
                - Polyline: Selects volumes intersecting with the polyline path
                - Cube: Selects volumes within or intersecting the bounding box defined by two corner points
                - Cylinder: Selects volumes within or intersecting the cylindrical region
                - Sphere: Selects volumes within or intersecting the spherical region
            includeIntersecting (bool, optional): Whether to include volumes that only partially
                intersect with the sample region. Defaults to True.
                - True: Returns volumes that are fully contained within OR partially intersect the region
                - False: Returns only volumes that are fully contained within the region

                Note: This parameter only applies to Cube, Cylinder, and Sphere geometry types.
                For Point and Polyline, this parameter is ignored as the selection behavior
                is inherently based on intersection/containment.

        Returns:
            list[ExternalVolume]: A list of ExternalVolume objects that match the selection criteria.
            Returns an empty list if no volumes are found.

        Raises:
            TypeError: If sampleRegion is not one of the supported Geometry types.

        Examples:
            See :ref:`external_volume_and_selection_example`.

        >>> # Select volumes containing a specific point
        >>> point = Point(20.0, 0.0, -50.0)
        >>> volumes = selection.getExternalVolumes(point)

        >>> # Select volumes intersecting with a polyline
        >>> polyline = Polyline([Point(5.5, -40, -50), Point(25, 5.2, -48), Point(20.5, 50.2, -45)])
        >>> volumes = selection.getExternalVolumes(polyline)

        >>> # Select volumes within a bounding box (including intersecting)
        >>> cube = Cube(Point(18.0, 1.5, -49.2), Point(23.5, 2.5, -47.3))
        >>> volumes = selection.getExternalVolumes(cube, includeIntersecting=True)

        >>> # Select only volumes fully contained within a bounding box
        >>> volumes = selection.getExternalVolumes(cube, includeIntersecting=False)

        >>> # Select volumes within a cylindrical region
        >>> cylinder = Cylinder(Point(22.12, 45.3, -52.2), Point(25.2, 30.3, -48.4), radius=1.0)
        >>> volumes = selection.getExternalVolumes(cylinder)

        >>> # Select volumes within a spherical region
        >>> sphere = Sphere(Point(18.94, 47.05, -53.83), radius=5.0)
        >>> volumes = selection.getExternalVolumes(sphere)
        """
        if isinstance(sampleRegion, Point):
            externalVolumes = self._getExternalVolumesByPoint(point=sampleRegion)
        elif isinstance(sampleRegion, Polyline):
            externalVolumes = self._getExternalVolumesByPolyline(polyline=sampleRegion)
        elif isinstance(sampleRegion, Cube) or isinstance(sampleRegion, Cylinder) or isinstance(sampleRegion, Sphere):
            externalVolumes = self._getExternalVolumesByBoundingVolume(volume=sampleRegion, includeIntersecting=includeIntersecting)
        else:
            raise TypeError(f"Unsupported SampleRegion type: {type(sampleRegion)}")

        return [ExternalVolume(self._client, obj) for obj in externalVolumes]

    def getAttachedExternalVolumes(self, externalVolume : ExternalVolume) -> list[ExternalVolume]:
        """
        Examples:
            See :ref:`external_volume_and_selection_example`.
        """
        request = SelectionService.getAttachedExternalVolumesRequest(_projectId=self._projectId, _externalVolumeID=externalVolume._objectId)
        result_ = self._client.callFunction(self._SelectionService.getAttachedExternalVolumes, request)
        return [ExternalVolume(self._client, obj) for obj in result_.result]

    def getAttachedExternalVolumesByVolumeName(self, externalVolumeName : str) -> list[ExternalVolume]:
        """
        Examples:
            See :ref:`external_volume_and_selection_example`.
        """
        request = SelectionService.getAttachedExternalVolumesByVolumeNameRequest(_projectId=self._projectId, externalVolumeName=externalVolumeName)
        result_ = self._client.callFunction(self._SelectionService.getAttachedExternalVolumesByVolumeName, request)
        return [ExternalVolume(self._client, obj) for obj in result_.result]
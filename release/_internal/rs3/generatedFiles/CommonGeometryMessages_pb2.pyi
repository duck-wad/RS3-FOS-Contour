from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Point(_message.Message):
    __slots__ = ("x", "y", "z")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

class Polyline(_message.Message):
    __slots__ = ("point",)
    POINT_FIELD_NUMBER: _ClassVar[int]
    point: _containers.RepeatedCompositeFieldContainer[Point]
    def __init__(self, point: _Optional[_Iterable[_Union[Point, _Mapping]]] = ...) -> None: ...

class Sphere(_message.Message):
    __slots__ = ("center", "radius")
    CENTER_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    center: Point
    radius: float
    def __init__(self, center: _Optional[_Union[Point, _Mapping]] = ..., radius: _Optional[float] = ...) -> None: ...

class Box(_message.Message):
    __slots__ = ("corner1", "corner2", "rotationAboutX", "rotationAboutY", "rotationAboutZ")
    CORNER1_FIELD_NUMBER: _ClassVar[int]
    CORNER2_FIELD_NUMBER: _ClassVar[int]
    ROTATIONABOUTX_FIELD_NUMBER: _ClassVar[int]
    ROTATIONABOUTY_FIELD_NUMBER: _ClassVar[int]
    ROTATIONABOUTZ_FIELD_NUMBER: _ClassVar[int]
    corner1: Point
    corner2: Point
    rotationAboutX: float
    rotationAboutY: float
    rotationAboutZ: float
    def __init__(self, corner1: _Optional[_Union[Point, _Mapping]] = ..., corner2: _Optional[_Union[Point, _Mapping]] = ..., rotationAboutX: _Optional[float] = ..., rotationAboutY: _Optional[float] = ..., rotationAboutZ: _Optional[float] = ...) -> None: ...

class Cylinder(_message.Message):
    __slots__ = ("axisStartPoint", "axisEndPoint", "radius")
    AXISSTARTPOINT_FIELD_NUMBER: _ClassVar[int]
    AXISENDPOINT_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    axisStartPoint: Point
    axisEndPoint: Point
    radius: float
    def __init__(self, axisStartPoint: _Optional[_Union[Point, _Mapping]] = ..., axisEndPoint: _Optional[_Union[Point, _Mapping]] = ..., radius: _Optional[float] = ...) -> None: ...

class Geometry(_message.Message):
    __slots__ = ("point", "polyline", "box", "cylinder", "sphere")
    POINT_FIELD_NUMBER: _ClassVar[int]
    POLYLINE_FIELD_NUMBER: _ClassVar[int]
    BOX_FIELD_NUMBER: _ClassVar[int]
    CYLINDER_FIELD_NUMBER: _ClassVar[int]
    SPHERE_FIELD_NUMBER: _ClassVar[int]
    point: Point
    polyline: Polyline
    box: Box
    cylinder: Cylinder
    sphere: Sphere
    def __init__(self, point: _Optional[_Union[Point, _Mapping]] = ..., polyline: _Optional[_Union[Polyline, _Mapping]] = ..., box: _Optional[_Union[Box, _Mapping]] = ..., cylinder: _Optional[_Union[Cylinder, _Mapping]] = ..., sphere: _Optional[_Union[Sphere, _Mapping]] = ...) -> None: ...

class VolumeGeometry(_message.Message):
    __slots__ = ("box", "cylinder", "sphere")
    BOX_FIELD_NUMBER: _ClassVar[int]
    CYLINDER_FIELD_NUMBER: _ClassVar[int]
    SPHERE_FIELD_NUMBER: _ClassVar[int]
    box: Box
    cylinder: Cylinder
    sphere: Sphere
    def __init__(self, box: _Optional[_Union[Box, _Mapping]] = ..., cylinder: _Optional[_Union[Cylinder, _Mapping]] = ..., sphere: _Optional[_Union[Sphere, _Mapping]] = ...) -> None: ...

class NodesSelection(_message.Message):
    __slots__ = ("region",)
    REGION_FIELD_NUMBER: _ClassVar[int]
    region: Geometry
    def __init__(self, region: _Optional[_Union[Geometry, _Mapping]] = ...) -> None: ...

class RegionSelectionSetting(_message.Message):
    __slots__ = ("region", "includeIntersecting")
    REGION_FIELD_NUMBER: _ClassVar[int]
    INCLUDEINTERSECTING_FIELD_NUMBER: _ClassVar[int]
    region: Geometry
    includeIntersecting: bool
    def __init__(self, region: _Optional[_Union[Geometry, _Mapping]] = ..., includeIntersecting: bool = ...) -> None: ...

import CommonGeometryMessages_pb2 as _CommonGeometryMessages_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class _getExternalVolumesByGeometryRequest(_message.Message):
    __slots__ = ("_projectId", "geometry", "includeIntersecting")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    INCLUDEINTERSECTING_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    geometry: _CommonGeometryMessages_pb2.Geometry
    includeIntersecting: bool
    def __init__(self, _projectId: _Optional[str] = ..., geometry: _Optional[_Union[_CommonGeometryMessages_pb2.Geometry, _Mapping]] = ..., includeIntersecting: bool = ...) -> None: ...

class _getExternalVolumesByGeometryResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getAttachedExternalVolumesRequest(_message.Message):
    __slots__ = ("_projectId", "_externalVolumeID")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _EXTERNALVOLUMEID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    _externalVolumeID: str
    def __init__(self, _projectId: _Optional[str] = ..., _externalVolumeID: _Optional[str] = ...) -> None: ...

class getAttachedExternalVolumesResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getAttachedExternalVolumesByVolumeNameRequest(_message.Message):
    __slots__ = ("_projectId", "externalVolumeName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    EXTERNALVOLUMENAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    externalVolumeName: str
    def __init__(self, _projectId: _Optional[str] = ..., externalVolumeName: _Optional[str] = ...) -> None: ...

class getAttachedExternalVolumesByVolumeNameResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

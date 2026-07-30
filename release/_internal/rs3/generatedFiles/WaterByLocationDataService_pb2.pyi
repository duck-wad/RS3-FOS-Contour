import CommonMessages_pb2 as _CommonMessages_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetProjectPropertyRequest(_message.Message):
    __slots__ = ("objectId", "propertyName", "value", "projectId")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    propertyName: str
    value: _CommonMessages_pb2.PropertyValue
    projectId: str
    def __init__(self, objectId: _Optional[str] = ..., propertyName: _Optional[str] = ..., value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ..., projectId: _Optional[str] = ...) -> None: ...

class SetProjectPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetProjectPropertyRequest(_message.Message):
    __slots__ = ("objectId", "propertyName", "projectId")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    propertyName: str
    projectId: str
    def __init__(self, objectId: _Optional[str] = ..., propertyName: _Optional[str] = ..., projectId: _Optional[str] = ...) -> None: ...

class GetProjectPropertyResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

class SetProjectColorRequest(_message.Message):
    __slots__ = ("objectId", "value", "projectId")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    value: bytes
    projectId: str
    def __init__(self, objectId: _Optional[str] = ..., value: _Optional[bytes] = ..., projectId: _Optional[str] = ...) -> None: ...

class SetProjectColorResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetProjectColorRequest(_message.Message):
    __slots__ = ("objectId", "projectId")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    projectId: str
    def __init__(self, objectId: _Optional[str] = ..., projectId: _Optional[str] = ...) -> None: ...

class GetProjectColorResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bytes
    def __init__(self, value: _Optional[bytes] = ...) -> None: ...

class SetWaterByLocationsRequest(_message.Message):
    __slots__ = ("projectId", "waterSurfaceId", "waterSurfaceLocation")
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    WATERSURFACEID_FIELD_NUMBER: _ClassVar[int]
    WATERSURFACELOCATION_FIELD_NUMBER: _ClassVar[int]
    projectId: str
    waterSurfaceId: str
    waterSurfaceLocation: _containers.RepeatedCompositeFieldContainer[_CommonMessages_pb2.Point3D]
    def __init__(self, projectId: _Optional[str] = ..., waterSurfaceId: _Optional[str] = ..., waterSurfaceLocation: _Optional[_Iterable[_Union[_CommonMessages_pb2.Point3D, _Mapping]]] = ...) -> None: ...

class SetWaterByLocationsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetWaterByLocationsRequest(_message.Message):
    __slots__ = ("waterSurfaceId", "projectId")
    WATERSURFACEID_FIELD_NUMBER: _ClassVar[int]
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    waterSurfaceId: str
    projectId: str
    def __init__(self, waterSurfaceId: _Optional[str] = ..., projectId: _Optional[str] = ...) -> None: ...

class GetWaterByLocationsResponse(_message.Message):
    __slots__ = ("waterSurfaceLocation",)
    WATERSURFACELOCATION_FIELD_NUMBER: _ClassVar[int]
    waterSurfaceLocation: _containers.RepeatedCompositeFieldContainer[_CommonMessages_pb2.Point3D]
    def __init__(self, waterSurfaceLocation: _Optional[_Iterable[_Union[_CommonMessages_pb2.Point3D, _Mapping]]] = ...) -> None: ...

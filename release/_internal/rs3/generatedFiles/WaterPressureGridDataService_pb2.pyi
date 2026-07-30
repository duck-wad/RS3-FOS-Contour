import CommonMessages_pb2 as _CommonMessages_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WaterGridSet(_message.Message):
    __slots__ = ("x", "y", "z", "commonValue")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    COMMONVALUE_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    commonValue: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ..., commonValue: _Optional[float] = ...) -> None: ...

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

class SetPWPPointSetRequest(_message.Message):
    __slots__ = ("projectId", "waterGridId", "PWPPointSet")
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    WATERGRIDID_FIELD_NUMBER: _ClassVar[int]
    PWPPOINTSET_FIELD_NUMBER: _ClassVar[int]
    projectId: str
    waterGridId: str
    PWPPointSet: _containers.RepeatedCompositeFieldContainer[WaterGridSet]
    def __init__(self, projectId: _Optional[str] = ..., waterGridId: _Optional[str] = ..., PWPPointSet: _Optional[_Iterable[_Union[WaterGridSet, _Mapping]]] = ...) -> None: ...

class SetPWPPointSetResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPWPPointSetRequest(_message.Message):
    __slots__ = ("waterGridId", "projectId")
    WATERGRIDID_FIELD_NUMBER: _ClassVar[int]
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    waterGridId: str
    projectId: str
    def __init__(self, waterGridId: _Optional[str] = ..., projectId: _Optional[str] = ...) -> None: ...

class GetPWPPointSetResponse(_message.Message):
    __slots__ = ("PWPPointSet",)
    PWPPOINTSET_FIELD_NUMBER: _ClassVar[int]
    PWPPointSet: _containers.RepeatedCompositeFieldContainer[WaterGridSet]
    def __init__(self, PWPPointSet: _Optional[_Iterable[_Union[WaterGridSet, _Mapping]]] = ...) -> None: ...

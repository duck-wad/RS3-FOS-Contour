from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PropertyValue(_message.Message):
    __slots__ = ("doubleValue", "floatValue", "intValue", "longValue", "uintValue", "ulongValue", "boolValue", "stringValue", "bytesValue", "enumValue", "vector3DValue", "point3DValue")
    DOUBLEVALUE_FIELD_NUMBER: _ClassVar[int]
    FLOATVALUE_FIELD_NUMBER: _ClassVar[int]
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    LONGVALUE_FIELD_NUMBER: _ClassVar[int]
    UINTVALUE_FIELD_NUMBER: _ClassVar[int]
    ULONGVALUE_FIELD_NUMBER: _ClassVar[int]
    BOOLVALUE_FIELD_NUMBER: _ClassVar[int]
    STRINGVALUE_FIELD_NUMBER: _ClassVar[int]
    BYTESVALUE_FIELD_NUMBER: _ClassVar[int]
    ENUMVALUE_FIELD_NUMBER: _ClassVar[int]
    VECTOR3DVALUE_FIELD_NUMBER: _ClassVar[int]
    POINT3DVALUE_FIELD_NUMBER: _ClassVar[int]
    doubleValue: float
    floatValue: float
    intValue: int
    longValue: int
    uintValue: int
    ulongValue: int
    boolValue: bool
    stringValue: str
    bytesValue: bytes
    enumValue: str
    vector3DValue: Vector3D
    point3DValue: Point3D
    def __init__(self, doubleValue: _Optional[float] = ..., floatValue: _Optional[float] = ..., intValue: _Optional[int] = ..., longValue: _Optional[int] = ..., uintValue: _Optional[int] = ..., ulongValue: _Optional[int] = ..., boolValue: bool = ..., stringValue: _Optional[str] = ..., bytesValue: _Optional[bytes] = ..., enumValue: _Optional[str] = ..., vector3DValue: _Optional[_Union[Vector3D, _Mapping]] = ..., point3DValue: _Optional[_Union[Point3D, _Mapping]] = ...) -> None: ...

class SetPropertyRequest(_message.Message):
    __slots__ = ("objectId", "propertyName", "value")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    propertyName: str
    value: PropertyValue
    def __init__(self, objectId: _Optional[str] = ..., propertyName: _Optional[str] = ..., value: _Optional[_Union[PropertyValue, _Mapping]] = ...) -> None: ...

class SetPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPropertyRequest(_message.Message):
    __slots__ = ("objectId", "propertyName")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    propertyName: str
    def __init__(self, objectId: _Optional[str] = ..., propertyName: _Optional[str] = ...) -> None: ...

class GetPropertyResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: PropertyValue
    def __init__(self, value: _Optional[_Union[PropertyValue, _Mapping]] = ...) -> None: ...

class SetColorRequest(_message.Message):
    __slots__ = ("objectId", "value")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    value: bytes
    def __init__(self, objectId: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...

class SetColorResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetColorRequest(_message.Message):
    __slots__ = ("objectId",)
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    def __init__(self, objectId: _Optional[str] = ...) -> None: ...

class GetColorResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bytes
    def __init__(self, value: _Optional[bytes] = ...) -> None: ...

class SetStageFactorPropertyRequest(_message.Message):
    __slots__ = ("propertyId", "stageFactorId", "propertyName", "value")
    PROPERTYID_FIELD_NUMBER: _ClassVar[int]
    STAGEFACTORID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    propertyId: str
    stageFactorId: str
    propertyName: str
    value: PropertyValue
    def __init__(self, propertyId: _Optional[str] = ..., stageFactorId: _Optional[str] = ..., propertyName: _Optional[str] = ..., value: _Optional[_Union[PropertyValue, _Mapping]] = ...) -> None: ...

class SetStageFactorPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetStageFactorPropertyRequest(_message.Message):
    __slots__ = ("propertyId", "stageFactorId", "propertyName")
    PROPERTYID_FIELD_NUMBER: _ClassVar[int]
    STAGEFACTORID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    propertyId: str
    stageFactorId: str
    propertyName: str
    def __init__(self, propertyId: _Optional[str] = ..., stageFactorId: _Optional[str] = ..., propertyName: _Optional[str] = ...) -> None: ...

class GetStageFactorPropertyResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: PropertyValue
    def __init__(self, value: _Optional[_Union[PropertyValue, _Mapping]] = ...) -> None: ...

class Point3D(_message.Message):
    __slots__ = ("x", "y", "z")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

class Vector3D(_message.Message):
    __slots__ = ("x", "y", "z")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

class LinearDirection(_message.Message):
    __slots__ = ("trend", "plunge")
    TREND_FIELD_NUMBER: _ClassVar[int]
    PLUNGE_FIELD_NUMBER: _ClassVar[int]
    trend: float
    plunge: float
    def __init__(self, trend: _Optional[float] = ..., plunge: _Optional[float] = ...) -> None: ...

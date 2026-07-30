import CommonMessages_pb2 as _CommonMessages_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserDefinedFunctionPoint(_message.Message):
    __slots__ = ("suction", "value")
    SUCTION_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    suction: float
    value: float
    def __init__(self, suction: _Optional[float] = ..., value: _Optional[float] = ...) -> None: ...

class SetUserDefinedFunctionRequest(_message.Message):
    __slots__ = ("objectId", "projectId", "propertyName", "point")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    POINT_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    projectId: str
    propertyName: str
    point: _containers.RepeatedCompositeFieldContainer[UserDefinedFunctionPoint]
    def __init__(self, objectId: _Optional[str] = ..., projectId: _Optional[str] = ..., propertyName: _Optional[str] = ..., point: _Optional[_Iterable[_Union[UserDefinedFunctionPoint, _Mapping]]] = ...) -> None: ...

class SetUserDefinedFunctionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetUserDefinedFunctionRequest(_message.Message):
    __slots__ = ("objectId", "projectId", "propertyName")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    projectId: str
    propertyName: str
    def __init__(self, objectId: _Optional[str] = ..., projectId: _Optional[str] = ..., propertyName: _Optional[str] = ...) -> None: ...

class GetUserDefinedFunctionResponse(_message.Message):
    __slots__ = ("point",)
    POINT_FIELD_NUMBER: _ClassVar[int]
    point: _containers.RepeatedCompositeFieldContainer[UserDefinedFunctionPoint]
    def __init__(self, point: _Optional[_Iterable[_Union[UserDefinedFunctionPoint, _Mapping]]] = ...) -> None: ...

class SetCustomHydraulicModelPropertyRequest(_message.Message):
    __slots__ = ("objectId", "projectId", "propertyName", "value")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    projectId: str
    propertyName: str
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, objectId: _Optional[str] = ..., projectId: _Optional[str] = ..., propertyName: _Optional[str] = ..., value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

class SetCustomHydraulicModelPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCustomHydraulicModelPropertyRequest(_message.Message):
    __slots__ = ("objectId", "projectId", "propertyName")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    projectId: str
    propertyName: str
    def __init__(self, objectId: _Optional[str] = ..., projectId: _Optional[str] = ..., propertyName: _Optional[str] = ...) -> None: ...

class GetCustomHydraulicModelPropertyResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

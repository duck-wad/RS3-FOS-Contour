import CommonMessages_pb2 as _CommonMessages_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetMaterialStiffnessPropertyRequest(_message.Message):
    __slots__ = ("propertyId", "isLoading", "propertyName", "value")
    PROPERTYID_FIELD_NUMBER: _ClassVar[int]
    ISLOADING_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    propertyId: str
    isLoading: bool
    propertyName: str
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, propertyId: _Optional[str] = ..., isLoading: bool = ..., propertyName: _Optional[str] = ..., value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

class SetMaterialStiffnessPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMaterialStiffnessPropertyRequest(_message.Message):
    __slots__ = ("propertyId", "isLoading", "propertyName")
    PROPERTYID_FIELD_NUMBER: _ClassVar[int]
    ISLOADING_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    propertyId: str
    isLoading: bool
    propertyName: str
    def __init__(self, propertyId: _Optional[str] = ..., isLoading: bool = ..., propertyName: _Optional[str] = ...) -> None: ...

class GetMaterialStiffnessPropertyResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

class SetMaterialStiffnessBeddingPlanePropertyRequest(_message.Message):
    __slots__ = ("objectId", "propertyName", "value")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    propertyName: str
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, objectId: _Optional[str] = ..., propertyName: _Optional[str] = ..., value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

class SetMaterialStiffnessBeddingPlanePropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMaterialStiffnessBeddingPlanePropertyRequest(_message.Message):
    __slots__ = ("objectId", "propertyName")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    propertyName: str
    def __init__(self, objectId: _Optional[str] = ..., propertyName: _Optional[str] = ...) -> None: ...

class GetMaterialStiffnessBeddingPlanePropertyResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

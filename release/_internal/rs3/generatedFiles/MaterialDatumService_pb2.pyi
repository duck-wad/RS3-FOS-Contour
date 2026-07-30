import CommonMessages_pb2 as _CommonMessages_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetDatumPropertyRequest(_message.Message):
    __slots__ = ("objectId", "upperPropertyName", "propertyName", "value")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    UPPERPROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    upperPropertyName: str
    propertyName: str
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, objectId: _Optional[str] = ..., upperPropertyName: _Optional[str] = ..., propertyName: _Optional[str] = ..., value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

class SetDatumPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetDatumPropertyRequest(_message.Message):
    __slots__ = ("objectId", "upperPropertyName", "propertyName")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    UPPERPROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    upperPropertyName: str
    propertyName: str
    def __init__(self, objectId: _Optional[str] = ..., upperPropertyName: _Optional[str] = ..., propertyName: _Optional[str] = ...) -> None: ...

class GetDatumPropertyResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

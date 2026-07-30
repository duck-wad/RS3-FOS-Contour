import CommonMessages_pb2 as _CommonMessages_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetJointRequest(_message.Message):
    __slots__ = ("objectId", "jointIndex")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    JOINTINDEX_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    jointIndex: int
    def __init__(self, objectId: _Optional[str] = ..., jointIndex: _Optional[int] = ...) -> None: ...

class GetJointResponse(_message.Message):
    __slots__ = ("jointId",)
    JOINTID_FIELD_NUMBER: _ClassVar[int]
    jointId: str
    def __init__(self, jointId: _Optional[str] = ...) -> None: ...

class SetJointPropertyRequest(_message.Message):
    __slots__ = ("materialId", "objectId", "propertyName", "value")
    MATERIALID_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    materialId: str
    objectId: str
    propertyName: str
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, materialId: _Optional[str] = ..., objectId: _Optional[str] = ..., propertyName: _Optional[str] = ..., value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

class SetJointPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetJointPropertyRequest(_message.Message):
    __slots__ = ("materialId", "objectId", "propertyName")
    MATERIALID_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    materialId: str
    objectId: str
    propertyName: str
    def __init__(self, materialId: _Optional[str] = ..., objectId: _Optional[str] = ..., propertyName: _Optional[str] = ...) -> None: ...

class GetJointPropertyResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

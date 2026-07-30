import CommonMessages_pb2 as _CommonMessages_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetMaterialJointStageFactorPropertyRequest(_message.Message):
    __slots__ = ("materialId", "jointId", "stageFactorId", "propertyName", "value")
    MATERIALID_FIELD_NUMBER: _ClassVar[int]
    JOINTID_FIELD_NUMBER: _ClassVar[int]
    STAGEFACTORID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    materialId: str
    jointId: str
    stageFactorId: str
    propertyName: str
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, materialId: _Optional[str] = ..., jointId: _Optional[str] = ..., stageFactorId: _Optional[str] = ..., propertyName: _Optional[str] = ..., value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

class SetMaterialJointStageFactorPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMaterialJointStageFactorPropertyRequest(_message.Message):
    __slots__ = ("materialId", "jointId", "stageFactorId", "propertyName")
    MATERIALID_FIELD_NUMBER: _ClassVar[int]
    JOINTID_FIELD_NUMBER: _ClassVar[int]
    STAGEFACTORID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    materialId: str
    jointId: str
    stageFactorId: str
    propertyName: str
    def __init__(self, materialId: _Optional[str] = ..., jointId: _Optional[str] = ..., stageFactorId: _Optional[str] = ..., propertyName: _Optional[str] = ...) -> None: ...

class GetMaterialJointStageFactorPropertyResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

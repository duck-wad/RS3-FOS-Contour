import CommonMessages_pb2 as _CommonMessages_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetInitialWaterConditionRequest(_message.Message):
    __slots__ = ("propertyId", "stageFactorId", "waterType", "waterTableName")
    PROPERTYID_FIELD_NUMBER: _ClassVar[int]
    STAGEFACTORID_FIELD_NUMBER: _ClassVar[int]
    WATERTYPE_FIELD_NUMBER: _ClassVar[int]
    WATERTABLENAME_FIELD_NUMBER: _ClassVar[int]
    propertyId: str
    stageFactorId: str
    waterType: str
    waterTableName: str
    def __init__(self, propertyId: _Optional[str] = ..., stageFactorId: _Optional[str] = ..., waterType: _Optional[str] = ..., waterTableName: _Optional[str] = ...) -> None: ...

class SetInitialWaterConditionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetInitialWaterConditionRequest(_message.Message):
    __slots__ = ("propertyId", "stageFactorId")
    PROPERTYID_FIELD_NUMBER: _ClassVar[int]
    STAGEFACTORID_FIELD_NUMBER: _ClassVar[int]
    propertyId: str
    stageFactorId: str
    def __init__(self, propertyId: _Optional[str] = ..., stageFactorId: _Optional[str] = ...) -> None: ...

class GetInitialWaterConditionResponse(_message.Message):
    __slots__ = ("waterTableName",)
    WATERTABLENAME_FIELD_NUMBER: _ClassVar[int]
    waterTableName: str
    def __init__(self, waterTableName: _Optional[str] = ...) -> None: ...

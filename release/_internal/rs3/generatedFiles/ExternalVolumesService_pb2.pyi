import CommonMessages_pb2 as _CommonMessages_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetAppliedMaterialPropertyRequest(_message.Message):
    __slots__ = ("objectId", "stageNum", "materialName")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    STAGENUM_FIELD_NUMBER: _ClassVar[int]
    MATERIALNAME_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    stageNum: int
    materialName: str
    def __init__(self, objectId: _Optional[str] = ..., stageNum: _Optional[int] = ..., materialName: _Optional[str] = ...) -> None: ...

class SetAppliedMaterialPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAppliedMaterialPropertyRequest(_message.Message):
    __slots__ = ("objectId", "stageNum")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    STAGENUM_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    stageNum: int
    def __init__(self, objectId: _Optional[str] = ..., stageNum: _Optional[int] = ...) -> None: ...

class GetAppliedMaterialPropertyResponse(_message.Message):
    __slots__ = ("materialName",)
    MATERIALNAME_FIELD_NUMBER: _ClassVar[int]
    materialName: str
    def __init__(self, materialName: _Optional[str] = ...) -> None: ...

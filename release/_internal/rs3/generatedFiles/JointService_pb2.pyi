import CommonMessages_pb2 as _CommonMessages_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetSlipStageRequest(_message.Message):
    __slots__ = ("jointId", "slipStageNumber")
    JOINTID_FIELD_NUMBER: _ClassVar[int]
    SLIPSTAGENUMBER_FIELD_NUMBER: _ClassVar[int]
    jointId: str
    slipStageNumber: int
    def __init__(self, jointId: _Optional[str] = ..., slipStageNumber: _Optional[int] = ...) -> None: ...

class SetSlipStageResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSlipStageRequest(_message.Message):
    __slots__ = ("jointId",)
    JOINTID_FIELD_NUMBER: _ClassVar[int]
    jointId: str
    def __init__(self, jointId: _Optional[str] = ...) -> None: ...

class GetSlipStageResponse(_message.Message):
    __slots__ = ("slipStageNumber",)
    SLIPSTAGENUMBER_FIELD_NUMBER: _ClassVar[int]
    slipStageNumber: int
    def __init__(self, slipStageNumber: _Optional[int] = ...) -> None: ...

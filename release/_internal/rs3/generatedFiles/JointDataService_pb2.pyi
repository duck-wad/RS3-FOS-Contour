import CommonMessages_pb2 as _CommonMessages_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetPiezoToUseRequest(_message.Message):
    __slots__ = ("jointId", "piezoName")
    JOINTID_FIELD_NUMBER: _ClassVar[int]
    PIEZONAME_FIELD_NUMBER: _ClassVar[int]
    jointId: str
    piezoName: str
    def __init__(self, jointId: _Optional[str] = ..., piezoName: _Optional[str] = ...) -> None: ...

class SetPiezoToUseResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPiezoToUseRequest(_message.Message):
    __slots__ = ("jointId",)
    JOINTID_FIELD_NUMBER: _ClassVar[int]
    jointId: str
    def __init__(self, jointId: _Optional[str] = ...) -> None: ...

class GetPiezoToUseResponse(_message.Message):
    __slots__ = ("piezoName",)
    PIEZONAME_FIELD_NUMBER: _ClassVar[int]
    piezoName: str
    def __init__(self, piezoName: _Optional[str] = ...) -> None: ...

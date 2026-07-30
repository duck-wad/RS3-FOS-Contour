from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PingRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PingResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OpenFileRequest(_message.Message):
    __slots__ = ("fileName",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    fileName: str
    def __init__(self, fileName: _Optional[str] = ...) -> None: ...

class OpenFileResponse(_message.Message):
    __slots__ = ("modelID", "success")
    MODELID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    modelID: str
    success: bool
    def __init__(self, modelID: _Optional[str] = ..., success: bool = ...) -> None: ...

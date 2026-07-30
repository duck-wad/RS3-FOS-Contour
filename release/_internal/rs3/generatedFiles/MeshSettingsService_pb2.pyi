import CommonMessages_pb2 as _CommonMessages_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MeshRequest(_message.Message):
    __slots__ = ("projectId",)
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    projectId: str
    def __init__(self, projectId: _Optional[str] = ...) -> None: ...

class MeshResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

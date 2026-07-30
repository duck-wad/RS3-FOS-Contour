from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetIsRelativeStagingRequest(_message.Message):
    __slots__ = ("propertyID",)
    PROPERTYID_FIELD_NUMBER: _ClassVar[int]
    propertyID: str
    def __init__(self, propertyID: _Optional[str] = ...) -> None: ...

class GetIsRelativeStagingResponse(_message.Message):
    __slots__ = ("isRelativeStaging",)
    ISRELATIVESTAGING_FIELD_NUMBER: _ClassVar[int]
    isRelativeStaging: bool
    def __init__(self, isRelativeStaging: bool = ...) -> None: ...

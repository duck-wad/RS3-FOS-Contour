from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetBulgeLocationsRequest(_message.Message):
    __slots__ = ("boltId", "bulgeLocations")
    BOLTID_FIELD_NUMBER: _ClassVar[int]
    BULGELOCATIONS_FIELD_NUMBER: _ClassVar[int]
    boltId: str
    bulgeLocations: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, boltId: _Optional[str] = ..., bulgeLocations: _Optional[_Iterable[float]] = ...) -> None: ...

class SetBulgeLocationsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetBulgeLocationsRequest(_message.Message):
    __slots__ = ("boltId",)
    BOLTID_FIELD_NUMBER: _ClassVar[int]
    boltId: str
    def __init__(self, boltId: _Optional[str] = ...) -> None: ...

class GetBulgeLocationsResponse(_message.Message):
    __slots__ = ("bulgeLocations",)
    BULGELOCATIONS_FIELD_NUMBER: _ClassVar[int]
    bulgeLocations: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, bulgeLocations: _Optional[_Iterable[float]] = ...) -> None: ...

import CommonMessages_pb2 as _CommonMessages_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GaussPointFailure(_message.Message):
    __slots__ = ("location", "failureType")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    FAILURETYPE_FIELD_NUMBER: _ClassVar[int]
    location: _CommonMessages_pb2.Point3D
    failureType: str
    def __init__(self, location: _Optional[_Union[_CommonMessages_pb2.Point3D, _Mapping]] = ..., failureType: _Optional[str] = ...) -> None: ...

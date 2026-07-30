import CommonMessages_pb2 as _CommonMessages_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetBeamPropertyRequest(_message.Message):
    __slots__ = ("pileId", "beamName")
    PILEID_FIELD_NUMBER: _ClassVar[int]
    BEAMNAME_FIELD_NUMBER: _ClassVar[int]
    pileId: str
    beamName: str
    def __init__(self, pileId: _Optional[str] = ..., beamName: _Optional[str] = ...) -> None: ...

class SetBeamPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetBeamPropertyRequest(_message.Message):
    __slots__ = ("pileId",)
    PILEID_FIELD_NUMBER: _ClassVar[int]
    pileId: str
    def __init__(self, pileId: _Optional[str] = ...) -> None: ...

class GetBeamPropertyResponse(_message.Message):
    __slots__ = ("beamName",)
    BEAMNAME_FIELD_NUMBER: _ClassVar[int]
    beamName: str
    def __init__(self, beamName: _Optional[str] = ...) -> None: ...

class DistanceTractionValues(_message.Message):
    __slots__ = ("distances", "tractions")
    DISTANCES_FIELD_NUMBER: _ClassVar[int]
    TRACTIONS_FIELD_NUMBER: _ClassVar[int]
    distances: float
    tractions: float
    def __init__(self, distances: _Optional[float] = ..., tractions: _Optional[float] = ...) -> None: ...

class GetMultiLinearGridRequest(_message.Message):
    __slots__ = ("pileId",)
    PILEID_FIELD_NUMBER: _ClassVar[int]
    pileId: str
    def __init__(self, pileId: _Optional[str] = ...) -> None: ...

class GetMultiLinearGridResponse(_message.Message):
    __slots__ = ("distanceTractionValues",)
    DISTANCETRACTIONVALUES_FIELD_NUMBER: _ClassVar[int]
    distanceTractionValues: _containers.RepeatedCompositeFieldContainer[DistanceTractionValues]
    def __init__(self, distanceTractionValues: _Optional[_Iterable[_Union[DistanceTractionValues, _Mapping]]] = ...) -> None: ...

class SetMultiLinearGridRequest(_message.Message):
    __slots__ = ("pileId", "distanceTractionValues")
    PILEID_FIELD_NUMBER: _ClassVar[int]
    DISTANCETRACTIONVALUES_FIELD_NUMBER: _ClassVar[int]
    pileId: str
    distanceTractionValues: _containers.RepeatedCompositeFieldContainer[DistanceTractionValues]
    def __init__(self, pileId: _Optional[str] = ..., distanceTractionValues: _Optional[_Iterable[_Union[DistanceTractionValues, _Mapping]]] = ...) -> None: ...

class SetMultiLinearGridResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

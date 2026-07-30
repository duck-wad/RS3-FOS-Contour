import CommonMessages_pb2 as _CommonMessages_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SingleEffectiveStressPoint(_message.Message):
    __slots__ = ("X", "Y")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    X: float
    Y: float
    def __init__(self, X: _Optional[float] = ..., Y: _Optional[float] = ...) -> None: ...

class SetSingleEffectiveStressRequest(_message.Message):
    __slots__ = ("objectId", "tabularValueType", "point")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    TABULARVALUETYPE_FIELD_NUMBER: _ClassVar[int]
    POINT_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    tabularValueType: str
    point: _containers.RepeatedCompositeFieldContainer[SingleEffectiveStressPoint]
    def __init__(self, objectId: _Optional[str] = ..., tabularValueType: _Optional[str] = ..., point: _Optional[_Iterable[_Union[SingleEffectiveStressPoint, _Mapping]]] = ...) -> None: ...

class SetSingleEffectiveStressResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSingleEffectiveStressRequest(_message.Message):
    __slots__ = ("objectId", "tabularValueType")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    TABULARVALUETYPE_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    tabularValueType: str
    def __init__(self, objectId: _Optional[str] = ..., tabularValueType: _Optional[str] = ...) -> None: ...

class GetSingleEffectiveStressResponse(_message.Message):
    __slots__ = ("point",)
    POINT_FIELD_NUMBER: _ClassVar[int]
    point: _containers.RepeatedCompositeFieldContainer[SingleEffectiveStressPoint]
    def __init__(self, point: _Optional[_Iterable[_Union[SingleEffectiveStressPoint, _Mapping]]] = ...) -> None: ...

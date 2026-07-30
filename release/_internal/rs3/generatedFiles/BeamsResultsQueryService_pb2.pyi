import ResultsQueryService_pb2 as _ResultsQueryService_pb2
import ResultsQueryCommonMessage_pb2 as _ResultsQueryCommonMessage_pb2
import BFPCommonMessage_pb2 as _BFPCommonMessage_pb2
import GaussPointFailureMessage_pb2 as _GaussPointFailureMessage_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BeamResultQueryBase(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class ElementResults(_message.Message):
    __slots__ = ("elementInformation", "entityInformation", "nodeValues", "failurePoint")
    ELEMENTINFORMATION_FIELD_NUMBER: _ClassVar[int]
    ENTITYINFORMATION_FIELD_NUMBER: _ClassVar[int]
    NODEVALUES_FIELD_NUMBER: _ClassVar[int]
    FAILUREPOINT_FIELD_NUMBER: _ClassVar[int]
    elementInformation: _ResultsQueryService_pb2.ElementInformation
    entityInformation: _ResultsQueryCommonMessage_pb2.EntityMessage
    nodeValues: _containers.RepeatedCompositeFieldContainer[_BFPCommonMessage_pb2.ElementNodalValues]
    failurePoint: _GaussPointFailureMessage_pb2.GaussPointFailure
    def __init__(self, elementInformation: _Optional[_Union[_ResultsQueryService_pb2.ElementInformation, _Mapping]] = ..., entityInformation: _Optional[_Union[_ResultsQueryCommonMessage_pb2.EntityMessage, _Mapping]] = ..., nodeValues: _Optional[_Iterable[_Union[_BFPCommonMessage_pb2.ElementNodalValues, _Mapping]]] = ..., failurePoint: _Optional[_Union[_GaussPointFailureMessage_pb2.GaussPointFailure, _Mapping]] = ...) -> None: ...

class BeamElementResultsHeader(_message.Message):
    __slots__ = ("totalQueriedElementsCount",)
    TOTALQUERIEDELEMENTSCOUNT_FIELD_NUMBER: _ClassVar[int]
    totalQueriedElementsCount: int
    def __init__(self, totalQueriedElementsCount: _Optional[int] = ...) -> None: ...

class BeamElementResultsData(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ElementResults]
    def __init__(self, results: _Optional[_Iterable[_Union[ElementResults, _Mapping]]] = ...) -> None: ...

class BeamElementResultsResponseChunk(_message.Message):
    __slots__ = ("header", "data")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    header: BeamElementResultsHeader
    data: BeamElementResultsData
    def __init__(self, header: _Optional[_Union[BeamElementResultsHeader, _Mapping]] = ..., data: _Optional[_Union[BeamElementResultsData, _Mapping]] = ...) -> None: ...

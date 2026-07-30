import ResultsQueryService_pb2 as _ResultsQueryService_pb2
import ResultsQueryCommonMessage_pb2 as _ResultsQueryCommonMessage_pb2
import GaussPointFailureMessage_pb2 as _GaussPointFailureMessage_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BoltResultQueryBase(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class BoltNodalResultValues(_message.Message):
    __slots__ = ("axisForce", "axisStress", "displacementX", "displacementY", "displacementZ", "displacementTotal", "interfaceShearForce", "interfaceDisplacementX", "interfaceDisplacementY", "interfaceDisplacementZ", "interfaceDisplacementTotal")
    AXISFORCE_FIELD_NUMBER: _ClassVar[int]
    AXISSTRESS_FIELD_NUMBER: _ClassVar[int]
    DISPLACEMENTX_FIELD_NUMBER: _ClassVar[int]
    DISPLACEMENTY_FIELD_NUMBER: _ClassVar[int]
    DISPLACEMENTZ_FIELD_NUMBER: _ClassVar[int]
    DISPLACEMENTTOTAL_FIELD_NUMBER: _ClassVar[int]
    INTERFACESHEARFORCE_FIELD_NUMBER: _ClassVar[int]
    INTERFACEDISPLACEMENTX_FIELD_NUMBER: _ClassVar[int]
    INTERFACEDISPLACEMENTY_FIELD_NUMBER: _ClassVar[int]
    INTERFACEDISPLACEMENTZ_FIELD_NUMBER: _ClassVar[int]
    INTERFACEDISPLACEMENTTOTAL_FIELD_NUMBER: _ClassVar[int]
    axisForce: float
    axisStress: float
    displacementX: float
    displacementY: float
    displacementZ: float
    displacementTotal: float
    interfaceShearForce: float
    interfaceDisplacementX: float
    interfaceDisplacementY: float
    interfaceDisplacementZ: float
    interfaceDisplacementTotal: float
    def __init__(self, axisForce: _Optional[float] = ..., axisStress: _Optional[float] = ..., displacementX: _Optional[float] = ..., displacementY: _Optional[float] = ..., displacementZ: _Optional[float] = ..., displacementTotal: _Optional[float] = ..., interfaceShearForce: _Optional[float] = ..., interfaceDisplacementX: _Optional[float] = ..., interfaceDisplacementY: _Optional[float] = ..., interfaceDisplacementZ: _Optional[float] = ..., interfaceDisplacementTotal: _Optional[float] = ...) -> None: ...

class ElementResults(_message.Message):
    __slots__ = ("elementInformation", "entityInformation", "boltID", "nodeValues", "failurePoint")
    ELEMENTINFORMATION_FIELD_NUMBER: _ClassVar[int]
    ENTITYINFORMATION_FIELD_NUMBER: _ClassVar[int]
    BOLTID_FIELD_NUMBER: _ClassVar[int]
    NODEVALUES_FIELD_NUMBER: _ClassVar[int]
    FAILUREPOINT_FIELD_NUMBER: _ClassVar[int]
    elementInformation: _ResultsQueryService_pb2.ElementInformation
    entityInformation: _ResultsQueryCommonMessage_pb2.EntityMessage
    boltID: int
    nodeValues: _containers.RepeatedCompositeFieldContainer[BoltNodalResultValues]
    failurePoint: _GaussPointFailureMessage_pb2.GaussPointFailure
    def __init__(self, elementInformation: _Optional[_Union[_ResultsQueryService_pb2.ElementInformation, _Mapping]] = ..., entityInformation: _Optional[_Union[_ResultsQueryCommonMessage_pb2.EntityMessage, _Mapping]] = ..., boltID: _Optional[int] = ..., nodeValues: _Optional[_Iterable[_Union[BoltNodalResultValues, _Mapping]]] = ..., failurePoint: _Optional[_Union[_GaussPointFailureMessage_pb2.GaussPointFailure, _Mapping]] = ...) -> None: ...

class BoltElementResultsHeader(_message.Message):
    __slots__ = ("totalQueriedElementsCount",)
    TOTALQUERIEDELEMENTSCOUNT_FIELD_NUMBER: _ClassVar[int]
    totalQueriedElementsCount: int
    def __init__(self, totalQueriedElementsCount: _Optional[int] = ...) -> None: ...

class BoltElementResultsData(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ElementResults]
    def __init__(self, results: _Optional[_Iterable[_Union[ElementResults, _Mapping]]] = ...) -> None: ...

class BoltElementResultsResponseChunk(_message.Message):
    __slots__ = ("header", "data")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    header: BoltElementResultsHeader
    data: BoltElementResultsData
    def __init__(self, header: _Optional[_Union[BoltElementResultsHeader, _Mapping]] = ..., data: _Optional[_Union[BoltElementResultsData, _Mapping]] = ...) -> None: ...

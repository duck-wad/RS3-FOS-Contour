import ResultsQueryCommonMessage_pb2 as _ResultsQueryCommonMessage_pb2
import BFPCommonMessage_pb2 as _BFPCommonMessage_pb2
import GaussPointFailureMessage_pb2 as _GaussPointFailureMessage_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PileForepoleResultQueryBase(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class NodalValues(_message.Message):
    __slots__ = ("elementNodeValues", "interfaceNodeValues")
    ELEMENTNODEVALUES_FIELD_NUMBER: _ClassVar[int]
    INTERFACENODEVALUES_FIELD_NUMBER: _ClassVar[int]
    elementNodeValues: _containers.RepeatedCompositeFieldContainer[_BFPCommonMessage_pb2.ElementNodalValues]
    interfaceNodeValues: _containers.RepeatedCompositeFieldContainer[_BFPCommonMessage_pb2.InterfaceNodalValues]
    def __init__(self, elementNodeValues: _Optional[_Iterable[_Union[_BFPCommonMessage_pb2.ElementNodalValues, _Mapping]]] = ..., interfaceNodeValues: _Optional[_Iterable[_Union[_BFPCommonMessage_pb2.InterfaceNodalValues, _Mapping]]] = ...) -> None: ...

class ElementResults(_message.Message):
    __slots__ = ("pileID", "beamElementID", "interfaceElementID", "nodeIDs", "entityInformation", "nodeValues", "failurePoint", "interfaceFailurePoint")
    PILEID_FIELD_NUMBER: _ClassVar[int]
    BEAMELEMENTID_FIELD_NUMBER: _ClassVar[int]
    INTERFACEELEMENTID_FIELD_NUMBER: _ClassVar[int]
    NODEIDS_FIELD_NUMBER: _ClassVar[int]
    ENTITYINFORMATION_FIELD_NUMBER: _ClassVar[int]
    NODEVALUES_FIELD_NUMBER: _ClassVar[int]
    FAILUREPOINT_FIELD_NUMBER: _ClassVar[int]
    INTERFACEFAILUREPOINT_FIELD_NUMBER: _ClassVar[int]
    pileID: int
    beamElementID: int
    interfaceElementID: int
    nodeIDs: _containers.RepeatedScalarFieldContainer[int]
    entityInformation: _ResultsQueryCommonMessage_pb2.EntityMessage
    nodeValues: NodalValues
    failurePoint: _GaussPointFailureMessage_pb2.GaussPointFailure
    interfaceFailurePoint: _GaussPointFailureMessage_pb2.GaussPointFailure
    def __init__(self, pileID: _Optional[int] = ..., beamElementID: _Optional[int] = ..., interfaceElementID: _Optional[int] = ..., nodeIDs: _Optional[_Iterable[int]] = ..., entityInformation: _Optional[_Union[_ResultsQueryCommonMessage_pb2.EntityMessage, _Mapping]] = ..., nodeValues: _Optional[_Union[NodalValues, _Mapping]] = ..., failurePoint: _Optional[_Union[_GaussPointFailureMessage_pb2.GaussPointFailure, _Mapping]] = ..., interfaceFailurePoint: _Optional[_Union[_GaussPointFailureMessage_pb2.GaussPointFailure, _Mapping]] = ...) -> None: ...

class PileForepoleElementResultsHeader(_message.Message):
    __slots__ = ("totalQueriedElementsCount",)
    TOTALQUERIEDELEMENTSCOUNT_FIELD_NUMBER: _ClassVar[int]
    totalQueriedElementsCount: int
    def __init__(self, totalQueriedElementsCount: _Optional[int] = ...) -> None: ...

class PileForepoleElementResultsData(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ElementResults]
    def __init__(self, results: _Optional[_Iterable[_Union[ElementResults, _Mapping]]] = ...) -> None: ...

class PileForepoleElementResultsResponseChunk(_message.Message):
    __slots__ = ("header", "data")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    header: PileForepoleElementResultsHeader
    data: PileForepoleElementResultsData
    def __init__(self, header: _Optional[_Union[PileForepoleElementResultsHeader, _Mapping]] = ..., data: _Optional[_Union[PileForepoleElementResultsData, _Mapping]] = ...) -> None: ...

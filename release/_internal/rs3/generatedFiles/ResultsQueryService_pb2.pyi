import CommonMessages_pb2 as _CommonMessages_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResultQueryBase(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class ReadAllResultsRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class ReadAllResultsResponse(_message.Message):
    __slots__ = ("resultsAvailable", "failureReason")
    RESULTSAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    FAILUREREASON_FIELD_NUMBER: _ClassVar[int]
    resultsAvailable: bool
    failureReason: str
    def __init__(self, resultsAvailable: bool = ..., failureReason: _Optional[str] = ...) -> None: ...

class ReadResultsByStageSRFRequest(_message.Message):
    __slots__ = ("_projectId", "stageNumber", "srfValueNumber")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    STAGENUMBER_FIELD_NUMBER: _ClassVar[int]
    SRFVALUENUMBER_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    stageNumber: int
    srfValueNumber: int
    def __init__(self, _projectId: _Optional[str] = ..., stageNumber: _Optional[int] = ..., srfValueNumber: _Optional[int] = ...) -> None: ...

class ReadResultsResponse(_message.Message):
    __slots__ = ("resultsAvailable",)
    RESULTSAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    resultsAvailable: bool
    def __init__(self, resultsAvailable: bool = ...) -> None: ...

class NodeInformation(_message.Message):
    __slots__ = ("nodeID", "location")
    NODEID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    nodeID: int
    location: _CommonMessages_pb2.Point3D
    def __init__(self, nodeID: _Optional[int] = ..., location: _Optional[_Union[_CommonMessages_pb2.Point3D, _Mapping]] = ...) -> None: ...

class QueryNodeInformationRequest(_message.Message):
    __slots__ = ("_projectId", "stageNumber")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    STAGENUMBER_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    stageNumber: int
    def __init__(self, _projectId: _Optional[str] = ..., stageNumber: _Optional[int] = ...) -> None: ...

class QueryNodeInformationResponse(_message.Message):
    __slots__ = ("NodesInformation",)
    NODESINFORMATION_FIELD_NUMBER: _ClassVar[int]
    NodesInformation: _containers.RepeatedCompositeFieldContainer[NodeInformation]
    def __init__(self, NodesInformation: _Optional[_Iterable[_Union[NodeInformation, _Mapping]]] = ...) -> None: ...

class ElementInformation(_message.Message):
    __slots__ = ("elementID", "nodeIDs")
    ELEMENTID_FIELD_NUMBER: _ClassVar[int]
    NODEIDS_FIELD_NUMBER: _ClassVar[int]
    elementID: int
    nodeIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, elementID: _Optional[int] = ..., nodeIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class ElementInformationQueryRequest(_message.Message):
    __slots__ = ("_projectId", "stageNumber")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    STAGENUMBER_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    stageNumber: int
    def __init__(self, _projectId: _Optional[str] = ..., stageNumber: _Optional[int] = ...) -> None: ...

class ElementInformationQueryResponse(_message.Message):
    __slots__ = ("ElementsInformation",)
    ELEMENTSINFORMATION_FIELD_NUMBER: _ClassVar[int]
    ElementsInformation: _containers.RepeatedCompositeFieldContainer[ElementInformation]
    def __init__(self, ElementsInformation: _Optional[_Iterable[_Union[ElementInformation, _Mapping]]] = ...) -> None: ...

class PileForepoleElementInformation(_message.Message):
    __slots__ = ("beamElementID", "interfaceElementID", "nodeIDs")
    BEAMELEMENTID_FIELD_NUMBER: _ClassVar[int]
    INTERFACEELEMENTID_FIELD_NUMBER: _ClassVar[int]
    NODEIDS_FIELD_NUMBER: _ClassVar[int]
    beamElementID: int
    interfaceElementID: int
    nodeIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, beamElementID: _Optional[int] = ..., interfaceElementID: _Optional[int] = ..., nodeIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class PileForepoleElementInformationQueryResponse(_message.Message):
    __slots__ = ("ElementsInformation",)
    ELEMENTSINFORMATION_FIELD_NUMBER: _ClassVar[int]
    ElementsInformation: _containers.RepeatedCompositeFieldContainer[PileForepoleElementInformation]
    def __init__(self, ElementsInformation: _Optional[_Iterable[_Union[PileForepoleElementInformation, _Mapping]]] = ...) -> None: ...

class SRFValueInformation(_message.Message):
    __slots__ = ("srf", "maxTotalDisplacement", "converged")
    SRF_FIELD_NUMBER: _ClassVar[int]
    MAXTOTALDISPLACEMENT_FIELD_NUMBER: _ClassVar[int]
    CONVERGED_FIELD_NUMBER: _ClassVar[int]
    srf: float
    maxTotalDisplacement: float
    converged: bool
    def __init__(self, srf: _Optional[float] = ..., maxTotalDisplacement: _Optional[float] = ..., converged: bool = ...) -> None: ...

class SRFValuesQueryRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class SRFValuesQueryResponse(_message.Message):
    __slots__ = ("srfValues",)
    SRFVALUES_FIELD_NUMBER: _ClassVar[int]
    srfValues: _containers.RepeatedCompositeFieldContainer[SRFValueInformation]
    def __init__(self, srfValues: _Optional[_Iterable[_Union[SRFValueInformation, _Mapping]]] = ...) -> None: ...

class QueryNodeInformationHeader(_message.Message):
    __slots__ = ("totalNodesCount",)
    TOTALNODESCOUNT_FIELD_NUMBER: _ClassVar[int]
    totalNodesCount: int
    def __init__(self, totalNodesCount: _Optional[int] = ...) -> None: ...

class QueryNodeInformationData(_message.Message):
    __slots__ = ("NodesInformation",)
    NODESINFORMATION_FIELD_NUMBER: _ClassVar[int]
    NodesInformation: _containers.RepeatedCompositeFieldContainer[NodeInformation]
    def __init__(self, NodesInformation: _Optional[_Iterable[_Union[NodeInformation, _Mapping]]] = ...) -> None: ...

class QueryNodeInformationResponseChunk(_message.Message):
    __slots__ = ("header", "data")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    header: QueryNodeInformationHeader
    data: QueryNodeInformationData
    def __init__(self, header: _Optional[_Union[QueryNodeInformationHeader, _Mapping]] = ..., data: _Optional[_Union[QueryNodeInformationData, _Mapping]] = ...) -> None: ...

class ElementInformationHeader(_message.Message):
    __slots__ = ("totalElementsCount",)
    TOTALELEMENTSCOUNT_FIELD_NUMBER: _ClassVar[int]
    totalElementsCount: int
    def __init__(self, totalElementsCount: _Optional[int] = ...) -> None: ...

class ElementInformationData(_message.Message):
    __slots__ = ("ElementsInformation",)
    ELEMENTSINFORMATION_FIELD_NUMBER: _ClassVar[int]
    ElementsInformation: _containers.RepeatedCompositeFieldContainer[ElementInformation]
    def __init__(self, ElementsInformation: _Optional[_Iterable[_Union[ElementInformation, _Mapping]]] = ...) -> None: ...

class ElementInformationResponseChunk(_message.Message):
    __slots__ = ("header", "data")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    header: ElementInformationHeader
    data: ElementInformationData
    def __init__(self, header: _Optional[_Union[ElementInformationHeader, _Mapping]] = ..., data: _Optional[_Union[ElementInformationData, _Mapping]] = ...) -> None: ...

class PileForepoleElementInformationHeader(_message.Message):
    __slots__ = ("totalElementsCount",)
    TOTALELEMENTSCOUNT_FIELD_NUMBER: _ClassVar[int]
    totalElementsCount: int
    def __init__(self, totalElementsCount: _Optional[int] = ...) -> None: ...

class PileForepoleElementInformationData(_message.Message):
    __slots__ = ("ElementsInformation",)
    ELEMENTSINFORMATION_FIELD_NUMBER: _ClassVar[int]
    ElementsInformation: _containers.RepeatedCompositeFieldContainer[PileForepoleElementInformation]
    def __init__(self, ElementsInformation: _Optional[_Iterable[_Union[PileForepoleElementInformation, _Mapping]]] = ...) -> None: ...

class PileForepoleElementInformationResponseChunk(_message.Message):
    __slots__ = ("header", "data")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    header: PileForepoleElementInformationHeader
    data: PileForepoleElementInformationData
    def __init__(self, header: _Optional[_Union[PileForepoleElementInformationHeader, _Mapping]] = ..., data: _Optional[_Union[PileForepoleElementInformationData, _Mapping]] = ...) -> None: ...

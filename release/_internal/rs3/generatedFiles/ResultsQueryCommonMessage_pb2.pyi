import CommonMessages_pb2 as _CommonMessages_pb2
import CommonGeometryMessages_pb2 as _CommonGeometryMessages_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntityMessage(_message.Message):
    __slots__ = ("name", "ID")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    ID: str
    def __init__(self, name: _Optional[str] = ..., ID: _Optional[str] = ...) -> None: ...

class ResultsQueryRequest(_message.Message):
    __slots__ = ("_projectId", "stageNumber", "srfValueNumber", "entityName", "sampleRegion")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    STAGENUMBER_FIELD_NUMBER: _ClassVar[int]
    SRFVALUENUMBER_FIELD_NUMBER: _ClassVar[int]
    ENTITYNAME_FIELD_NUMBER: _ClassVar[int]
    SAMPLEREGION_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    stageNumber: int
    srfValueNumber: int
    entityName: str
    sampleRegion: _CommonGeometryMessages_pb2.RegionSelectionSetting
    def __init__(self, _projectId: _Optional[str] = ..., stageNumber: _Optional[int] = ..., srfValueNumber: _Optional[int] = ..., entityName: _Optional[str] = ..., sampleRegion: _Optional[_Union[_CommonGeometryMessages_pb2.RegionSelectionSetting, _Mapping]] = ...) -> None: ...

class NodeInformation(_message.Message):
    __slots__ = ("nodeID", "location")
    NODEID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    nodeID: int
    location: _CommonMessages_pb2.Point3D
    def __init__(self, nodeID: _Optional[int] = ..., location: _Optional[_Union[_CommonMessages_pb2.Point3D, _Mapping]] = ...) -> None: ...

class StructuralNodeResults(_message.Message):
    __slots__ = ("nodeInformation", "entityInformation", "indexToPattern")
    NODEINFORMATION_FIELD_NUMBER: _ClassVar[int]
    ENTITYINFORMATION_FIELD_NUMBER: _ClassVar[int]
    INDEXTOPATTERN_FIELD_NUMBER: _ClassVar[int]
    nodeInformation: NodeInformation
    entityInformation: EntityMessage
    indexToPattern: int
    def __init__(self, nodeInformation: _Optional[_Union[NodeInformation, _Mapping]] = ..., entityInformation: _Optional[_Union[EntityMessage, _Mapping]] = ..., indexToPattern: _Optional[int] = ...) -> None: ...

class StructuralNodeResultsHeader(_message.Message):
    __slots__ = ("totalQueriedNodesCount",)
    TOTALQUERIEDNODESCOUNT_FIELD_NUMBER: _ClassVar[int]
    totalQueriedNodesCount: int
    def __init__(self, totalQueriedNodesCount: _Optional[int] = ...) -> None: ...

class StructuralNodeResultsData(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[StructuralNodeResults]
    def __init__(self, results: _Optional[_Iterable[_Union[StructuralNodeResults, _Mapping]]] = ...) -> None: ...

class StructuralNodeResultsResponseChunk(_message.Message):
    __slots__ = ("header", "data")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    header: StructuralNodeResultsHeader
    data: StructuralNodeResultsData
    def __init__(self, header: _Optional[_Union[StructuralNodeResultsHeader, _Mapping]] = ..., data: _Optional[_Union[StructuralNodeResultsData, _Mapping]] = ...) -> None: ...

class StructuralElementResultsHeader(_message.Message):
    __slots__ = ("hasUserData", "userDataNameToResultIndexMap", "totalQueriedElementsCount")
    class UserDataNameToResultIndexMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    HASUSERDATA_FIELD_NUMBER: _ClassVar[int]
    USERDATANAMETORESULTINDEXMAP_FIELD_NUMBER: _ClassVar[int]
    TOTALQUERIEDELEMENTSCOUNT_FIELD_NUMBER: _ClassVar[int]
    hasUserData: bool
    userDataNameToResultIndexMap: _containers.ScalarMap[str, int]
    totalQueriedElementsCount: int
    def __init__(self, hasUserData: bool = ..., userDataNameToResultIndexMap: _Optional[_Mapping[str, int]] = ..., totalQueriedElementsCount: _Optional[int] = ...) -> None: ...

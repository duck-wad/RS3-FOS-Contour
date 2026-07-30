import ResultsQueryService_pb2 as _ResultsQueryService_pb2
import CommonMessages_pb2 as _CommonMessages_pb2
import CommonGeometryMessages_pb2 as _CommonGeometryMessages_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SolidResultQueryBase(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class SolidResultsQueryRequest(_message.Message):
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

class NodalValues(_message.Message):
    __slots__ = ("displacementX", "displacementY", "displacementZ", "excessPWP", "totalPWP")
    DISPLACEMENTX_FIELD_NUMBER: _ClassVar[int]
    DISPLACEMENTY_FIELD_NUMBER: _ClassVar[int]
    DISPLACEMENTZ_FIELD_NUMBER: _ClassVar[int]
    EXCESSPWP_FIELD_NUMBER: _ClassVar[int]
    TOTALPWP_FIELD_NUMBER: _ClassVar[int]
    displacementX: float
    displacementY: float
    displacementZ: float
    excessPWP: float
    totalPWP: float
    def __init__(self, displacementX: _Optional[float] = ..., displacementY: _Optional[float] = ..., displacementZ: _Optional[float] = ..., excessPWP: _Optional[float] = ..., totalPWP: _Optional[float] = ...) -> None: ...

class MaterialResults(_message.Message):
    __slots__ = ("materialID", "materialName", "dataTypeValues")
    MATERIALID_FIELD_NUMBER: _ClassVar[int]
    MATERIALNAME_FIELD_NUMBER: _ClassVar[int]
    DATATYPEVALUES_FIELD_NUMBER: _ClassVar[int]
    materialID: str
    materialName: str
    dataTypeValues: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, materialID: _Optional[str] = ..., materialName: _Optional[str] = ..., dataTypeValues: _Optional[_Iterable[float]] = ...) -> None: ...

class NodalResults(_message.Message):
    __slots__ = ("nodeInformation", "entityNames", "entityIDs", "nodalValues", "materialValues")
    NODEINFORMATION_FIELD_NUMBER: _ClassVar[int]
    ENTITYNAMES_FIELD_NUMBER: _ClassVar[int]
    ENTITYIDS_FIELD_NUMBER: _ClassVar[int]
    NODALVALUES_FIELD_NUMBER: _ClassVar[int]
    MATERIALVALUES_FIELD_NUMBER: _ClassVar[int]
    nodeInformation: _ResultsQueryService_pb2.NodeInformation
    entityNames: _containers.RepeatedScalarFieldContainer[str]
    entityIDs: _containers.RepeatedScalarFieldContainer[str]
    nodalValues: NodalValues
    materialValues: _containers.RepeatedCompositeFieldContainer[MaterialResults]
    def __init__(self, nodeInformation: _Optional[_Union[_ResultsQueryService_pb2.NodeInformation, _Mapping]] = ..., entityNames: _Optional[_Iterable[str]] = ..., entityIDs: _Optional[_Iterable[str]] = ..., nodalValues: _Optional[_Union[NodalValues, _Mapping]] = ..., materialValues: _Optional[_Iterable[_Union[MaterialResults, _Mapping]]] = ...) -> None: ...

class SolidNodalResultsQueryRequest(_message.Message):
    __slots__ = ("baseRequest", "requiredDataTypes")
    BASEREQUEST_FIELD_NUMBER: _ClassVar[int]
    REQUIREDDATATYPES_FIELD_NUMBER: _ClassVar[int]
    baseRequest: SolidResultsQueryRequest
    requiredDataTypes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, baseRequest: _Optional[_Union[SolidResultsQueryRequest, _Mapping]] = ..., requiredDataTypes: _Optional[_Iterable[str]] = ...) -> None: ...

class SolidNodalResultsQueryResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[NodalResults]
    def __init__(self, results: _Optional[_Iterable[_Union[NodalResults, _Mapping]]] = ...) -> None: ...

class SolidNodalResultsHeader(_message.Message):
    __slots__ = ("totalQueriedNodesCount", "dataTypeNameToIndexMap")
    class DataTypeNameToIndexMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    TOTALQUERIEDNODESCOUNT_FIELD_NUMBER: _ClassVar[int]
    DATATYPENAMETOINDEXMAP_FIELD_NUMBER: _ClassVar[int]
    totalQueriedNodesCount: int
    dataTypeNameToIndexMap: _containers.ScalarMap[str, int]
    def __init__(self, totalQueriedNodesCount: _Optional[int] = ..., dataTypeNameToIndexMap: _Optional[_Mapping[str, int]] = ...) -> None: ...

class SolidNodalResultsData(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[NodalResults]
    def __init__(self, results: _Optional[_Iterable[_Union[NodalResults, _Mapping]]] = ...) -> None: ...

class SolidNodalResultsResponseChunk(_message.Message):
    __slots__ = ("header", "data")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    header: SolidNodalResultsHeader
    data: SolidNodalResultsData
    def __init__(self, header: _Optional[_Union[SolidNodalResultsHeader, _Mapping]] = ..., data: _Optional[_Union[SolidNodalResultsData, _Mapping]] = ...) -> None: ...

class UserDataResults(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, values: _Optional[_Iterable[float]] = ...) -> None: ...

class FailurePoint(_message.Message):
    __slots__ = ("location", "failureTypes")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    FAILURETYPES_FIELD_NUMBER: _ClassVar[int]
    location: _CommonMessages_pb2.Point3D
    failureTypes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, location: _Optional[_Union[_CommonMessages_pb2.Point3D, _Mapping]] = ..., failureTypes: _Optional[_Iterable[str]] = ...) -> None: ...

class ElementResults(_message.Message):
    __slots__ = ("elementInformation", "entityName", "entityID", "yieldPercent", "failurePoints", "nodedUserDataResults")
    class NodedUserDataResultsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: UserDataResults
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[UserDataResults, _Mapping]] = ...) -> None: ...
    ELEMENTINFORMATION_FIELD_NUMBER: _ClassVar[int]
    ENTITYNAME_FIELD_NUMBER: _ClassVar[int]
    ENTITYID_FIELD_NUMBER: _ClassVar[int]
    YIELDPERCENT_FIELD_NUMBER: _ClassVar[int]
    FAILUREPOINTS_FIELD_NUMBER: _ClassVar[int]
    NODEDUSERDATARESULTS_FIELD_NUMBER: _ClassVar[int]
    elementInformation: _ResultsQueryService_pb2.ElementInformation
    entityName: str
    entityID: str
    yieldPercent: float
    failurePoints: _containers.RepeatedCompositeFieldContainer[FailurePoint]
    nodedUserDataResults: _containers.MessageMap[int, UserDataResults]
    def __init__(self, elementInformation: _Optional[_Union[_ResultsQueryService_pb2.ElementInformation, _Mapping]] = ..., entityName: _Optional[str] = ..., entityID: _Optional[str] = ..., yieldPercent: _Optional[float] = ..., failurePoints: _Optional[_Iterable[_Union[FailurePoint, _Mapping]]] = ..., nodedUserDataResults: _Optional[_Mapping[int, UserDataResults]] = ...) -> None: ...

class SolidElementResultsQueryResponse(_message.Message):
    __slots__ = ("hasUserData", "userDataNameToResultIndexMap", "results")
    class UserDataNameToResultIndexMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    HASUSERDATA_FIELD_NUMBER: _ClassVar[int]
    USERDATANAMETORESULTINDEXMAP_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    hasUserData: bool
    userDataNameToResultIndexMap: _containers.ScalarMap[str, int]
    results: _containers.RepeatedCompositeFieldContainer[ElementResults]
    def __init__(self, hasUserData: bool = ..., userDataNameToResultIndexMap: _Optional[_Mapping[str, int]] = ..., results: _Optional[_Iterable[_Union[ElementResults, _Mapping]]] = ...) -> None: ...

class SolidElementResultsHeader(_message.Message):
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

class SolidElementResultsData(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ElementResults]
    def __init__(self, results: _Optional[_Iterable[_Union[ElementResults, _Mapping]]] = ...) -> None: ...

class SolidElementResultsResponseChunk(_message.Message):
    __slots__ = ("header", "data")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    header: SolidElementResultsHeader
    data: SolidElementResultsData
    def __init__(self, header: _Optional[_Union[SolidElementResultsHeader, _Mapping]] = ..., data: _Optional[_Union[SolidElementResultsData, _Mapping]] = ...) -> None: ...

class SolidResultsByDataTypesQueryRequest(_message.Message):
    __slots__ = ("_projectId", "stageNumber", "srfValueNumber", "requiredDataTypes")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    STAGENUMBER_FIELD_NUMBER: _ClassVar[int]
    SRFVALUENUMBER_FIELD_NUMBER: _ClassVar[int]
    REQUIREDDATATYPES_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    stageNumber: int
    srfValueNumber: int
    requiredDataTypes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, _projectId: _Optional[str] = ..., stageNumber: _Optional[int] = ..., srfValueNumber: _Optional[int] = ..., requiredDataTypes: _Optional[_Iterable[str]] = ...) -> None: ...

class SolidResultsByDataTypesQueryResponse(_message.Message):
    __slots__ = ("resultsAvailable",)
    RESULTSAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    resultsAvailable: bool
    def __init__(self, resultsAvailable: bool = ...) -> None: ...

import ResultsQueryService_pb2 as _ResultsQueryService_pb2
import ResultsQueryCommonMessage_pb2 as _ResultsQueryCommonMessage_pb2
import JointResultsQueryService_pb2 as _JointResultsQueryService_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LinerNodalResultsQueryResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[LinerNodalResults]
    def __init__(self, results: _Optional[_Iterable[_Union[LinerNodalResults, _Mapping]]] = ...) -> None: ...

class LinerNodalResults(_message.Message):
    __slots__ = ("entityInformation", "compositeLinerStructureInformation", "nodeInformation")
    ENTITYINFORMATION_FIELD_NUMBER: _ClassVar[int]
    COMPOSITELINERSTRUCTUREINFORMATION_FIELD_NUMBER: _ClassVar[int]
    NODEINFORMATION_FIELD_NUMBER: _ClassVar[int]
    entityInformation: _ResultsQueryCommonMessage_pb2.EntityMessage
    compositeLinerStructureInformation: CompositeLinerStructureInformation
    nodeInformation: _ResultsQueryService_pb2.NodeInformation
    def __init__(self, entityInformation: _Optional[_Union[_ResultsQueryCommonMessage_pb2.EntityMessage, _Mapping]] = ..., compositeLinerStructureInformation: _Optional[_Union[CompositeLinerStructureInformation, _Mapping]] = ..., nodeInformation: _Optional[_Union[_ResultsQueryService_pb2.NodeInformation, _Mapping]] = ...) -> None: ...

class CompositeLinerStructureInformation(_message.Message):
    __slots__ = ("layerIndex", "assignedPropertyName", "attachedLinerLayerUpperIndex", "attachedLinerLayerLowerIndex", "attachedInterfaceLayerUpperIndex", "attachedInterfaceLayerLowerIndex")
    LAYERINDEX_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEDPROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    ATTACHEDLINERLAYERUPPERINDEX_FIELD_NUMBER: _ClassVar[int]
    ATTACHEDLINERLAYERLOWERINDEX_FIELD_NUMBER: _ClassVar[int]
    ATTACHEDINTERFACELAYERUPPERINDEX_FIELD_NUMBER: _ClassVar[int]
    ATTACHEDINTERFACELAYERLOWERINDEX_FIELD_NUMBER: _ClassVar[int]
    layerIndex: int
    assignedPropertyName: str
    attachedLinerLayerUpperIndex: _containers.RepeatedScalarFieldContainer[int]
    attachedLinerLayerLowerIndex: _containers.RepeatedScalarFieldContainer[int]
    attachedInterfaceLayerUpperIndex: int
    attachedInterfaceLayerLowerIndex: int
    def __init__(self, layerIndex: _Optional[int] = ..., assignedPropertyName: _Optional[str] = ..., attachedLinerLayerUpperIndex: _Optional[_Iterable[int]] = ..., attachedLinerLayerLowerIndex: _Optional[_Iterable[int]] = ..., attachedInterfaceLayerUpperIndex: _Optional[int] = ..., attachedInterfaceLayerLowerIndex: _Optional[int] = ...) -> None: ...

class LinerResults(_message.Message):
    __slots__ = ("DISPLACEMENT_X", "DISPLACEMENT_Y", "DISPLACEMENT_Z", "TOTAL_DISPLACEMENT", "NORMAL_DISPLACEMENT", "AXIAL_FORCE_XX", "AXIAL_FORCE_YY", "AXIAL_FORCE_ZZ", "SHEAR_FORCE_YZ", "SHEAR_FORCE_XZ", "SHEAR_FORCE_XY", "MOMENT_XX", "MOMENT_YY", "MOMENT_ZZ", "MOMENT_YZ", "MOMENT_XZ", "MOMENT_XY")
    DISPLACEMENT_X_FIELD_NUMBER: _ClassVar[int]
    DISPLACEMENT_Y_FIELD_NUMBER: _ClassVar[int]
    DISPLACEMENT_Z_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DISPLACEMENT_FIELD_NUMBER: _ClassVar[int]
    NORMAL_DISPLACEMENT_FIELD_NUMBER: _ClassVar[int]
    AXIAL_FORCE_XX_FIELD_NUMBER: _ClassVar[int]
    AXIAL_FORCE_YY_FIELD_NUMBER: _ClassVar[int]
    AXIAL_FORCE_ZZ_FIELD_NUMBER: _ClassVar[int]
    SHEAR_FORCE_YZ_FIELD_NUMBER: _ClassVar[int]
    SHEAR_FORCE_XZ_FIELD_NUMBER: _ClassVar[int]
    SHEAR_FORCE_XY_FIELD_NUMBER: _ClassVar[int]
    MOMENT_XX_FIELD_NUMBER: _ClassVar[int]
    MOMENT_YY_FIELD_NUMBER: _ClassVar[int]
    MOMENT_ZZ_FIELD_NUMBER: _ClassVar[int]
    MOMENT_YZ_FIELD_NUMBER: _ClassVar[int]
    MOMENT_XZ_FIELD_NUMBER: _ClassVar[int]
    MOMENT_XY_FIELD_NUMBER: _ClassVar[int]
    DISPLACEMENT_X: _containers.RepeatedScalarFieldContainer[float]
    DISPLACEMENT_Y: _containers.RepeatedScalarFieldContainer[float]
    DISPLACEMENT_Z: _containers.RepeatedScalarFieldContainer[float]
    TOTAL_DISPLACEMENT: _containers.RepeatedScalarFieldContainer[float]
    NORMAL_DISPLACEMENT: _containers.RepeatedScalarFieldContainer[float]
    AXIAL_FORCE_XX: _containers.RepeatedScalarFieldContainer[float]
    AXIAL_FORCE_YY: _containers.RepeatedScalarFieldContainer[float]
    AXIAL_FORCE_ZZ: _containers.RepeatedScalarFieldContainer[float]
    SHEAR_FORCE_YZ: _containers.RepeatedScalarFieldContainer[float]
    SHEAR_FORCE_XZ: _containers.RepeatedScalarFieldContainer[float]
    SHEAR_FORCE_XY: _containers.RepeatedScalarFieldContainer[float]
    MOMENT_XX: _containers.RepeatedScalarFieldContainer[float]
    MOMENT_YY: _containers.RepeatedScalarFieldContainer[float]
    MOMENT_ZZ: _containers.RepeatedScalarFieldContainer[float]
    MOMENT_YZ: _containers.RepeatedScalarFieldContainer[float]
    MOMENT_XZ: _containers.RepeatedScalarFieldContainer[float]
    MOMENT_XY: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, DISPLACEMENT_X: _Optional[_Iterable[float]] = ..., DISPLACEMENT_Y: _Optional[_Iterable[float]] = ..., DISPLACEMENT_Z: _Optional[_Iterable[float]] = ..., TOTAL_DISPLACEMENT: _Optional[_Iterable[float]] = ..., NORMAL_DISPLACEMENT: _Optional[_Iterable[float]] = ..., AXIAL_FORCE_XX: _Optional[_Iterable[float]] = ..., AXIAL_FORCE_YY: _Optional[_Iterable[float]] = ..., AXIAL_FORCE_ZZ: _Optional[_Iterable[float]] = ..., SHEAR_FORCE_YZ: _Optional[_Iterable[float]] = ..., SHEAR_FORCE_XZ: _Optional[_Iterable[float]] = ..., SHEAR_FORCE_XY: _Optional[_Iterable[float]] = ..., MOMENT_XX: _Optional[_Iterable[float]] = ..., MOMENT_YY: _Optional[_Iterable[float]] = ..., MOMENT_ZZ: _Optional[_Iterable[float]] = ..., MOMENT_YZ: _Optional[_Iterable[float]] = ..., MOMENT_XZ: _Optional[_Iterable[float]] = ..., MOMENT_XY: _Optional[_Iterable[float]] = ...) -> None: ...

class LinerElementResultsQueryResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[LinerElementResults]
    def __init__(self, results: _Optional[_Iterable[_Union[LinerElementResults, _Mapping]]] = ...) -> None: ...

class LinerElementResults(_message.Message):
    __slots__ = ("entityInformation", "compositeLinerStructureInformation", "elementInformation", "failureType", "linerNodalResults")
    ENTITYINFORMATION_FIELD_NUMBER: _ClassVar[int]
    COMPOSITELINERSTRUCTUREINFORMATION_FIELD_NUMBER: _ClassVar[int]
    ELEMENTINFORMATION_FIELD_NUMBER: _ClassVar[int]
    FAILURETYPE_FIELD_NUMBER: _ClassVar[int]
    LINERNODALRESULTS_FIELD_NUMBER: _ClassVar[int]
    entityInformation: _ResultsQueryCommonMessage_pb2.EntityMessage
    compositeLinerStructureInformation: CompositeLinerStructureInformation
    elementInformation: _ResultsQueryService_pb2.ElementInformation
    failureType: str
    linerNodalResults: _containers.RepeatedCompositeFieldContainer[LinerResults]
    def __init__(self, entityInformation: _Optional[_Union[_ResultsQueryCommonMessage_pb2.EntityMessage, _Mapping]] = ..., compositeLinerStructureInformation: _Optional[_Union[CompositeLinerStructureInformation, _Mapping]] = ..., elementInformation: _Optional[_Union[_ResultsQueryService_pb2.ElementInformation, _Mapping]] = ..., failureType: _Optional[str] = ..., linerNodalResults: _Optional[_Iterable[_Union[LinerResults, _Mapping]]] = ...) -> None: ...

class SetCoordinateSystemRequest(_message.Message):
    __slots__ = ("_projectId", "coordinateSystemName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    COORDINATESYSTEMNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    coordinateSystemName: str
    def __init__(self, _projectId: _Optional[str] = ..., coordinateSystemName: _Optional[str] = ...) -> None: ...

class SetCoordinateSystemResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCoordinateSystemRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class GetCoordinateSystemResponse(_message.Message):
    __slots__ = ("coordinateSystemName",)
    COORDINATESYSTEMNAME_FIELD_NUMBER: _ClassVar[int]
    coordinateSystemName: str
    def __init__(self, coordinateSystemName: _Optional[str] = ...) -> None: ...

class LinerNodalResultsResponseChunk(_message.Message):
    __slots__ = ("header", "data")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    header: _ResultsQueryCommonMessage_pb2.StructuralNodeResultsHeader
    data: LinerNodalResultsQueryResponse
    def __init__(self, header: _Optional[_Union[_ResultsQueryCommonMessage_pb2.StructuralNodeResultsHeader, _Mapping]] = ..., data: _Optional[_Union[LinerNodalResultsQueryResponse, _Mapping]] = ...) -> None: ...

class LinerElementResultsResponseChunk(_message.Message):
    __slots__ = ("header", "data")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    header: _ResultsQueryCommonMessage_pb2.StructuralElementResultsHeader
    data: LinerElementResultsQueryResponse
    def __init__(self, header: _Optional[_Union[_ResultsQueryCommonMessage_pb2.StructuralElementResultsHeader, _Mapping]] = ..., data: _Optional[_Union[LinerElementResultsQueryResponse, _Mapping]] = ...) -> None: ...

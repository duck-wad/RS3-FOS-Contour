import ResultsQueryService_pb2 as _ResultsQueryService_pb2
import ResultsQueryCommonMessage_pb2 as _ResultsQueryCommonMessage_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JointNodalResultsQueryResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[JointNodalResults]
    def __init__(self, results: _Optional[_Iterable[_Union[JointNodalResults, _Mapping]]] = ...) -> None: ...

class JointNodalResults(_message.Message):
    __slots__ = ("entityInformation", "nodeInformation", "compositeLinerLinerAttachmentInformation")
    ENTITYINFORMATION_FIELD_NUMBER: _ClassVar[int]
    NODEINFORMATION_FIELD_NUMBER: _ClassVar[int]
    COMPOSITELINERLINERATTACHMENTINFORMATION_FIELD_NUMBER: _ClassVar[int]
    entityInformation: _ResultsQueryCommonMessage_pb2.EntityMessage
    nodeInformation: _ResultsQueryService_pb2.NodeInformation
    compositeLinerLinerAttachmentInformation: CompositeLinerLinerAttachmentInformation
    def __init__(self, entityInformation: _Optional[_Union[_ResultsQueryCommonMessage_pb2.EntityMessage, _Mapping]] = ..., nodeInformation: _Optional[_Union[_ResultsQueryService_pb2.NodeInformation, _Mapping]] = ..., compositeLinerLinerAttachmentInformation: _Optional[_Union[CompositeLinerLinerAttachmentInformation, _Mapping]] = ...) -> None: ...

class CompositeLinerLinerAttachmentInformation(_message.Message):
    __slots__ = ("layerIndex", "assignedPropertyName", "attachedLinerLayerUpperIndex", "attachedLinerLayerLowerIndex")
    LAYERINDEX_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEDPROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    ATTACHEDLINERLAYERUPPERINDEX_FIELD_NUMBER: _ClassVar[int]
    ATTACHEDLINERLAYERLOWERINDEX_FIELD_NUMBER: _ClassVar[int]
    layerIndex: int
    assignedPropertyName: str
    attachedLinerLayerUpperIndex: _containers.RepeatedScalarFieldContainer[int]
    attachedLinerLayerLowerIndex: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, layerIndex: _Optional[int] = ..., assignedPropertyName: _Optional[str] = ..., attachedLinerLayerUpperIndex: _Optional[_Iterable[int]] = ..., attachedLinerLayerLowerIndex: _Optional[_Iterable[int]] = ...) -> None: ...

class JointResults(_message.Message):
    __slots__ = ("DISPLACEMENT_X", "DISPLACEMENT_Y", "DISPLACEMENT_Z", "NORMAL_STRESS", "SHEAR_STRESS", "PLASTIC_STRAIN", "DISPLACEMENT_NORMAL", "DISPLACEMENT_SHEAR")
    DISPLACEMENT_X_FIELD_NUMBER: _ClassVar[int]
    DISPLACEMENT_Y_FIELD_NUMBER: _ClassVar[int]
    DISPLACEMENT_Z_FIELD_NUMBER: _ClassVar[int]
    NORMAL_STRESS_FIELD_NUMBER: _ClassVar[int]
    SHEAR_STRESS_FIELD_NUMBER: _ClassVar[int]
    PLASTIC_STRAIN_FIELD_NUMBER: _ClassVar[int]
    DISPLACEMENT_NORMAL_FIELD_NUMBER: _ClassVar[int]
    DISPLACEMENT_SHEAR_FIELD_NUMBER: _ClassVar[int]
    DISPLACEMENT_X: _containers.RepeatedScalarFieldContainer[float]
    DISPLACEMENT_Y: _containers.RepeatedScalarFieldContainer[float]
    DISPLACEMENT_Z: _containers.RepeatedScalarFieldContainer[float]
    NORMAL_STRESS: _containers.RepeatedScalarFieldContainer[float]
    SHEAR_STRESS: _containers.RepeatedScalarFieldContainer[float]
    PLASTIC_STRAIN: _containers.RepeatedScalarFieldContainer[float]
    DISPLACEMENT_NORMAL: _containers.RepeatedScalarFieldContainer[float]
    DISPLACEMENT_SHEAR: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, DISPLACEMENT_X: _Optional[_Iterable[float]] = ..., DISPLACEMENT_Y: _Optional[_Iterable[float]] = ..., DISPLACEMENT_Z: _Optional[_Iterable[float]] = ..., NORMAL_STRESS: _Optional[_Iterable[float]] = ..., SHEAR_STRESS: _Optional[_Iterable[float]] = ..., PLASTIC_STRAIN: _Optional[_Iterable[float]] = ..., DISPLACEMENT_NORMAL: _Optional[_Iterable[float]] = ..., DISPLACEMENT_SHEAR: _Optional[_Iterable[float]] = ...) -> None: ...

class JointElementResultsQueryResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[JointElementResults]
    def __init__(self, results: _Optional[_Iterable[_Union[JointElementResults, _Mapping]]] = ...) -> None: ...

class JointElementResults(_message.Message):
    __slots__ = ("entityInformation", "elementInformation", "failureType", "jointNodalResults", "compositeLinerLinerAttachmentInformation")
    ENTITYINFORMATION_FIELD_NUMBER: _ClassVar[int]
    ELEMENTINFORMATION_FIELD_NUMBER: _ClassVar[int]
    FAILURETYPE_FIELD_NUMBER: _ClassVar[int]
    JOINTNODALRESULTS_FIELD_NUMBER: _ClassVar[int]
    COMPOSITELINERLINERATTACHMENTINFORMATION_FIELD_NUMBER: _ClassVar[int]
    entityInformation: _ResultsQueryCommonMessage_pb2.EntityMessage
    elementInformation: _ResultsQueryService_pb2.ElementInformation
    failureType: str
    jointNodalResults: _containers.RepeatedCompositeFieldContainer[JointResults]
    compositeLinerLinerAttachmentInformation: CompositeLinerLinerAttachmentInformation
    def __init__(self, entityInformation: _Optional[_Union[_ResultsQueryCommonMessage_pb2.EntityMessage, _Mapping]] = ..., elementInformation: _Optional[_Union[_ResultsQueryService_pb2.ElementInformation, _Mapping]] = ..., failureType: _Optional[str] = ..., jointNodalResults: _Optional[_Iterable[_Union[JointResults, _Mapping]]] = ..., compositeLinerLinerAttachmentInformation: _Optional[_Union[CompositeLinerLinerAttachmentInformation, _Mapping]] = ...) -> None: ...

class JointNodalResultsResponseChunk(_message.Message):
    __slots__ = ("header", "data")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    header: _ResultsQueryCommonMessage_pb2.StructuralNodeResultsHeader
    data: JointNodalResultsQueryResponse
    def __init__(self, header: _Optional[_Union[_ResultsQueryCommonMessage_pb2.StructuralNodeResultsHeader, _Mapping]] = ..., data: _Optional[_Union[JointNodalResultsQueryResponse, _Mapping]] = ...) -> None: ...

class JointElementResultsResponseChunk(_message.Message):
    __slots__ = ("header", "data")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    header: _ResultsQueryCommonMessage_pb2.StructuralElementResultsHeader
    data: JointElementResultsQueryResponse
    def __init__(self, header: _Optional[_Union[_ResultsQueryCommonMessage_pb2.StructuralElementResultsHeader, _Mapping]] = ..., data: _Optional[_Union[JointElementResultsQueryResponse, _Mapping]] = ...) -> None: ...

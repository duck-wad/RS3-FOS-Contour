from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ModelBase(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class saveRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class saveResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class saveAsRequest(_message.Message):
    __slots__ = ("_projectId", "newLocation")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    NEWLOCATION_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    newLocation: str
    def __init__(self, _projectId: _Optional[str] = ..., newLocation: _Optional[str] = ...) -> None: ...

class saveAsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class closeRequest(_message.Message):
    __slots__ = ("_projectId", "saveProject")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    SAVEPROJECT_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    saveProject: bool
    def __init__(self, _projectId: _Optional[str] = ..., saveProject: bool = ...) -> None: ...

class closeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class saveComputeFileRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class saveComputeFileResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class setActiveStageByNameRequest(_message.Message):
    __slots__ = ("_projectId", "stageName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    STAGENAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    stageName: str
    def __init__(self, _projectId: _Optional[str] = ..., stageName: _Optional[str] = ...) -> None: ...

class setActiveStageByNameResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class getActiveStageNameRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class getActiveStageNameResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class setActiveStageRequest(_message.Message):
    __slots__ = ("_projectId", "stageNum")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    STAGENUM_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    stageNum: int
    def __init__(self, _projectId: _Optional[str] = ..., stageNum: _Optional[int] = ...) -> None: ...

class setActiveStageResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class getActiveStageRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class getActiveStageResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: int
    def __init__(self, result: _Optional[int] = ...) -> None: ...

class getBoltPropertyByNameRequest(_message.Message):
    __slots__ = ("_projectId", "boltName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    BOLTNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    boltName: str
    def __init__(self, _projectId: _Optional[str] = ..., boltName: _Optional[str] = ...) -> None: ...

class getBoltPropertyByNameResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class getBeamPropertyByNameRequest(_message.Message):
    __slots__ = ("_projectId", "beamName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    BEAMNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    beamName: str
    def __init__(self, _projectId: _Optional[str] = ..., beamName: _Optional[str] = ...) -> None: ...

class getBeamPropertyByNameResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class getLinerPropertyByNameRequest(_message.Message):
    __slots__ = ("_projectId", "linerName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    LINERNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    linerName: str
    def __init__(self, _projectId: _Optional[str] = ..., linerName: _Optional[str] = ...) -> None: ...

class getLinerPropertyByNameResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class getJointPropertyByNameRequest(_message.Message):
    __slots__ = ("_projectId", "jointName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    JOINTNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    jointName: str
    def __init__(self, _projectId: _Optional[str] = ..., jointName: _Optional[str] = ...) -> None: ...

class getJointPropertyByNameResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class getLiningCompositionPropertyByNameRequest(_message.Message):
    __slots__ = ("_projectId", "compositeLinerName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    COMPOSITELINERNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    compositeLinerName: str
    def __init__(self, _projectId: _Optional[str] = ..., compositeLinerName: _Optional[str] = ...) -> None: ...

class getLiningCompositionPropertyByNameResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class getPilePropertyByNameRequest(_message.Message):
    __slots__ = ("_projectId", "pileName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    PILENAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    pileName: str
    def __init__(self, _projectId: _Optional[str] = ..., pileName: _Optional[str] = ...) -> None: ...

class getPilePropertyByNameResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class getMaterialPropertyByNameRequest(_message.Message):
    __slots__ = ("_projectId", "materialName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    MATERIALNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    materialName: str
    def __init__(self, _projectId: _Optional[str] = ..., materialName: _Optional[str] = ...) -> None: ...

class getMaterialPropertyByNameResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class getWaterByLocationPropertyByNameRequest(_message.Message):
    __slots__ = ("_projectId", "waterSurfaceName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    WATERSURFACENAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    waterSurfaceName: str
    def __init__(self, _projectId: _Optional[str] = ..., waterSurfaceName: _Optional[str] = ...) -> None: ...

class getWaterByLocationPropertyByNameResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class getWaterGridPropertyByNameRequest(_message.Message):
    __slots__ = ("_projectId", "waterGridName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    WATERGRIDNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    waterGridName: str
    def __init__(self, _projectId: _Optional[str] = ..., waterGridName: _Optional[str] = ...) -> None: ...

class getWaterGridPropertyByNameResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class getExternalVolumeByNameRequest(_message.Message):
    __slots__ = ("_projectId", "externalVolumeName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    EXTERNALVOLUMENAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    externalVolumeName: str
    def __init__(self, _projectId: _Optional[str] = ..., externalVolumeName: _Optional[str] = ...) -> None: ...

class getExternalVolumeByNameResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class getDiscreteFunctionByNameRequest(_message.Message):
    __slots__ = ("_projectId", "discreteFunctionName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    DISCRETEFUNCTIONNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    discreteFunctionName: str
    def __init__(self, _projectId: _Optional[str] = ..., discreteFunctionName: _Optional[str] = ...) -> None: ...

class getDiscreteFunctionByNameResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class getShearNormalFunctionByNameRequest(_message.Message):
    __slots__ = ("_projectId", "shearNormalFunctionName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    SHEARNORMALFUNCTIONNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    shearNormalFunctionName: str
    def __init__(self, _projectId: _Optional[str] = ..., shearNormalFunctionName: _Optional[str] = ...) -> None: ...

class getShearNormalFunctionByNameResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class getGeneralizedAnisotropicFunctionByNameRequest(_message.Message):
    __slots__ = ("_projectId", "generalizedAnisotropicFunctionName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    GENERALIZEDANISOTROPICFUNCTIONNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    generalizedAnisotropicFunctionName: str
    def __init__(self, _projectId: _Optional[str] = ..., generalizedAnisotropicFunctionName: _Optional[str] = ...) -> None: ...

class getGeneralizedAnisotropicFunctionByNameResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class getCustomHydraulicModelPropertyByNameRequest(_message.Message):
    __slots__ = ("_projectId", "hydraulicModelName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    HYDRAULICMODELNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    hydraulicModelName: str
    def __init__(self, _projectId: _Optional[str] = ..., hydraulicModelName: _Optional[str] = ...) -> None: ...

class getCustomHydraulicModelPropertyByNameResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class getAllBoltPropertiesRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class getAllBoltPropertiesResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getAllBeamPropertiesRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class getAllBeamPropertiesResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getAllLinerPropertiesRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class getAllLinerPropertiesResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getAllJointPropertiesRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class getAllJointPropertiesResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getAllLiningCompositionPropertiesRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class getAllLiningCompositionPropertiesResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getAllPilePropertiesRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class getAllPilePropertiesResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getAllMaterialPropertiesRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class getAllMaterialPropertiesResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getAllWaterByLocationPropertiesRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class getAllWaterByLocationPropertiesResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getAllWaterGridPropertiesRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class getAllWaterGridPropertiesResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getAllCustomHydraulicModelPropertiesRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class getAllCustomHydraulicModelPropertiesResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getAllExternalVolumesRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class getAllExternalVolumesResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getAllBoltPropertiesInUseRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class getAllBoltPropertiesInUseResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getAllBeamPropertiesInUseRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class getAllBeamPropertiesInUseResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getAllLinerPropertiesInUseRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class getAllLinerPropertiesInUseResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getAllJointPropertiesInUseRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class getAllJointPropertiesInUseResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getAllLiningCompositionPropertiesInUseRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class getAllLiningCompositionPropertiesInUseResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getAllPilePropertiesInUseRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class getAllPilePropertiesInUseResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getAllMaterialPropertiesInUseRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class getAllMaterialPropertiesInUseResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getBoltPropertiesInUseByStageRequest(_message.Message):
    __slots__ = ("_projectId", "_stageNum")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _STAGENUM_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    _stageNum: int
    def __init__(self, _projectId: _Optional[str] = ..., _stageNum: _Optional[int] = ...) -> None: ...

class getBoltPropertiesInUseByStageResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getBeamPropertiesInUseByStageRequest(_message.Message):
    __slots__ = ("_projectId", "_stageNum")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _STAGENUM_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    _stageNum: int
    def __init__(self, _projectId: _Optional[str] = ..., _stageNum: _Optional[int] = ...) -> None: ...

class getBeamPropertiesInUseByStageResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getLinerPropertiesInUseByStageRequest(_message.Message):
    __slots__ = ("_projectId", "_stageNum")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _STAGENUM_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    _stageNum: int
    def __init__(self, _projectId: _Optional[str] = ..., _stageNum: _Optional[int] = ...) -> None: ...

class getLinerPropertiesInUseByStageResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getJointPropertiesInUseByStageRequest(_message.Message):
    __slots__ = ("_projectId", "_stageNum")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _STAGENUM_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    _stageNum: int
    def __init__(self, _projectId: _Optional[str] = ..., _stageNum: _Optional[int] = ...) -> None: ...

class getJointPropertiesInUseByStageResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getLiningCompositionPropertiesInUseByStageRequest(_message.Message):
    __slots__ = ("_projectId", "_stageNum")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _STAGENUM_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    _stageNum: int
    def __init__(self, _projectId: _Optional[str] = ..., _stageNum: _Optional[int] = ...) -> None: ...

class getLiningCompositionPropertiesInUseByStageResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getPilePropertiesInUseByStageRequest(_message.Message):
    __slots__ = ("_projectId", "_stageNum")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _STAGENUM_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    _stageNum: int
    def __init__(self, _projectId: _Optional[str] = ..., _stageNum: _Optional[int] = ...) -> None: ...

class getPilePropertiesInUseByStageResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getMaterialPropertiesInUseByStageRequest(_message.Message):
    __slots__ = ("_projectId", "_stageNum")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _STAGENUM_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    _stageNum: int
    def __init__(self, _projectId: _Optional[str] = ..., _stageNum: _Optional[int] = ...) -> None: ...

class getMaterialPropertiesInUseByStageResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class createNewBoltPropertyRequest(_message.Message):
    __slots__ = ("_projectId", "boltName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    BOLTNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    boltName: str
    def __init__(self, _projectId: _Optional[str] = ..., boltName: _Optional[str] = ...) -> None: ...

class createNewBoltPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class deleteBoltPropertyRequest(_message.Message):
    __slots__ = ("_projectId", "boltName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    BOLTNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    boltName: str
    def __init__(self, _projectId: _Optional[str] = ..., boltName: _Optional[str] = ...) -> None: ...

class deleteBoltPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class createNewBeamPropertyRequest(_message.Message):
    __slots__ = ("_projectId", "beamName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    BEAMNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    beamName: str
    def __init__(self, _projectId: _Optional[str] = ..., beamName: _Optional[str] = ...) -> None: ...

class createNewBeamPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class deleteBeamPropertyRequest(_message.Message):
    __slots__ = ("_projectId", "beamName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    BEAMNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    beamName: str
    def __init__(self, _projectId: _Optional[str] = ..., beamName: _Optional[str] = ...) -> None: ...

class deleteBeamPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class createNewJointPropertyRequest(_message.Message):
    __slots__ = ("_projectId", "jointName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    JOINTNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    jointName: str
    def __init__(self, _projectId: _Optional[str] = ..., jointName: _Optional[str] = ...) -> None: ...

class createNewJointPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class deleteJointPropertyRequest(_message.Message):
    __slots__ = ("_projectId", "jointName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    JOINTNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    jointName: str
    def __init__(self, _projectId: _Optional[str] = ..., jointName: _Optional[str] = ...) -> None: ...

class deleteJointPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class createNewLinerPropertyRequest(_message.Message):
    __slots__ = ("_projectId", "linerName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    LINERNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    linerName: str
    def __init__(self, _projectId: _Optional[str] = ..., linerName: _Optional[str] = ...) -> None: ...

class createNewLinerPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class deleteLinerPropertyRequest(_message.Message):
    __slots__ = ("_projectId", "linerName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    LINERNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    linerName: str
    def __init__(self, _projectId: _Optional[str] = ..., linerName: _Optional[str] = ...) -> None: ...

class deleteLinerPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class createNewLiningCompositionPropertyRequest(_message.Message):
    __slots__ = ("_projectId", "compositeLinerName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    COMPOSITELINERNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    compositeLinerName: str
    def __init__(self, _projectId: _Optional[str] = ..., compositeLinerName: _Optional[str] = ...) -> None: ...

class createNewLiningCompositionPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class deleteLiningCompositionPropertyRequest(_message.Message):
    __slots__ = ("_projectId", "compositeLinerName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    COMPOSITELINERNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    compositeLinerName: str
    def __init__(self, _projectId: _Optional[str] = ..., compositeLinerName: _Optional[str] = ...) -> None: ...

class deleteLiningCompositionPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class createNewPilePropertyRequest(_message.Message):
    __slots__ = ("_projectId", "pileName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    PILENAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    pileName: str
    def __init__(self, _projectId: _Optional[str] = ..., pileName: _Optional[str] = ...) -> None: ...

class createNewPilePropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class deletePilePropertyRequest(_message.Message):
    __slots__ = ("_projectId", "pileName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    PILENAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    pileName: str
    def __init__(self, _projectId: _Optional[str] = ..., pileName: _Optional[str] = ...) -> None: ...

class deletePilePropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class createNewMaterialPropertyRequest(_message.Message):
    __slots__ = ("_projectId", "materialName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    MATERIALNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    materialName: str
    def __init__(self, _projectId: _Optional[str] = ..., materialName: _Optional[str] = ...) -> None: ...

class createNewMaterialPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class deleteMaterialPropertyRequest(_message.Message):
    __slots__ = ("_projectId", "materialName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    MATERIALNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    materialName: str
    def __init__(self, _projectId: _Optional[str] = ..., materialName: _Optional[str] = ...) -> None: ...

class deleteMaterialPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class createNewWaterByLocationPropertyRequest(_message.Message):
    __slots__ = ("_projectId", "waterSurfaceName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    WATERSURFACENAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    waterSurfaceName: str
    def __init__(self, _projectId: _Optional[str] = ..., waterSurfaceName: _Optional[str] = ...) -> None: ...

class createNewWaterByLocationPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class deleteWaterByLocationPropertyRequest(_message.Message):
    __slots__ = ("_projectId", "waterSurfaceName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    WATERSURFACENAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    waterSurfaceName: str
    def __init__(self, _projectId: _Optional[str] = ..., waterSurfaceName: _Optional[str] = ...) -> None: ...

class deleteWaterByLocationPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class createNewWaterGridPropertyRequest(_message.Message):
    __slots__ = ("_projectId", "waterGridName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    WATERGRIDNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    waterGridName: str
    def __init__(self, _projectId: _Optional[str] = ..., waterGridName: _Optional[str] = ...) -> None: ...

class createNewWaterGridPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class deleteWaterGridPropertyRequest(_message.Message):
    __slots__ = ("_projectId", "waterGridName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    WATERGRIDNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    waterGridName: str
    def __init__(self, _projectId: _Optional[str] = ..., waterGridName: _Optional[str] = ...) -> None: ...

class deleteWaterGridPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class getDiscreteFunctionsRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class getDiscreteFunctionsResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getShearNormalFunctionsRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class getShearNormalFunctionsResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class getGeneralizedAnisotropicFunctionsRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class getGeneralizedAnisotropicFunctionsResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class createNewDiscreteFunctionRequest(_message.Message):
    __slots__ = ("_projectId", "discreteFunctionName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    DISCRETEFUNCTIONNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    discreteFunctionName: str
    def __init__(self, _projectId: _Optional[str] = ..., discreteFunctionName: _Optional[str] = ...) -> None: ...

class createNewDiscreteFunctionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class deleteDiscreteFunctionRequest(_message.Message):
    __slots__ = ("_projectId", "discreteFunctionName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    DISCRETEFUNCTIONNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    discreteFunctionName: str
    def __init__(self, _projectId: _Optional[str] = ..., discreteFunctionName: _Optional[str] = ...) -> None: ...

class deleteDiscreteFunctionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class createNewShearNormalFunctionRequest(_message.Message):
    __slots__ = ("_projectId", "shearNormalFunctionName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    SHEARNORMALFUNCTIONNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    shearNormalFunctionName: str
    def __init__(self, _projectId: _Optional[str] = ..., shearNormalFunctionName: _Optional[str] = ...) -> None: ...

class createNewShearNormalFunctionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class deleteShearNormalFunctionRequest(_message.Message):
    __slots__ = ("_projectId", "shearNormalFunctionName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    SHEARNORMALFUNCTIONNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    shearNormalFunctionName: str
    def __init__(self, _projectId: _Optional[str] = ..., shearNormalFunctionName: _Optional[str] = ...) -> None: ...

class deleteShearNormalFunctionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class createNewGeneralizedAnisotropicFunctionRequest(_message.Message):
    __slots__ = ("_projectId", "generalizedAnisotropicFunctionName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    GENERALIZEDANISOTROPICFUNCTIONNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    generalizedAnisotropicFunctionName: str
    def __init__(self, _projectId: _Optional[str] = ..., generalizedAnisotropicFunctionName: _Optional[str] = ...) -> None: ...

class createNewGeneralizedAnisotropicFunctionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class deleteGeneralizedAnisotropicFunctionRequest(_message.Message):
    __slots__ = ("_projectId", "generalizedAnisotropicFunctionName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    GENERALIZEDANISOTROPICFUNCTIONNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    generalizedAnisotropicFunctionName: str
    def __init__(self, _projectId: _Optional[str] = ..., generalizedAnisotropicFunctionName: _Optional[str] = ...) -> None: ...

class deleteGeneralizedAnisotropicFunctionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class createNewCustomHydraulicModelRequest(_message.Message):
    __slots__ = ("_projectId", "customHydraulicModelFunctionName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMHYDRAULICMODELFUNCTIONNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    customHydraulicModelFunctionName: str
    def __init__(self, _projectId: _Optional[str] = ..., customHydraulicModelFunctionName: _Optional[str] = ...) -> None: ...

class createNewCustomHydraulicModelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class deleteCustomHydraulicModelRequest(_message.Message):
    __slots__ = ("_projectId", "hydraulicModelName")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    HYDRAULICMODELNAME_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    hydraulicModelName: str
    def __init__(self, _projectId: _Optional[str] = ..., hydraulicModelName: _Optional[str] = ...) -> None: ...

class deleteCustomHydraulicModelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

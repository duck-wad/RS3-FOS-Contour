import CommonMessages_pb2 as _CommonMessages_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetFunctionPropertyRequest(_message.Message):
    __slots__ = ("objectId", "functionType", "propertyName", "value")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    FUNCTIONTYPE_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    functionType: str
    propertyName: str
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, objectId: _Optional[str] = ..., functionType: _Optional[str] = ..., propertyName: _Optional[str] = ..., value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

class SetFunctionPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetFunctionPropertyRequest(_message.Message):
    __slots__ = ("objectId", "functionType", "propertyName")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    FUNCTIONTYPE_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    functionType: str
    propertyName: str
    def __init__(self, objectId: _Optional[str] = ..., functionType: _Optional[str] = ..., propertyName: _Optional[str] = ...) -> None: ...

class GetFunctionPropertyResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

class SetFunctionColorRequest(_message.Message):
    __slots__ = ("objectId", "functionType", "value")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    FUNCTIONTYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    functionType: str
    value: bytes
    def __init__(self, objectId: _Optional[str] = ..., functionType: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...

class SetFunctionColorResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetFunctionColorRequest(_message.Message):
    __slots__ = ("objectId", "functionType")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    FUNCTIONTYPE_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    functionType: str
    def __init__(self, objectId: _Optional[str] = ..., functionType: _Optional[str] = ...) -> None: ...

class GetFunctionColorResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bytes
    def __init__(self, value: _Optional[bytes] = ...) -> None: ...

class SetDiscreteFunctionDataPointsRequest(_message.Message):
    __slots__ = ("objectId", "propertyName", "value")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    propertyName: str
    value: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, objectId: _Optional[str] = ..., propertyName: _Optional[str] = ..., value: _Optional[_Iterable[float]] = ...) -> None: ...

class SetDiscreteFunctionDataPointsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetDiscreteFunctionDataPointsRequest(_message.Message):
    __slots__ = ("objectId", "propertyName")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    propertyName: str
    def __init__(self, objectId: _Optional[str] = ..., propertyName: _Optional[str] = ...) -> None: ...

class GetDiscreteFunctionDataPointsResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, value: _Optional[_Iterable[float]] = ...) -> None: ...

class ShearNormalPoints(_message.Message):
    __slots__ = ("normalVal", "shearVal", "residualShearVal")
    NORMALVAL_FIELD_NUMBER: _ClassVar[int]
    SHEARVAL_FIELD_NUMBER: _ClassVar[int]
    RESIDUALSHEARVAL_FIELD_NUMBER: _ClassVar[int]
    normalVal: float
    shearVal: float
    residualShearVal: float
    def __init__(self, normalVal: _Optional[float] = ..., shearVal: _Optional[float] = ..., residualShearVal: _Optional[float] = ...) -> None: ...

class SetShearNormalFunctionDataPointsRequest(_message.Message):
    __slots__ = ("objectId", "value")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    value: _containers.RepeatedCompositeFieldContainer[ShearNormalPoints]
    def __init__(self, objectId: _Optional[str] = ..., value: _Optional[_Iterable[_Union[ShearNormalPoints, _Mapping]]] = ...) -> None: ...

class SetShearNormalFunctionDataPointsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetShearNormalFunctionDataPointsRequest(_message.Message):
    __slots__ = ("objectId",)
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    def __init__(self, objectId: _Optional[str] = ...) -> None: ...

class GetShearNormalFunctionDataPointsResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[ShearNormalPoints]
    def __init__(self, value: _Optional[_Iterable[_Union[ShearNormalPoints, _Mapping]]] = ...) -> None: ...

class DipDipDirectionPoints(_message.Message):
    __slots__ = ("dip", "dipDirection", "A", "B", "materialName")
    DIP_FIELD_NUMBER: _ClassVar[int]
    DIPDIRECTION_FIELD_NUMBER: _ClassVar[int]
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    MATERIALNAME_FIELD_NUMBER: _ClassVar[int]
    dip: float
    dipDirection: float
    A: float
    B: float
    materialName: str
    def __init__(self, dip: _Optional[float] = ..., dipDirection: _Optional[float] = ..., A: _Optional[float] = ..., B: _Optional[float] = ..., materialName: _Optional[str] = ...) -> None: ...

class SetGeneralizedAnisotropicFunctionDipDataPointsRequest(_message.Message):
    __slots__ = ("objectId", "projectId", "value")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    projectId: str
    value: _containers.RepeatedCompositeFieldContainer[DipDipDirectionPoints]
    def __init__(self, objectId: _Optional[str] = ..., projectId: _Optional[str] = ..., value: _Optional[_Iterable[_Union[DipDipDirectionPoints, _Mapping]]] = ...) -> None: ...

class SetGeneralizedAnisotropicFunctionDipDataPointsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetGeneralizedAnisotropicFunctionDipDataPointsRequest(_message.Message):
    __slots__ = ("objectId", "projectId")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    projectId: str
    def __init__(self, objectId: _Optional[str] = ..., projectId: _Optional[str] = ...) -> None: ...

class GetGeneralizedAnisotropicFunctionDipDataPointsResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[DipDipDirectionPoints]
    def __init__(self, value: _Optional[_Iterable[_Union[DipDipDirectionPoints, _Mapping]]] = ...) -> None: ...

class SetSnowdenPropertyRequest(_message.Message):
    __slots__ = ("materialId", "isBeddingFunction", "propertyName", "value")
    MATERIALID_FIELD_NUMBER: _ClassVar[int]
    ISBEDDINGFUNCTION_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    materialId: str
    isBeddingFunction: bool
    propertyName: str
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, materialId: _Optional[str] = ..., isBeddingFunction: bool = ..., propertyName: _Optional[str] = ..., value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

class SetSnowdenPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSnowdenPropertyRequest(_message.Message):
    __slots__ = ("objectId", "isBeddingFunction", "propertyName")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    ISBEDDINGFUNCTION_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    isBeddingFunction: bool
    propertyName: str
    def __init__(self, objectId: _Optional[str] = ..., isBeddingFunction: bool = ..., propertyName: _Optional[str] = ...) -> None: ...

class GetSnowdenPropertyResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

class SurfacePoints(_message.Message):
    __slots__ = ("surfaceName", "A", "B", "materialName")
    SURFACENAME_FIELD_NUMBER: _ClassVar[int]
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    MATERIALNAME_FIELD_NUMBER: _ClassVar[int]
    surfaceName: str
    A: float
    B: float
    materialName: str
    def __init__(self, surfaceName: _Optional[str] = ..., A: _Optional[float] = ..., B: _Optional[float] = ..., materialName: _Optional[str] = ...) -> None: ...

class SetGeneralizedAnisotropicFunctionSurfaceDataPointsRequest(_message.Message):
    __slots__ = ("objectId", "projectId", "value")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    projectId: str
    value: _containers.RepeatedCompositeFieldContainer[SurfacePoints]
    def __init__(self, objectId: _Optional[str] = ..., projectId: _Optional[str] = ..., value: _Optional[_Iterable[_Union[SurfacePoints, _Mapping]]] = ...) -> None: ...

class SetGeneralizedAnisotropicFunctionSurfaceDataPointsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetGeneralizedAnisotropicFunctionSurfaceDataPointsRequest(_message.Message):
    __slots__ = ("objectId", "projectId")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    projectId: str
    def __init__(self, objectId: _Optional[str] = ..., projectId: _Optional[str] = ...) -> None: ...

class GetGeneralizedAnisotropicFunctionSurfaceDataPointsResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[SurfacePoints]
    def __init__(self, value: _Optional[_Iterable[_Union[SurfacePoints, _Mapping]]] = ...) -> None: ...

class SetGeneralizedAnisotropicBaseMaterialRequest(_message.Message):
    __slots__ = ("objectId", "projectId", "baseMaterial")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    BASEMATERIAL_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    projectId: str
    baseMaterial: str
    def __init__(self, objectId: _Optional[str] = ..., projectId: _Optional[str] = ..., baseMaterial: _Optional[str] = ...) -> None: ...

class SetGeneralizedAnisotropicBaseMaterialResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetGeneralizedAnisotropicBaseMaterialRequest(_message.Message):
    __slots__ = ("objectId",)
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    def __init__(self, objectId: _Optional[str] = ...) -> None: ...

class GetGeneralizedAnisotropicBaseMaterialResponse(_message.Message):
    __slots__ = ("baseMaterial",)
    BASEMATERIAL_FIELD_NUMBER: _ClassVar[int]
    baseMaterial: str
    def __init__(self, baseMaterial: _Optional[str] = ...) -> None: ...

class SetShearNormalFunctionRequest(_message.Message):
    __slots__ = ("objectId", "isBeddingFunction", "isResidualFunction", "normalStress", "shearStress", "residualShearStress")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    ISBEDDINGFUNCTION_FIELD_NUMBER: _ClassVar[int]
    ISRESIDUALFUNCTION_FIELD_NUMBER: _ClassVar[int]
    NORMALSTRESS_FIELD_NUMBER: _ClassVar[int]
    SHEARSTRESS_FIELD_NUMBER: _ClassVar[int]
    RESIDUALSHEARSTRESS_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    isBeddingFunction: bool
    isResidualFunction: bool
    normalStress: _containers.RepeatedScalarFieldContainer[float]
    shearStress: _containers.RepeatedScalarFieldContainer[float]
    residualShearStress: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, objectId: _Optional[str] = ..., isBeddingFunction: bool = ..., isResidualFunction: bool = ..., normalStress: _Optional[_Iterable[float]] = ..., shearStress: _Optional[_Iterable[float]] = ..., residualShearStress: _Optional[_Iterable[float]] = ...) -> None: ...

class SetShearNormalFunctionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetCohesionFrictionFunctionRequest(_message.Message):
    __slots__ = ("objectId", "isBeddingFunction", "isResidualFunction", "normalStress", "cohesion", "frictionAngle", "residualCohesion", "residualFrictionAngle")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    ISBEDDINGFUNCTION_FIELD_NUMBER: _ClassVar[int]
    ISRESIDUALFUNCTION_FIELD_NUMBER: _ClassVar[int]
    NORMALSTRESS_FIELD_NUMBER: _ClassVar[int]
    COHESION_FIELD_NUMBER: _ClassVar[int]
    FRICTIONANGLE_FIELD_NUMBER: _ClassVar[int]
    RESIDUALCOHESION_FIELD_NUMBER: _ClassVar[int]
    RESIDUALFRICTIONANGLE_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    isBeddingFunction: bool
    isResidualFunction: bool
    normalStress: _containers.RepeatedScalarFieldContainer[float]
    cohesion: _containers.RepeatedScalarFieldContainer[float]
    frictionAngle: _containers.RepeatedScalarFieldContainer[float]
    residualCohesion: _containers.RepeatedScalarFieldContainer[float]
    residualFrictionAngle: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, objectId: _Optional[str] = ..., isBeddingFunction: bool = ..., isResidualFunction: bool = ..., normalStress: _Optional[_Iterable[float]] = ..., cohesion: _Optional[_Iterable[float]] = ..., frictionAngle: _Optional[_Iterable[float]] = ..., residualCohesion: _Optional[_Iterable[float]] = ..., residualFrictionAngle: _Optional[_Iterable[float]] = ...) -> None: ...

class SetCohesionFrictionFunctionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSnowdenStrengthFunctionColumnRequest(_message.Message):
    __slots__ = ("objectId", "propertyName", "isBeddingFunction", "isShearNormal")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    ISBEDDINGFUNCTION_FIELD_NUMBER: _ClassVar[int]
    ISSHEARNORMAL_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    propertyName: str
    isBeddingFunction: bool
    isShearNormal: bool
    def __init__(self, objectId: _Optional[str] = ..., propertyName: _Optional[str] = ..., isBeddingFunction: bool = ..., isShearNormal: bool = ...) -> None: ...

class GetSnowdenStrengthFunctionColumnResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[_CommonMessages_pb2.PropertyValue]
    def __init__(self, value: _Optional[_Iterable[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]]] = ...) -> None: ...

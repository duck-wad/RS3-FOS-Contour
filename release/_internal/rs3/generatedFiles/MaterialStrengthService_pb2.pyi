import CommonMessages_pb2 as _CommonMessages_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetSelectedFunctionPropertyRequest(_message.Message):
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

class SetSelectedFunctionPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSelectedFunctionPropertyRequest(_message.Message):
    __slots__ = ("objectId", "functionType", "propertyName")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    FUNCTIONTYPE_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    functionType: str
    propertyName: str
    def __init__(self, objectId: _Optional[str] = ..., functionType: _Optional[str] = ..., propertyName: _Optional[str] = ...) -> None: ...

class GetSelectedFunctionPropertyResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

class PlasticStrainVsFrictionAnglePoint(_message.Message):
    __slots__ = ("plasticStrain", "frictionAngle")
    PLASTICSTRAIN_FIELD_NUMBER: _ClassVar[int]
    FRICTIONANGLE_FIELD_NUMBER: _ClassVar[int]
    plasticStrain: float
    frictionAngle: float
    def __init__(self, plasticStrain: _Optional[float] = ..., frictionAngle: _Optional[float] = ...) -> None: ...

class PlasticStrainVsCohesionPoint(_message.Message):
    __slots__ = ("plasticStrain", "cohesion")
    PLASTICSTRAIN_FIELD_NUMBER: _ClassVar[int]
    COHESION_FIELD_NUMBER: _ClassVar[int]
    plasticStrain: float
    cohesion: float
    def __init__(self, plasticStrain: _Optional[float] = ..., cohesion: _Optional[float] = ...) -> None: ...

class SetConeHardeningFunctionRequest(_message.Message):
    __slots__ = ("objectId", "frictionAngleFunction", "cohesionFunction")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    FRICTIONANGLEFUNCTION_FIELD_NUMBER: _ClassVar[int]
    COHESIONFUNCTION_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    frictionAngleFunction: _containers.RepeatedCompositeFieldContainer[PlasticStrainVsFrictionAnglePoint]
    cohesionFunction: _containers.RepeatedCompositeFieldContainer[PlasticStrainVsCohesionPoint]
    def __init__(self, objectId: _Optional[str] = ..., frictionAngleFunction: _Optional[_Iterable[_Union[PlasticStrainVsFrictionAnglePoint, _Mapping]]] = ..., cohesionFunction: _Optional[_Iterable[_Union[PlasticStrainVsCohesionPoint, _Mapping]]] = ...) -> None: ...

class SetConeHardeningFunctionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetConeHardeningFunctionRequest(_message.Message):
    __slots__ = ("objectId",)
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    def __init__(self, objectId: _Optional[str] = ...) -> None: ...

class GetConeHardeningFunctionResponse(_message.Message):
    __slots__ = ("frictionAngleFunction", "cohesionFunction")
    FRICTIONANGLEFUNCTION_FIELD_NUMBER: _ClassVar[int]
    COHESIONFUNCTION_FIELD_NUMBER: _ClassVar[int]
    frictionAngleFunction: _containers.RepeatedCompositeFieldContainer[PlasticStrainVsFrictionAnglePoint]
    cohesionFunction: _containers.RepeatedCompositeFieldContainer[PlasticStrainVsCohesionPoint]
    def __init__(self, frictionAngleFunction: _Optional[_Iterable[_Union[PlasticStrainVsFrictionAnglePoint, _Mapping]]] = ..., cohesionFunction: _Optional[_Iterable[_Union[PlasticStrainVsCohesionPoint, _Mapping]]] = ...) -> None: ...

class SetAnisotropicLinearPlanarPropertyRequest(_message.Message):
    __slots__ = ("objectId", "propertyName", "value")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    propertyName: str
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, objectId: _Optional[str] = ..., propertyName: _Optional[str] = ..., value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

class SetAnisotropicLinearPlanarPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAnisotropicLinearPlanarPropertyRequest(_message.Message):
    __slots__ = ("objectId", "propertyName")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    propertyName: str
    def __init__(self, objectId: _Optional[str] = ..., propertyName: _Optional[str] = ...) -> None: ...

class GetAnisotropicLinearPlanarPropertyResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

class SetAnisotropicSurfacePropertyRequest(_message.Message):
    __slots__ = ("objectId", "surfaceName")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    SURFACENAME_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    surfaceName: str
    def __init__(self, objectId: _Optional[str] = ..., surfaceName: _Optional[str] = ...) -> None: ...

class SetAnisotropicSurfacePropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAnisotropicSurfacePropertyRequest(_message.Message):
    __slots__ = ("objectId",)
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    def __init__(self, objectId: _Optional[str] = ...) -> None: ...

class GetAnisotropicSurfacePropertyResponse(_message.Message):
    __slots__ = ("surfaceName",)
    SURFACENAME_FIELD_NUMBER: _ClassVar[int]
    surfaceName: str
    def __init__(self, surfaceName: _Optional[str] = ...) -> None: ...

class MeanStressDataPoint(_message.Message):
    __slots__ = ("volumetricPlasticStrain", "meanStress")
    VOLUMETRICPLASTICSTRAIN_FIELD_NUMBER: _ClassVar[int]
    MEANSTRESS_FIELD_NUMBER: _ClassVar[int]
    volumetricPlasticStrain: float
    meanStress: float
    def __init__(self, volumetricPlasticStrain: _Optional[float] = ..., meanStress: _Optional[float] = ...) -> None: ...

class SetMeanStressFunctionPropertyRequest(_message.Message):
    __slots__ = ("objectId", "point")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    POINT_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    point: _containers.RepeatedCompositeFieldContainer[MeanStressDataPoint]
    def __init__(self, objectId: _Optional[str] = ..., point: _Optional[_Iterable[_Union[MeanStressDataPoint, _Mapping]]] = ...) -> None: ...

class SetMeanStressFunctionPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMeanStressFunctionPropertyRequest(_message.Message):
    __slots__ = ("objectId",)
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    def __init__(self, objectId: _Optional[str] = ...) -> None: ...

class GetMeanStressFunctionPropertyResponse(_message.Message):
    __slots__ = ("point",)
    POINT_FIELD_NUMBER: _ClassVar[int]
    point: _containers.RepeatedCompositeFieldContainer[MeanStressDataPoint]
    def __init__(self, point: _Optional[_Iterable[_Union[MeanStressDataPoint, _Mapping]]] = ...) -> None: ...

class MaterialDependentVerticalStressPoint(_message.Message):
    __slots__ = ("materialName", "verticalStessFactor")
    MATERIALNAME_FIELD_NUMBER: _ClassVar[int]
    VERTICALSTESSFACTOR_FIELD_NUMBER: _ClassVar[int]
    materialName: str
    verticalStessFactor: float
    def __init__(self, materialName: _Optional[str] = ..., verticalStessFactor: _Optional[float] = ...) -> None: ...

class SetMaterialDependentVerticalStressFactorPropertyRequest(_message.Message):
    __slots__ = ("objectId", "point")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    POINT_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    point: _containers.RepeatedCompositeFieldContainer[MaterialDependentVerticalStressPoint]
    def __init__(self, objectId: _Optional[str] = ..., point: _Optional[_Iterable[_Union[MaterialDependentVerticalStressPoint, _Mapping]]] = ...) -> None: ...

class SetMaterialDependentVerticalStressFactorPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMaterialDependentVerticalStressFactorPropertyRequest(_message.Message):
    __slots__ = ("objectId",)
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    def __init__(self, objectId: _Optional[str] = ...) -> None: ...

class GetMaterialDependentVerticalStressFactorPropertyResponse(_message.Message):
    __slots__ = ("point",)
    POINT_FIELD_NUMBER: _ClassVar[int]
    point: _containers.RepeatedCompositeFieldContainer[MaterialDependentVerticalStressPoint]
    def __init__(self, point: _Optional[_Iterable[_Union[MaterialDependentVerticalStressPoint, _Mapping]]] = ...) -> None: ...

class StressHistoryHeader(_message.Message):
    __slots__ = ("column1", "column2")
    COLUMN1_FIELD_NUMBER: _ClassVar[int]
    COLUMN2_FIELD_NUMBER: _ClassVar[int]
    column1: str
    column2: str
    def __init__(self, column1: _Optional[str] = ..., column2: _Optional[str] = ...) -> None: ...

class StressHistoryPoint(_message.Message):
    __slots__ = ("z", "stressHistoryVal")
    Z_FIELD_NUMBER: _ClassVar[int]
    STRESSHISTORYVAL_FIELD_NUMBER: _ClassVar[int]
    z: float
    stressHistoryVal: float
    def __init__(self, z: _Optional[float] = ..., stressHistoryVal: _Optional[float] = ...) -> None: ...

class SetStressHistoryPropertyRequest(_message.Message):
    __slots__ = ("objectId", "header", "point")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    POINT_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    header: StressHistoryHeader
    point: _containers.RepeatedCompositeFieldContainer[StressHistoryPoint]
    def __init__(self, objectId: _Optional[str] = ..., header: _Optional[_Union[StressHistoryHeader, _Mapping]] = ..., point: _Optional[_Iterable[_Union[StressHistoryPoint, _Mapping]]] = ...) -> None: ...

class SetStressHistoryPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetStressHistoryPropertyRequest(_message.Message):
    __slots__ = ("objectId",)
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    def __init__(self, objectId: _Optional[str] = ...) -> None: ...

class GetStressHistoryPropertyResponse(_message.Message):
    __slots__ = ("header", "point")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    POINT_FIELD_NUMBER: _ClassVar[int]
    header: StressHistoryHeader
    point: _containers.RepeatedCompositeFieldContainer[StressHistoryPoint]
    def __init__(self, header: _Optional[_Union[StressHistoryHeader, _Mapping]] = ..., point: _Optional[_Iterable[_Union[StressHistoryPoint, _Mapping]]] = ...) -> None: ...

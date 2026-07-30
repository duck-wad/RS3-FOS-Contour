import CommonMessages_pb2 as _CommonMessages_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetLinearDirectionRequest(_message.Message):
    __slots__ = ("objectId", "upperPropertyName", "propertyName", "value")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    UPPERPROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    upperPropertyName: str
    propertyName: str
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, objectId: _Optional[str] = ..., upperPropertyName: _Optional[str] = ..., propertyName: _Optional[str] = ..., value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

class SetLinearDirectionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetLinearDirectionRequest(_message.Message):
    __slots__ = ("objectId", "upperPropertyName", "propertyName")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    UPPERPROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    upperPropertyName: str
    propertyName: str
    def __init__(self, objectId: _Optional[str] = ..., upperPropertyName: _Optional[str] = ..., propertyName: _Optional[str] = ...) -> None: ...

class GetLinearDirectionResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

class SetInitialWaterConditionRequest(_message.Message):
    __slots__ = ("objectId", "waterType", "waterTableName")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    WATERTYPE_FIELD_NUMBER: _ClassVar[int]
    WATERTABLENAME_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    waterType: str
    waterTableName: str
    def __init__(self, objectId: _Optional[str] = ..., waterType: _Optional[str] = ..., waterTableName: _Optional[str] = ...) -> None: ...

class SetInitialWaterConditionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetInitialWaterConditionRequest(_message.Message):
    __slots__ = ("objectId",)
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    def __init__(self, objectId: _Optional[str] = ...) -> None: ...

class GetInitialWaterConditionResponse(_message.Message):
    __slots__ = ("waterTableName",)
    WATERTABLENAME_FIELD_NUMBER: _ClassVar[int]
    waterTableName: str
    def __init__(self, waterTableName: _Optional[str] = ...) -> None: ...

class CreateNewWaterConditionRequest(_message.Message):
    __slots__ = ("objectId", "waterConditionName", "userDefinedType", "value")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    WATERCONDITIONNAME_FIELD_NUMBER: _ClassVar[int]
    USERDEFINEDTYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    waterConditionName: str
    userDefinedType: str
    value: float
    def __init__(self, objectId: _Optional[str] = ..., waterConditionName: _Optional[str] = ..., userDefinedType: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...

class CreateNewWaterConditionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteWaterConditionRequest(_message.Message):
    __slots__ = ("objectId", "waterConditionName")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    WATERCONDITIONNAME_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    waterConditionName: str
    def __init__(self, objectId: _Optional[str] = ..., waterConditionName: _Optional[str] = ...) -> None: ...

class DeleteWaterConditionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetWaterConditionPropertyByNameRequest(_message.Message):
    __slots__ = ("objectId", "waterConditionName")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    WATERCONDITIONNAME_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    waterConditionName: str
    def __init__(self, objectId: _Optional[str] = ..., waterConditionName: _Optional[str] = ...) -> None: ...

class GetWaterConditionPropertyByNameResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class GetWaterConditionPropertiesRequest(_message.Message):
    __slots__ = ("objectId",)
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    def __init__(self, objectId: _Optional[str] = ...) -> None: ...

class GetWaterConditionPropertiesResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateNewCustomHydraulicModelRequest(_message.Message):
    __slots__ = ("objectId", "hydraulicModelName")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    HYDRAULICMODELNAME_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    hydraulicModelName: str
    def __init__(self, objectId: _Optional[str] = ..., hydraulicModelName: _Optional[str] = ...) -> None: ...

class CreateNewCustomHydraulicModelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteCustomHydraulicModelRequest(_message.Message):
    __slots__ = ("objectId", "hydraulicModelName")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    HYDRAULICMODELNAME_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    hydraulicModelName: str
    def __init__(self, objectId: _Optional[str] = ..., hydraulicModelName: _Optional[str] = ...) -> None: ...

class DeleteCustomHydraulicModelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCustomHydraulicModelPropertyByNameRequest(_message.Message):
    __slots__ = ("objectId", "hydraulicModelName")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    HYDRAULICMODELNAME_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    hydraulicModelName: str
    def __init__(self, objectId: _Optional[str] = ..., hydraulicModelName: _Optional[str] = ...) -> None: ...

class GetCustomHydraulicModelPropertyByNameResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class GetCustomHydraulicModelPropertiesRequest(_message.Message):
    __slots__ = ("objectId",)
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    def __init__(self, objectId: _Optional[str] = ...) -> None: ...

class GetCustomHydraulicModelPropertiesResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class SetCustomHydraulicModelTypeRequest(_message.Message):
    __slots__ = ("objectId", "value")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    value: str
    def __init__(self, objectId: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class SetCustomHydraulicModelTypeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCustomHydraulicModelTypeRequest(_message.Message):
    __slots__ = ("objectId",)
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    def __init__(self, objectId: _Optional[str] = ...) -> None: ...

class GetCustomHydraulicModelTypeResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

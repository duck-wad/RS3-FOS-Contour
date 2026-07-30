import CommonMessages_pb2 as _CommonMessages_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IsotropicFormulaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IsotropicFormulaType_UNSPECIFIED: _ClassVar[IsotropicFormulaType]
    FORMULA_1: _ClassVar[IsotropicFormulaType]
    FORMULA_2: _ClassVar[IsotropicFormulaType]
    FORMULA_3: _ClassVar[IsotropicFormulaType]
IsotropicFormulaType_UNSPECIFIED: IsotropicFormulaType
FORMULA_1: IsotropicFormulaType
FORMULA_2: IsotropicFormulaType
FORMULA_3: IsotropicFormulaType

class SetMaterialStiffnessFormulaPropertyRequest(_message.Message):
    __slots__ = ("propertyId", "isLoading", "propertyName", "value", "formula")
    PROPERTYID_FIELD_NUMBER: _ClassVar[int]
    ISLOADING_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    FORMULA_FIELD_NUMBER: _ClassVar[int]
    propertyId: str
    isLoading: bool
    propertyName: str
    value: _CommonMessages_pb2.PropertyValue
    formula: IsotropicFormulaType
    def __init__(self, propertyId: _Optional[str] = ..., isLoading: bool = ..., propertyName: _Optional[str] = ..., value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ..., formula: _Optional[_Union[IsotropicFormulaType, str]] = ...) -> None: ...

class SetMaterialStiffnessFormulaPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMaterialStiffnessFormulaPropertyRequest(_message.Message):
    __slots__ = ("propertyId", "isLoading", "propertyName", "formula")
    PROPERTYID_FIELD_NUMBER: _ClassVar[int]
    ISLOADING_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    FORMULA_FIELD_NUMBER: _ClassVar[int]
    propertyId: str
    isLoading: bool
    propertyName: str
    formula: IsotropicFormulaType
    def __init__(self, propertyId: _Optional[str] = ..., isLoading: bool = ..., propertyName: _Optional[str] = ..., formula: _Optional[_Union[IsotropicFormulaType, str]] = ...) -> None: ...

class GetMaterialStiffnessFormulaPropertyResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

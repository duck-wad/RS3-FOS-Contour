import CommonMessages_pb2 as _CommonMessages_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetDirectionTypeRequest(_message.Message):
    __slots__ = ("objectId", "value")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    value: str
    def __init__(self, objectId: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class SetDirectionTypeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetDirectionTypeRequest(_message.Message):
    __slots__ = ("objectId",)
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    def __init__(self, objectId: _Optional[str] = ...) -> None: ...

class GetDirectionTypeResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class SetTrendPlungePropertyRequest(_message.Message):
    __slots__ = ("objectId", "sigma1", "sigma3")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    SIGMA1_FIELD_NUMBER: _ClassVar[int]
    SIGMA3_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    sigma1: _CommonMessages_pb2.LinearDirection
    sigma3: _CommonMessages_pb2.LinearDirection
    def __init__(self, objectId: _Optional[str] = ..., sigma1: _Optional[_Union[_CommonMessages_pb2.LinearDirection, _Mapping]] = ..., sigma3: _Optional[_Union[_CommonMessages_pb2.LinearDirection, _Mapping]] = ...) -> None: ...

class SetTrendPlungePropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetTrendPlungePropertyRequest(_message.Message):
    __slots__ = ("objectId",)
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    def __init__(self, objectId: _Optional[str] = ...) -> None: ...

class GetTrendPlungePropertyResponse(_message.Message):
    __slots__ = ("sigma1", "sigma3")
    SIGMA1_FIELD_NUMBER: _ClassVar[int]
    SIGMA3_FIELD_NUMBER: _ClassVar[int]
    sigma1: _CommonMessages_pb2.LinearDirection
    sigma3: _CommonMessages_pb2.LinearDirection
    def __init__(self, sigma1: _Optional[_Union[_CommonMessages_pb2.LinearDirection, _Mapping]] = ..., sigma3: _Optional[_Union[_CommonMessages_pb2.LinearDirection, _Mapping]] = ...) -> None: ...

class SetVectorPropertyRequest(_message.Message):
    __slots__ = ("objectId", "sigma1", "sigma3")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    SIGMA1_FIELD_NUMBER: _ClassVar[int]
    SIGMA3_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    sigma1: _CommonMessages_pb2.Point3D
    sigma3: _CommonMessages_pb2.Point3D
    def __init__(self, objectId: _Optional[str] = ..., sigma1: _Optional[_Union[_CommonMessages_pb2.Point3D, _Mapping]] = ..., sigma3: _Optional[_Union[_CommonMessages_pb2.Point3D, _Mapping]] = ...) -> None: ...

class SetVectorPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetVectorPropertyRequest(_message.Message):
    __slots__ = ("objectId",)
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    def __init__(self, objectId: _Optional[str] = ...) -> None: ...

class GetVectorPropertyResponse(_message.Message):
    __slots__ = ("sigma1", "sigma3")
    SIGMA1_FIELD_NUMBER: _ClassVar[int]
    SIGMA3_FIELD_NUMBER: _ClassVar[int]
    sigma1: _CommonMessages_pb2.Point3D
    sigma3: _CommonMessages_pb2.Point3D
    def __init__(self, sigma1: _Optional[_Union[_CommonMessages_pb2.Point3D, _Mapping]] = ..., sigma3: _Optional[_Union[_CommonMessages_pb2.Point3D, _Mapping]] = ...) -> None: ...

class SetMaterialPropertyRequest(_message.Message):
    __slots__ = ("objectId", "materialName", "propertyName", "value")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    MATERIALNAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    materialName: str
    propertyName: str
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, objectId: _Optional[str] = ..., materialName: _Optional[str] = ..., propertyName: _Optional[str] = ..., value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

class SetMaterialPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMaterialPropertyRequest(_message.Message):
    __slots__ = ("objectId", "materialName", "propertyName")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    MATERIALNAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    materialName: str
    propertyName: str
    def __init__(self, objectId: _Optional[str] = ..., materialName: _Optional[str] = ..., propertyName: _Optional[str] = ...) -> None: ...

class GetMaterialPropertyResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

class SetMaterialTrendPlungePropertyRequest(_message.Message):
    __slots__ = ("objectId", "materialName", "sigma1", "sigma3")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    MATERIALNAME_FIELD_NUMBER: _ClassVar[int]
    SIGMA1_FIELD_NUMBER: _ClassVar[int]
    SIGMA3_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    materialName: str
    sigma1: _CommonMessages_pb2.LinearDirection
    sigma3: _CommonMessages_pb2.LinearDirection
    def __init__(self, objectId: _Optional[str] = ..., materialName: _Optional[str] = ..., sigma1: _Optional[_Union[_CommonMessages_pb2.LinearDirection, _Mapping]] = ..., sigma3: _Optional[_Union[_CommonMessages_pb2.LinearDirection, _Mapping]] = ...) -> None: ...

class SetMaterialTrendPlungePropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMaterialTrendPlungePropertyRequest(_message.Message):
    __slots__ = ("objectId", "materialName")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    MATERIALNAME_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    materialName: str
    def __init__(self, objectId: _Optional[str] = ..., materialName: _Optional[str] = ...) -> None: ...

class GetMaterialTrendPlungePropertyResponse(_message.Message):
    __slots__ = ("sigma1", "sigma3")
    SIGMA1_FIELD_NUMBER: _ClassVar[int]
    SIGMA3_FIELD_NUMBER: _ClassVar[int]
    sigma1: _CommonMessages_pb2.LinearDirection
    sigma3: _CommonMessages_pb2.LinearDirection
    def __init__(self, sigma1: _Optional[_Union[_CommonMessages_pb2.LinearDirection, _Mapping]] = ..., sigma3: _Optional[_Union[_CommonMessages_pb2.LinearDirection, _Mapping]] = ...) -> None: ...

class SetMaterialVectorPropertyRequest(_message.Message):
    __slots__ = ("objectId", "materialName", "sigma1", "sigma3")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    MATERIALNAME_FIELD_NUMBER: _ClassVar[int]
    SIGMA1_FIELD_NUMBER: _ClassVar[int]
    SIGMA3_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    materialName: str
    sigma1: _CommonMessages_pb2.Point3D
    sigma3: _CommonMessages_pb2.Point3D
    def __init__(self, objectId: _Optional[str] = ..., materialName: _Optional[str] = ..., sigma1: _Optional[_Union[_CommonMessages_pb2.Point3D, _Mapping]] = ..., sigma3: _Optional[_Union[_CommonMessages_pb2.Point3D, _Mapping]] = ...) -> None: ...

class SetMaterialVectorPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMaterialVectorPropertyRequest(_message.Message):
    __slots__ = ("objectId", "materialName")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    MATERIALNAME_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    materialName: str
    def __init__(self, objectId: _Optional[str] = ..., materialName: _Optional[str] = ...) -> None: ...

class GetMaterialVectorPropertyResponse(_message.Message):
    __slots__ = ("sigma1", "sigma3")
    SIGMA1_FIELD_NUMBER: _ClassVar[int]
    SIGMA3_FIELD_NUMBER: _ClassVar[int]
    sigma1: _CommonMessages_pb2.Point3D
    sigma3: _CommonMessages_pb2.Point3D
    def __init__(self, sigma1: _Optional[_Union[_CommonMessages_pb2.Point3D, _Mapping]] = ..., sigma3: _Optional[_Union[_CommonMessages_pb2.Point3D, _Mapping]] = ...) -> None: ...

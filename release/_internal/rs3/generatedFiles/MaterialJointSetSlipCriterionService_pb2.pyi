import CommonMessages_pb2 as _CommonMessages_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetJointPropertyRequest(_message.Message):
    __slots__ = ("materialId", "objectId", "propertyName", "value")
    MATERIALID_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    materialId: str
    objectId: str
    propertyName: str
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, materialId: _Optional[str] = ..., objectId: _Optional[str] = ..., propertyName: _Optional[str] = ..., value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

class SetJointPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetJointPropertyRequest(_message.Message):
    __slots__ = ("materialId", "objectId", "propertyName")
    MATERIALID_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    materialId: str
    objectId: str
    propertyName: str
    def __init__(self, materialId: _Optional[str] = ..., objectId: _Optional[str] = ..., propertyName: _Optional[str] = ...) -> None: ...

class GetJointPropertyResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

class SetJointOptionVectorPropertyRequest(_message.Message):
    __slots__ = ("materialId", "objectId", "value")
    MATERIALID_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    materialId: str
    objectId: str
    value: _CommonMessages_pb2.Vector3D
    def __init__(self, materialId: _Optional[str] = ..., objectId: _Optional[str] = ..., value: _Optional[_Union[_CommonMessages_pb2.Vector3D, _Mapping]] = ...) -> None: ...

class SetJointOptionVectorPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetJointOptionVectorPropertyRequest(_message.Message):
    __slots__ = ("materialId", "objectId")
    MATERIALID_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    materialId: str
    objectId: str
    def __init__(self, materialId: _Optional[str] = ..., objectId: _Optional[str] = ...) -> None: ...

class GetJointOptionVectorPropertyResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _CommonMessages_pb2.Vector3D
    def __init__(self, value: _Optional[_Union[_CommonMessages_pb2.Vector3D, _Mapping]] = ...) -> None: ...

class SetJointOptionTrendPlungePropertyRequest(_message.Message):
    __slots__ = ("materialId", "objectId", "trend", "plunge")
    MATERIALID_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    TREND_FIELD_NUMBER: _ClassVar[int]
    PLUNGE_FIELD_NUMBER: _ClassVar[int]
    materialId: str
    objectId: str
    trend: float
    plunge: float
    def __init__(self, materialId: _Optional[str] = ..., objectId: _Optional[str] = ..., trend: _Optional[float] = ..., plunge: _Optional[float] = ...) -> None: ...

class SetJointOptionTrendPlungePropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetJointOptionTrendPlungePropertyRequest(_message.Message):
    __slots__ = ("materialId", "objectId")
    MATERIALID_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    materialId: str
    objectId: str
    def __init__(self, materialId: _Optional[str] = ..., objectId: _Optional[str] = ...) -> None: ...

class GetJointOptionTrendPlungePropertyResponse(_message.Message):
    __slots__ = ("trend", "plunge")
    TREND_FIELD_NUMBER: _ClassVar[int]
    PLUNGE_FIELD_NUMBER: _ClassVar[int]
    trend: float
    plunge: float
    def __init__(self, trend: _Optional[float] = ..., plunge: _Optional[float] = ...) -> None: ...

class SetJointOptionDipDipDirectionPropertyRequest(_message.Message):
    __slots__ = ("materialId", "objectId", "dip", "dipDirection")
    MATERIALID_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    DIP_FIELD_NUMBER: _ClassVar[int]
    DIPDIRECTION_FIELD_NUMBER: _ClassVar[int]
    materialId: str
    objectId: str
    dip: float
    dipDirection: float
    def __init__(self, materialId: _Optional[str] = ..., objectId: _Optional[str] = ..., dip: _Optional[float] = ..., dipDirection: _Optional[float] = ...) -> None: ...

class SetJointOptionDipDipDirectionPropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetJointOptionDipDipDirectionPropertyRequest(_message.Message):
    __slots__ = ("materialId", "objectId")
    MATERIALID_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    materialId: str
    objectId: str
    def __init__(self, materialId: _Optional[str] = ..., objectId: _Optional[str] = ...) -> None: ...

class GetJointOptionDipDipDirectionPropertyResponse(_message.Message):
    __slots__ = ("dip", "dipDirection")
    DIP_FIELD_NUMBER: _ClassVar[int]
    DIPDIRECTION_FIELD_NUMBER: _ClassVar[int]
    dip: float
    dipDirection: float
    def __init__(self, dip: _Optional[float] = ..., dipDirection: _Optional[float] = ...) -> None: ...

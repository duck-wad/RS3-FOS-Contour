import CommonMessages_pb2 as _CommonMessages_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetProjectUnitRequest(_message.Message):
    __slots__ = ("objectId", "propertyName", "value", "resetProperties")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    RESETPROPERTIES_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    propertyName: str
    value: _CommonMessages_pb2.PropertyValue
    resetProperties: bool
    def __init__(self, objectId: _Optional[str] = ..., propertyName: _Optional[str] = ..., value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ..., resetProperties: bool = ...) -> None: ...

class SetProjectUnitResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetStagePropertyRequest(_message.Message):
    __slots__ = ("objectId", "propertyName", "stageNumber", "value")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    STAGENUMBER_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    propertyName: str
    stageNumber: int
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, objectId: _Optional[str] = ..., propertyName: _Optional[str] = ..., stageNumber: _Optional[int] = ..., value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

class SetStagePropertyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetStagePropertyRequest(_message.Message):
    __slots__ = ("objectId", "propertyName", "stageNumber")
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    PROPERTYNAME_FIELD_NUMBER: _ClassVar[int]
    STAGENUMBER_FIELD_NUMBER: _ClassVar[int]
    objectId: str
    propertyName: str
    stageNumber: int
    def __init__(self, objectId: _Optional[str] = ..., propertyName: _Optional[str] = ..., stageNumber: _Optional[int] = ...) -> None: ...

class GetStagePropertyResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _CommonMessages_pb2.PropertyValue
    def __init__(self, value: _Optional[_Union[_CommonMessages_pb2.PropertyValue, _Mapping]] = ...) -> None: ...

class GetDefinedStageNamesRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class GetDefinedStageNamesResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

class SetTotalNumberOfStagesRequest(_message.Message):
    __slots__ = ("_projectId", "numberOfStages")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFSTAGES_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    numberOfStages: int
    def __init__(self, _projectId: _Optional[str] = ..., numberOfStages: _Optional[int] = ...) -> None: ...

class SetTotalNumberOfStagesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddStagesRequest(_message.Message):
    __slots__ = ("_projectId", "referenceStage", "numberOfStages")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    REFERENCESTAGE_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFSTAGES_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    referenceStage: int
    numberOfStages: int
    def __init__(self, _projectId: _Optional[str] = ..., referenceStage: _Optional[int] = ..., numberOfStages: _Optional[int] = ...) -> None: ...

class AddStagesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteStagesRequest(_message.Message):
    __slots__ = ("_projectId", "startingStage", "numberOfStages")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    STARTINGSTAGE_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFSTAGES_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    startingStage: int
    numberOfStages: int
    def __init__(self, _projectId: _Optional[str] = ..., startingStage: _Optional[int] = ..., numberOfStages: _Optional[int] = ...) -> None: ...

class DeleteStagesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteStagesByListRequest(_message.Message):
    __slots__ = ("_projectId", "stageIndices")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    STAGEINDICES_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    stageIndices: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, _projectId: _Optional[str] = ..., stageIndices: _Optional[_Iterable[int]] = ...) -> None: ...

class DeleteStagesByListResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

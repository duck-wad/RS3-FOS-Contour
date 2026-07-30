from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StageFactorProperty(_message.Message):
    __slots__ = ("stageFactorID", "stageAppliedTo")
    STAGEFACTORID_FIELD_NUMBER: _ClassVar[int]
    STAGEAPPLIEDTO_FIELD_NUMBER: _ClassVar[int]
    stageFactorID: str
    stageAppliedTo: int
    def __init__(self, stageFactorID: _Optional[str] = ..., stageAppliedTo: _Optional[int] = ...) -> None: ...

class GetDefinedStageFactorsRequest(_message.Message):
    __slots__ = ("propertyID",)
    PROPERTYID_FIELD_NUMBER: _ClassVar[int]
    propertyID: str
    def __init__(self, propertyID: _Optional[str] = ...) -> None: ...

class GetDefinedStageFactorsResponse(_message.Message):
    __slots__ = ("stageFactors",)
    STAGEFACTORS_FIELD_NUMBER: _ClassVar[int]
    stageFactors: _containers.RepeatedCompositeFieldContainer[StageFactorProperty]
    def __init__(self, stageFactors: _Optional[_Iterable[_Union[StageFactorProperty, _Mapping]]] = ...) -> None: ...

class GetStageFactorRequest(_message.Message):
    __slots__ = ("propertyID", "stage")
    PROPERTYID_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    propertyID: str
    stage: int
    def __init__(self, propertyID: _Optional[str] = ..., stage: _Optional[int] = ...) -> None: ...

class GetStageFactorResponse(_message.Message):
    __slots__ = ("stageFactor",)
    STAGEFACTOR_FIELD_NUMBER: _ClassVar[int]
    stageFactor: StageFactorProperty
    def __init__(self, stageFactor: _Optional[_Union[StageFactorProperty, _Mapping]] = ...) -> None: ...

class CreateStageFactorRequest(_message.Message):
    __slots__ = ("propertyID", "stage", "useJointOptions")
    PROPERTYID_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    USEJOINTOPTIONS_FIELD_NUMBER: _ClassVar[int]
    propertyID: str
    stage: int
    useJointOptions: bool
    def __init__(self, propertyID: _Optional[str] = ..., stage: _Optional[int] = ..., useJointOptions: bool = ...) -> None: ...

class CreateStageFactorResponse(_message.Message):
    __slots__ = ("stageFactor",)
    STAGEFACTOR_FIELD_NUMBER: _ClassVar[int]
    stageFactor: StageFactorProperty
    def __init__(self, stageFactor: _Optional[_Union[StageFactorProperty, _Mapping]] = ...) -> None: ...

class SetDefinedStageFactorsRequest(_message.Message):
    __slots__ = ("propertyID", "stageFactorDictionary", "isRelativeStageFactors", "useJointOptions")
    class StageFactorDictionaryEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: StageFactorProperty
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[StageFactorProperty, _Mapping]] = ...) -> None: ...
    PROPERTYID_FIELD_NUMBER: _ClassVar[int]
    STAGEFACTORDICTIONARY_FIELD_NUMBER: _ClassVar[int]
    ISRELATIVESTAGEFACTORS_FIELD_NUMBER: _ClassVar[int]
    USEJOINTOPTIONS_FIELD_NUMBER: _ClassVar[int]
    propertyID: str
    stageFactorDictionary: _containers.MessageMap[int, StageFactorProperty]
    isRelativeStageFactors: bool
    useJointOptions: bool
    def __init__(self, propertyID: _Optional[str] = ..., stageFactorDictionary: _Optional[_Mapping[int, StageFactorProperty]] = ..., isRelativeStageFactors: bool = ..., useJointOptions: bool = ...) -> None: ...

class SetDefinedStageFactorsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

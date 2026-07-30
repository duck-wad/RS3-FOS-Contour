from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RestraintsBase(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class setAutoRestraintsRequest(_message.Message):
    __slots__ = ("_projectId", "autoRestraintTypeValue")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    AUTORESTRAINTTYPEVALUE_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    autoRestraintTypeValue: int
    def __init__(self, _projectId: _Optional[str] = ..., autoRestraintTypeValue: _Optional[int] = ...) -> None: ...

class setAutoRestraintsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class deleteAllRestraintsRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class deleteAllRestraintsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class getIsRestraintsSetRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class getIsRestraintsSetResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: bool = ...) -> None: ...

class setResetAllDisplacementsRequest(_message.Message):
    __slots__ = ("_projectId", "resetDisplacementsAfterStages", "stageNames")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    RESETDISPLACEMENTSAFTERSTAGES_FIELD_NUMBER: _ClassVar[int]
    STAGENAMES_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    resetDisplacementsAfterStages: bool
    stageNames: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, _projectId: _Optional[str] = ..., resetDisplacementsAfterStages: bool = ..., stageNames: _Optional[_Iterable[str]] = ...) -> None: ...

class setResetAllDisplacementsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class getIsResetAllDisplacementsAfterStagesRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class getIsResetAllDisplacementsAfterStagesResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bool
    def __init__(self, result: bool = ...) -> None: ...

class getResetAllDisplacementsStagesRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class getResetAllDisplacementsStagesResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[_Iterable[str]] = ...) -> None: ...

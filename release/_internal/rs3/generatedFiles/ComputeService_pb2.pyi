from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ComputeServiceBase(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class computeRequest(_message.Message):
    __slots__ = ("_projectId", "computeType", "computeStart")
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    COMPUTETYPE_FIELD_NUMBER: _ClassVar[int]
    COMPUTESTART_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    computeType: str
    computeStart: str
    def __init__(self, _projectId: _Optional[str] = ..., computeType: _Optional[str] = ..., computeStart: _Optional[str] = ...) -> None: ...

class computeResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class readStagesSSRConvergenceStatusRequest(_message.Message):
    __slots__ = ("_projectId",)
    _PROJECTID_FIELD_NUMBER: _ClassVar[int]
    _projectId: str
    def __init__(self, _projectId: _Optional[str] = ...) -> None: ...

class readStagesSSRConvergenceStatusResponse(_message.Message):
    __slots__ = ("success", "errorMessage", "isRecovery", "stagesConvergence", "srfValuesConvergence")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERRORMESSAGE_FIELD_NUMBER: _ClassVar[int]
    ISRECOVERY_FIELD_NUMBER: _ClassVar[int]
    STAGESCONVERGENCE_FIELD_NUMBER: _ClassVar[int]
    SRFVALUESCONVERGENCE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    errorMessage: str
    isRecovery: bool
    stagesConvergence: _containers.RepeatedCompositeFieldContainer[convergenceStatus]
    srfValuesConvergence: _containers.RepeatedCompositeFieldContainer[convergenceStatus]
    def __init__(self, success: bool = ..., errorMessage: _Optional[str] = ..., isRecovery: bool = ..., stagesConvergence: _Optional[_Iterable[_Union[convergenceStatus, _Mapping]]] = ..., srfValuesConvergence: _Optional[_Iterable[_Union[convergenceStatus, _Mapping]]] = ...) -> None: ...

class convergenceStatus(_message.Message):
    __slots__ = ("index", "converged")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    CONVERGED_FIELD_NUMBER: _ClassVar[int]
    index: int
    converged: bool
    def __init__(self, index: _Optional[int] = ..., converged: bool = ...) -> None: ...

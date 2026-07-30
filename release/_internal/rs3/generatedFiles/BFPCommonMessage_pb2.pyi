from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ElementNodalValues(_message.Message):
    __slots__ = ("axisForce", "shearForceMinAxis", "shearForceMaxAxis", "momentMinAxis", "momentMaxAxis", "displacementX", "displacementY", "displacementZ", "totalDisplacement")
    AXISFORCE_FIELD_NUMBER: _ClassVar[int]
    SHEARFORCEMINAXIS_FIELD_NUMBER: _ClassVar[int]
    SHEARFORCEMAXAXIS_FIELD_NUMBER: _ClassVar[int]
    MOMENTMINAXIS_FIELD_NUMBER: _ClassVar[int]
    MOMENTMAXAXIS_FIELD_NUMBER: _ClassVar[int]
    DISPLACEMENTX_FIELD_NUMBER: _ClassVar[int]
    DISPLACEMENTY_FIELD_NUMBER: _ClassVar[int]
    DISPLACEMENTZ_FIELD_NUMBER: _ClassVar[int]
    TOTALDISPLACEMENT_FIELD_NUMBER: _ClassVar[int]
    axisForce: float
    shearForceMinAxis: float
    shearForceMaxAxis: float
    momentMinAxis: float
    momentMaxAxis: float
    displacementX: float
    displacementY: float
    displacementZ: float
    totalDisplacement: float
    def __init__(self, axisForce: _Optional[float] = ..., shearForceMinAxis: _Optional[float] = ..., shearForceMaxAxis: _Optional[float] = ..., momentMinAxis: _Optional[float] = ..., momentMaxAxis: _Optional[float] = ..., displacementX: _Optional[float] = ..., displacementY: _Optional[float] = ..., displacementZ: _Optional[float] = ..., totalDisplacement: _Optional[float] = ...) -> None: ...

class InterfaceNodalValues(_message.Message):
    __slots__ = ("shearForce", "normalForceMinAxis", "normalForceMaxAxis", "confiningStress", "rockDisplacementX", "rockDisplacementY", "rockDisplacementZ", "rockTotalDisplacement")
    SHEARFORCE_FIELD_NUMBER: _ClassVar[int]
    NORMALFORCEMINAXIS_FIELD_NUMBER: _ClassVar[int]
    NORMALFORCEMAXAXIS_FIELD_NUMBER: _ClassVar[int]
    CONFININGSTRESS_FIELD_NUMBER: _ClassVar[int]
    ROCKDISPLACEMENTX_FIELD_NUMBER: _ClassVar[int]
    ROCKDISPLACEMENTY_FIELD_NUMBER: _ClassVar[int]
    ROCKDISPLACEMENTZ_FIELD_NUMBER: _ClassVar[int]
    ROCKTOTALDISPLACEMENT_FIELD_NUMBER: _ClassVar[int]
    shearForce: float
    normalForceMinAxis: float
    normalForceMaxAxis: float
    confiningStress: float
    rockDisplacementX: float
    rockDisplacementY: float
    rockDisplacementZ: float
    rockTotalDisplacement: float
    def __init__(self, shearForce: _Optional[float] = ..., normalForceMinAxis: _Optional[float] = ..., normalForceMaxAxis: _Optional[float] = ..., confiningStress: _Optional[float] = ..., rockDisplacementX: _Optional[float] = ..., rockDisplacementY: _Optional[float] = ..., rockDisplacementZ: _Optional[float] = ..., rockTotalDisplacement: _Optional[float] = ...) -> None: ...

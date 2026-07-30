import CommonMessages_pb2 as _CommonMessages_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompositeLiner(_message.Message):
    __slots__ = ("linerName", "hasUpperJoint", "upperJointName", "hasLowerJoint", "lowerJointName", "installationStage", "isRemoved", "removalStage")
    LINERNAME_FIELD_NUMBER: _ClassVar[int]
    HASUPPERJOINT_FIELD_NUMBER: _ClassVar[int]
    UPPERJOINTNAME_FIELD_NUMBER: _ClassVar[int]
    HASLOWERJOINT_FIELD_NUMBER: _ClassVar[int]
    LOWERJOINTNAME_FIELD_NUMBER: _ClassVar[int]
    INSTALLATIONSTAGE_FIELD_NUMBER: _ClassVar[int]
    ISREMOVED_FIELD_NUMBER: _ClassVar[int]
    REMOVALSTAGE_FIELD_NUMBER: _ClassVar[int]
    linerName: str
    hasUpperJoint: bool
    upperJointName: str
    hasLowerJoint: bool
    lowerJointName: str
    installationStage: int
    isRemoved: bool
    removalStage: int
    def __init__(self, linerName: _Optional[str] = ..., hasUpperJoint: bool = ..., upperJointName: _Optional[str] = ..., hasLowerJoint: bool = ..., lowerJointName: _Optional[str] = ..., installationStage: _Optional[int] = ..., isRemoved: bool = ..., removalStage: _Optional[int] = ...) -> None: ...

class SetCompositeLinerRequest(_message.Message):
    __slots__ = ("liningId", "compositeLiner")
    LININGID_FIELD_NUMBER: _ClassVar[int]
    COMPOSITELINER_FIELD_NUMBER: _ClassVar[int]
    liningId: str
    compositeLiner: _containers.RepeatedCompositeFieldContainer[CompositeLiner]
    def __init__(self, liningId: _Optional[str] = ..., compositeLiner: _Optional[_Iterable[_Union[CompositeLiner, _Mapping]]] = ...) -> None: ...

class SetCompositeLinerResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCompositeLinerRequest(_message.Message):
    __slots__ = ("liningId",)
    LININGID_FIELD_NUMBER: _ClassVar[int]
    liningId: str
    def __init__(self, liningId: _Optional[str] = ...) -> None: ...

class GetCompositeLinerResponse(_message.Message):
    __slots__ = ("compositeLiner",)
    COMPOSITELINER_FIELD_NUMBER: _ClassVar[int]
    compositeLiner: _containers.RepeatedCompositeFieldContainer[CompositeLiner]
    def __init__(self, compositeLiner: _Optional[_Iterable[_Union[CompositeLiner, _Mapping]]] = ...) -> None: ...

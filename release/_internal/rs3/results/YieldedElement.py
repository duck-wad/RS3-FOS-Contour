import rs3.generatedFiles.GaussPointFailureMessage_pb2 as GaussPointFailureMessage_pb2
from typing import Type

class GaussPointFailure:
    def __init__(self, grpcGaussPointFailure: GaussPointFailureMessage_pb2.GaussPointFailure, failureTypeEnum: Type):
        self._grpcGaussPointFailure = grpcGaussPointFailure
        self._failureType = failureTypeEnum(grpcGaussPointFailure.failureType)

    @property
    def XCoordinate(self):
        return self._grpcGaussPointFailure.location.x

    @property
    def YCoordinate(self):
        return self._grpcGaussPointFailure.location.y

    @property
    def ZCoordinate(self):
        return self._grpcGaussPointFailure.location.z

    @property
    def FailureType(self):
        return self._failureType


class YieldedElement:
    def __init__(self, grpcGaussPointFailure: GaussPointFailureMessage_pb2.GaussPointFailure, failureTypeEnum: Type):
        self._failurePoint = GaussPointFailure(grpcGaussPointFailure, failureTypeEnum=failureTypeEnum)

    def getFailurePoint(self) -> GaussPointFailure:
        return self._failurePoint

        
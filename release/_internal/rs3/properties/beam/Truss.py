from rs3._client import Client
from rs3.properties.stageFactors.StageFactorInterfaces import AbsoluteStageFactorInterface
from rs3.properties.PropertyEnums import *
from rs3.properties.beam import BeamCommon

class Truss(BeamCommon.BeamCommon):
    """
    Truss structural element.

    This class represents a truss member and **inherits all common beam
    properties, methods, and behaviors** from :class:`BeamCommon.BeamCommon`.

    No additional intrinsic properties are defined at the truss level beyond
    what is provided by ``BeamCommon``. Users should refer to
    ``BeamCommon.py`` for the complete list of available properties and
    interfaces.

    Examples:
        See :ref:`beam_example`.
    """
    def __init__(self, client: Client, id: str):
        super().__init__(client, id)
        self.StageFactorInterface = AbsoluteStageFactorInterface[BeamCommon.BeamCommonDefinedStageFactor, BeamCommon.BeamCommonStageFactor](id, client, BeamCommon.BeamCommonDefinedStageFactor, BeamCommon.BeamCommonStageFactor)
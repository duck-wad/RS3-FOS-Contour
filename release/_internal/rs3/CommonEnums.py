from enum import Enum
    
class LinearDirectionType(Enum):
    TREND_PLUNGE = "LINEAR_DIRECTION_TREND_PLUNGE"
    NORMAL_VECTOR = "LINEAR_DIRECTION_VECTOR"

class AutoRestraintsType(Enum):
    # NONE = 0
    UNDERGROUND = 1
    SURFACE_PINS = 2
    SURFACE_ROLLERS = 3
    
class ExternalVolumeRoles(Enum):
    GEOLOGY = "Geology"
    CONSTRUCTION = "Construction"
    EXCAVATION = "Excavation"
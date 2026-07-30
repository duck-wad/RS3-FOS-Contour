from enum import Enum

class ComputeType(Enum):
    ALL = "ALL"
    GROUNDWATER_ONLY = "GW_ONLY"
    
class ComputeStart(Enum):
    AFTER_LAST_COMPUTED_STAGE = "AFTER_LAST_COMPUTED_STAGE"
    FROM_BEGINNING = "FROM_BEGINNING"
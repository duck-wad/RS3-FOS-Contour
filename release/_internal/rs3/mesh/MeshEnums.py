from enum import Enum

class MeshElementType(Enum):
    MESH_4_NODED_TETRAHEDRA = "TET4"
    MESH_10_NODED_TETRAHEDRA = "TET10"
    MESH_MIXED_4_NODED_AND_10_NODED_TETRAHEDRA = "TET4AND10"
    
class MeshGradation(Enum):
    GRADED = "GRADED"
    UNIFORM = "UNIFORM"
    
class MeshDensity(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    USER_DEFINED = "USERDEFINED"
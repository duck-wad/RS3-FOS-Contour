from enum import Enum

# stage factors
class StageFactorMethodType(Enum):
    ABSOLUTE_STAGE_FACTOR = 0
    RELATIVE_STAGE_FACTOR = 1

# bolts
class BoltTypes(Enum):
    END_ANCHORED = "END_ANCHORED"
    FULLY_BONDED = "FULLY_BONDED"
    PLAIN_STRAND_CABLE = "PLAIN_STRAND_CABLE"
    SWELLEX = "SWELLEX_BOLT"
    TIEBACK = "TIEBACK_BOLT"
class BulgeTypes(Enum):
    GARFORD_BULB_25MM = "twentyfive_GARFORD_BULB"
    NUT_CASE_21MM = "twentyone_NUT_CASE"
class BondLengthType(Enum):
    PERCENT_OF_LENGTH = 0
    LENGTH = 1
class SecondaryBondLengthType(Enum): # int values below are directly associated with constants in RS3BoltData.cs - do not change
    PERCENTAGE_OF_LENGTH = 1
    LENGTH = 2
    FULLY_BONDED = 3

# beams
class BeamType(Enum):
    STANDARD_BEAM = "STANDARD"
    TRUSS = "TRUSS"
class BeamElementFormulation(Enum):
    BERNOULLI = "BERNOULLI"
    TIMOSHENKO = "TIMOSHENKO"
    
# liners
class LinerTypes(Enum):
    STANDARD = "STANDARD"
    GEOSYNTHETIC = "GEOSYNTHETIC"
    REINFORCED_CONCRETE = "REINFORCED_CONCRETE" 

# joints
class JointConstitutiveModelTypes(Enum):
    NONE = "NONE"
    MOHR_COULOMB = "MOHR_COULOMB"
    BARTON_BANDIS = "BARTON_BANDIS"
    GEOSYNTHETIC_HYPERBOLIC = "GEOSYNTHETIC_HYPERBOLIC"
    MATERIAL_DEPENDENT = "MATERIAL_DEPENDENT"
    
class AdditionalPressureType(Enum):
	PRESSURE = False
	PIEZOMETRIC_SURFACE = True
 
# pile
class PileSkinResistanceType(Enum):
    LINEAR = "LINEAR"
    MOHR_COULOMB = "CANDPHI"
    MULTI_LINEAR = "MULTILINEAR"
    
class ConnectionType(Enum):
    FREE = "FREE"
    HINGED = "HINGED"
    RIGID = "RIGID"

class LiningConnectionType(Enum):
    FIRST_LINER_AT_INSTALL = "FIRST_LINER_AT_INSTALL"
    ALL_LINERS = "ALL_LINERS"
    
class EndConditionType(Enum):
    NONE = False
    FORCE = "FORCE"
    DISPLACEMENT = "DISPLACEMENT"
    
class EndConditionPlacementPoint(Enum):
    TOP = "TOP"
    BOTTOM = "BOTTOM"

# groundwater
class GroundwaterInterpolationMethodType(Enum):
    INVERSE_DISTANCE = "InverseDistance"
    THIN_PLATE_SPLINE = "ThinPlateSpline"
    CHUGH = "Chugh"
    LOCAL_THIN_PLATE_SPLINE = "LocalThinPlateSpline"
    LINEAR_TRIANGULATION = "TINTriangulation"
    GAUSSIAN = "Gaussian"
    MULTI_QUADRATIC = "MultiQuadratic"
    POLYHARMONIC_SPLINE = "PolyharmonicSpline"
    COMPACTLY_SUPPORTED = "CompactlySupported"
    
class GroundwaterResolutionMethodType(Enum):
    COARSE = "Coarse"
    STANDARD = "Standard"
    FINE = "Fine"

class WaterGridPlane2DType(Enum):
    XZ_PLANE = "XZ_PLANE"
    YZ_PLANE = "YZ_PLANE"

class WaterGridInterpolationMethodType(Enum):
    HYBRID = "HybridAuto"
    THIN_PLATE_SPLINE = "ThinPlateSpline"
    HARDYS_MULTI_QUADRATIC = "HardysMultiQuadratic"
    KRIGING = "Kriging"
    INVERSE_DISTANCE = "InverseDistance"
    
class WaterGridPointSetType(Enum):
    PORE_PRESSURE = "PorePressure"
    PRESSURE_HEAD = "PressureHead"
    TOTAL_HEAD = "TotalHead"

# materials
class InitialElementLoadingType(Enum):
    FIELD_STRESS_ONLY = "FIELD_STRESS_ONLY"
    FIELD_STRESS_AND_BODY_FORCE = "BOTH_FIELD_AND_BODY"
    BODY_FORCE_ONLY = "BODY_FORCE_ONLY"
    NONE = "NONE"

class MaterialElasticityTypes(Enum):
    LINEAR_ISOTROPIC = "ISOTROPIC"
    TRANSVERSELY_ISOTROPIC = "TRANSVERSELY_ISOTROPIC"
    ORTHOTROPIC = "ORTHOTROPIC"
    DUNCAN_CHANG_HYPERBOLIC = "DUNCAN_CHANG_HYPERBOLIC"
    NON_LINEAR_ISOTROPIC = "NON_LINEAR_ISOTROPIC"
    
class UnloadingConditions(Enum):
    MEAN_STRESS = "LU_p"
    DEVIATORIC_STRESS = "LU_q"
    VOLUMETRIC_STRAIN = "LU_EpsV"
    DEVIATORIC_STRAIN = "LU_Epqscan"
    
class NonlinearIsotropicFormulaType(Enum):
    FORMULA_1 = "FORMULA_1"
    FORMULA_2 = "FORMULA_2"
    FORMULA_3 = "FORMULA_3"

class PoissonRatioType(Enum):
    CONSTANT = "CONSTANT"
    STRESS_DEPENDENT = "STRESS_DEPENDENT"
    
class ElasticParametersType(Enum):
    CONSTANT_SHEAR_MODULUS = "CONSTANT_SHEAR_MODULUS"
    CONSTANT_POISSON_RATIO = "CONSTANT_POISSON_RATIO"
    
class PlanarDirectionType(Enum):
    DIP_DIRECTION_AND_DIP = "DIP_DIRECTION_AND_DIP"
    NORMAL_VECTOR = "NORMAL_VECTOR"
    
class GeneralizedHoekBrownEstimationMethodType(Enum):
    GENERALIZED_HOEK_DIEDERICHS = "GENERALIZED_HOEK_DIEDERICHS"
    SIMPLIFIED_HOEK_DIEDERICHS = "SIMPLIFIED_HOEK_DIEDERICHS"
    HOEK_CARRANZA_TORRES_CORKUM = "HOEK_CARRANZA_TORRES_CORKUM"

class ConstitutiveModelTypes(Enum):
    MOHR_COULOMB = "MOHR_COULOMB"
    HOEK_BROWN = "HOEK_BROWN"
    DRUCKER_PRAGER = "DRUCKER_PRAGER"
    GENERALIZED_HOEK_BROWN = "GENERALIZED_HOEK_BROWN"
    CAM_CLAY = "CAM_CLAY"
    MODIFIED_CAM_CLAY = "MODIFIED_CAM_CLAY"
    DISCRETE_FUNCTION = "DISCRETE_FUNCTION"
    MOHR_COULOMB_WITH_CAP = "MOHR_COULOMB_WITH_CAP"
    SOFTENING_HARDENING_MODEL = "SOFTENING_HARDENING_MODEL"
    BOUNDING_SURFACE_PLASTICITY = "BOUNDING_SURFACE_PLASTICITY"
    MANZARI_AND_DAFALIAS = "MANZARI_AND_DAFALIAS"
    JOINTED_MOHR_COULOMB = "JOINTED_MOHR_COULOMB"
    JOINTED_GENERALIZED_HOEK_BROWN = "JOINTED_GENERALIZED_HOEK_BROWN"
    BARTON_BANDIS = "BARTON_BANDIS"
    HYPERBOLIC = "HYPERBOLIC"
    POWER_CURVE = "POWER_CURVE"
    CH_SOIL = "CH_SOIL"
    CY_SOIL = "CY_SOIL"
    DOUBLE_YIELD = "DOUBLE_YIELD"
    HARDENING_SOIL = "HARDENING_SOIL"
    HARDENING_SOIL_SMALL_STRAIN_STIFFNESS = "HARDENING_SOIL_SMALL_STRAIN_STIFFNESS"
    SOFT_SOIL = "SOFT_SOIL"
    SOFT_SOIL_CREEP = "SOFT_SOIL_CREEP"
    SWELLING_ROCK = "SWELLING_ROCK"
    SHANSEP = "SHANSEP"
    BARCELONA_BASIC = "BARCELONA_BASIC"
    NORSAND = "NORSAND"
    SHEAR_NORMAL_FUNCTION = "SHEAR_NORMAL_FUNCTION"
    SNOWDEN_MODIFIED_ANISOTROPIC_LINEAR = "SNOWDEN_MODIFIED_ANISOTROPIC_LINEAR"
    ANISOTROPIC_LINEAR = "ANISOTROPIC_LINEAR"
    GENERALIZED_ANISOTROPIC = "GENERALIZED_ANISOTROPIC"
    VERTICAL_STRESS_RATIO = "VERTICAL_STRESS_RATIO"
    
class MaterialType(Enum):
    ELASTIC = False
    PLASTIC = True
    
class GeneralizedHoekBrownDefinedType(Enum):
    MB_S_A = "MB_S_A"
    GSIType = "GSIType"
    
class SpecificVolumeAtUnitPressureType(Enum):
    NORMAL_COMPRESSION_LINE_N = "NORMAL_COMPRESSION_LINE_N"
    CRITICAL_STATE_LINE_GAMMA = "CRITICAL_STATE_LINE_GAMMA"
    
class InitialStateOfConsolidationType(Enum):
    OVERCONSOLIDATION_RATIO_OCR = "OVERCONSOLIDATION_RATIO_OCR"
    PRECONSOLIDATION_PRESSURE_PO = "PRECONSOLIDATION_PRESSURE_PO"
    
class CapType(Enum):
    NONE = "NONE"
    VERTICAL = "VERTICAL"
    ELLIPTICAL = "ELLIPTICAL"
    
class CapHardeningTypes(Enum):
    TABULAR = 0
    EXPONENTIAL = 1
    
class ConeHardeningTypes(Enum):
    TABULAR = 0
    HARDENING_PROPERTY = 1
    
class DilationTypes(Enum):
    DILATION_ANGLE = 0
    DILATION_COMPACTION = 1
    
class CySoilCapOption(Enum):
    NONE = "NONE"
    ELLIPTICAL = "ELLIPTICAL"
    
class DoubleYieldCapType(Enum):
    NONE = "NONE"
    VERTICAL = "VERTICAL"
    
class DilationOption(Enum):
    DILATION_ONLY = "DILATION_ONLY"
    DILATION_ROWES = "ROWES"
    
class PlaxisDilationOptionType(Enum):
    CONDITIONAL = "CONDITIONAL"
    ROWES = "ROWES"
    
class InitialConsolidationConditionType(Enum):
    OVER_CONSOLIDATION_RATIO = "OVER_CONSOLIDATION_RATIO"
    INITIAL_MEAN_STRESS = "INITIAL_MEAN_STRESS"
    
class NorsandInitialConsolidationConditionType(Enum):
    OVER_CONSOLIDATION_RATIO = "OVERCONSOLIDATION_RATIO"
    INITIAL_MEAN_STRESS = "INITIAL_MEAN_STRESS"
    
class Dilatancy(Enum):
    DILATANCY_DEACTIVATED = "DEACVTIVATED"
    DILATANCY_ACTIVATED = "ACTIVATED"
    
class SwellingForm(Enum):
    WITTKE = "WITTKE"
    ANAGNOSTOU = "ANAGNOSTOU"
    
class WaterCondition(Enum):
    SWELLING = "SWELLING"
    SWELLING_WITH_WATER  = "SWELLING_AT_WATER"
    
class StressHistoryTypes(Enum):
    OVER_CONSOLIDATION_OCR = "OVERCONSOLIDATION_RATIO"
    PRECONSOLIDATION_PRESSURE_PC = "PRECONSOLIDATION_PRESSURE"
    
class StressHistoryDefinitionMethods(Enum):
    STRESS_HISTORY_CONSTANT = "CONSTANT"
    STRESS_HISTORY_DEPTH = "DEPTH"
    STRESS_HISTORY_ELEVATION = "ELEVATION"
    
class AnisotropyDefinitionType(Enum):
    PLANE_DEFINITION = "PLANE_DEFINITION"
    SURFACE = "SURFACE"
    
class GeneralizedAnisotropyDefinitionType(Enum):
    DIP_DIPDIR = "DIP_DIPDIR"
    SURFACE = "SURFACE"
    
class TensileCutoffOptions(Enum):
    NONE = "NONE"
    HOEK_MARTIN = "HOEK_MARTIN"
    USER_DEFINED = "USER_DEFINED"
    
class DiscreteDrainedMode(Enum):
    UNDRAINED = "DF_UNDRAINED"
    DRAINED = "DF_DRAINED"
    
class Plane2DType(Enum):
    XZ_PLANE = "XZ_PLANE"
    YZ_PLANE = "YZ_PLANE"
    
class DiscreteFunctionInterpolationMethodType(Enum):
    HYBRID = "HybridAuto"
    THIN_PLATE_SPLINE = "ThinPlateSpline"
    KRIGING = "Kriging"
    INVERSE_DISTANCE = "InverseDistance"
    MODIFIED_CHUGH = "ModifiedChugh"

class PlaneOrientationType(Enum):
    LINEAR_DIRECTION_TREND_PLUNGE = "LINEAR_DIRECTION_TREND_PLUNGE"
    DIP_DIRECTION_AND_DIP = "DIP_DIRECTION_AND_DIP"
    NORMAL_VECTOR = "LINEAR_DIRECTION_VECTOR"
    
class MaterialJointSlipCriterionType(Enum):
    MOHR_COULOMB = "MOHR_COULOMB"
    BARTON_BANDIS = "BARTON_BANDIS"
    HYPERBOLIC_SIMPLE = "HYPERBOLIC_SIMPLE"
    
class SnowdenStrengthFunctionType(Enum):
    SHEAR_NORMAL = "SHEAR_NORMAL"
    COHESION_FRICTION = "COHESION_FRICTION"

class MaterialBehaviours(Enum):
    DRAINED = "DRAINED"
    UNDRAINED = "UNDRAINED"
    
class PorosityType(Enum):
    POROSITY = "POROSITY"
    VOID_RATIO = "VOID_RATIO"
    
class HydraulicMethodType(Enum):
    LINEAR_ISOTROPIC = "ISOTROPIC"
    TRANSVERSELY_ISOTROPIC = "TRANSVERSELY_ISOTROPIC"
    ORTHOTROPIC = "ORTHOTROPIC"
    
class EnhancedSimpleSoilTypes(Enum):
    CLAY = "CLAY"
    GENERAL = "GENERAL"
    LOAM = "LOAM"
    SAND = "SAND"
    SILT = "SILT"
    
class HydraulicModelType(Enum):
    BROOKS_AND_COREY = 0
    FREDLUND_AND_XING = 1
    GARDNER = 2
    SIMPLE = 3
    VAN_GENUCHTEN = 4
    CUSTOM = -1
    
class HuTypes(Enum):
    CUSTOM = "Custom"
    AUTO = "Auto"
    
class HydraulicParameterType(Enum):
    PWP = "PWP"
    RU = "RU"
    
class StaticWaterModes(Enum):
    DRY = "DRY"
    WATER_SURFACE = "WATER_SURFACE"
    PWP_INTERPOLATION_SURFACE = "PWP_INTERPOLATION_SURFACE"
    USER_DEFINED_VALUE = "USER_DEFINED_VALUE"
    PWP_POINT_SET = "PWP_POINT_SET"
    
class WCInputType(Enum):
    BY_WATER_CONTENT = 'WATERCONTENT'
    BY_DEGREE_OF_SATURATION = 'DEGREEOFSATURATION'
    
class DatumType(Enum):
    DEPTH = "Depth"
    RADIAL = "Radial"
    
class DatumDependencyIndex(Enum):
    YOUNGS_MODULUS = "YOUNGS_MODULUS"
    COHESION = "COHESION"
    FRICTION_ANGLE = "FRICTION_ANGLE"
    UNLOADING_YOUNGS_MODULUS = "UNLOADING_YOUNGS_MODULUS"
    
class UnsaturatedParameterType(Enum):
    NONE = "NONE"
    SINGLE_EFFECTIVE_STRESS = "SINGLE_EFFECTIVE_STRESS"
    
class MohrCoulombUnsaturatedParameterType(Enum):
    NONE = "NONE"
    UNSATURATED_SHEAR_STRENGTH = "UNSATURATED_SHEAR_STRENGTH"
    SINGLE_EFFECTIVE_STRESS = "SINGLE_EFFECTIVE_STRESS"
    
class UnsaturatedShearStrengthType(Enum):
	FREDLUND = "FREDLUND"
	VANAPALLI = "VANAPALLI"
    
class UnsaturatedSingleEffectiveStressMethod(Enum):
    BISHOP = "BISHOP"
    TABULAR_VALUE = "TABULAR"
    GUDEHUS_1995 = "GUDEHUS"
    KHALILI_2004 = "KHALILI"
    BOLZON_1996 = "BOLTZON"
    AITCHISON_1960 = "AITCHISON"
    KOHGO_1993 = "KOHGO"
    
class UnsaturatedTabularValueMethod(Enum):
    WITH_RESPECT_TO_SUCTION = "SUCTION"
    WITH_RESPECT_TO_DEGREE_OF_SATURATION = "DEGREE_OF_SATURATION"
    WITH_RESPECT_TO_EFFECTIVE_DEGREE_OF_SATURATION = "EFFECTIVE_DEGREE_OF_SATURATION"
from typing import List, Dict, Optional, Union, Iterable
import unicodedata as ud
import re
from rs3.results.ResultEnums import SolidsDataType

import rs3.generatedFiles.SolidsResultsQueryService_pb2 as SolidsResultsQueryService_pb2

class SolidNodalResults:
    '''
    Nodal result wrapper with per-material data access.

    Notes:
        - EntityNames/EntityIDs correspond to owning entities for this node.
        - getResult(dataType, materialName=None) returns the average across materials when materialName is None.
    '''
    _NON_MATERIAL_RESULT_ENUMS = (
        SolidsDataType.DISPLACEMENT_X,
        SolidsDataType.DISPLACEMENT_Y,
        SolidsDataType.DISPLACEMENT_Z,
        SolidsDataType.EXCESS_PWP,
        SolidsDataType.TOTAL_PWP,
    )

    def __init__(self, grpcNodalResults, dataTypeToIndexMap: Dict["SolidsDataType", int]):
        self._grpcNodalResults = grpcNodalResults
        self._materialProperties = self._setMaterialProperties(grpcNodalResults.materialValues)
        self._materialDataQuery = _DataTypeQuery(grpcNodalResults.materialValues, dataTypeToIndexMap)
    
    @property
    def NodeID(self):
        return self._grpcNodalResults.nodeInformation.nodeID

    @property
    def XCoordinate(self):
        return self._grpcNodalResults.nodeInformation.location.x
    
    @property
    def YCoordinate(self):
        return self._grpcNodalResults.nodeInformation.location.y
    
    @property
    def ZCoordinate(self):
        return self._grpcNodalResults.nodeInformation.location.z
    

    @property
    def EntityNames(self):
        return list(self._grpcNodalResults.entityNames)

    @property
    def EntityIDs(self):
        return list(self._grpcNodalResults.entityIDs)

    @property
    def MaterialProperties(self):
        return self._materialProperties

    def getResult(self, dataType: Union[str, "SolidsDataType"], materialName: Optional[str] = None) -> float:
        '''
        Get a nodal result by data type.

        Parameters:
            dataType: Union[str, SolidsDataType]
                Either a `SolidsDataType` enum member or a free-form string.
                Free-form strings are normalized (NFKC + casefold + separators removed)
                and resolved against `SolidsDataAlias.alias`.
                Examples: SolidsDataType.SIGMA_1_EFFECTIVE, "sigma1", "Stress P Major".

            materialName: Optional[str]
                When provided, return the value for that specific material.
                When None, return the average across materials.

        Returns:
            float: The requested value (material-specific or averaged).
        '''
        if self._dataTypeNonMaterialResult(dataType):
            return self._getNonMaterialResult(dataType)
        
        if materialName is not None and materialName not in self._materialProperties:
            raise ValueError(f"Material {materialName} not found")
        return self._materialDataQuery.getDataType(dataType).getResult(materialName)
            
    def _setMaterialProperties(self, materialProperties: List[SolidsResultsQueryService_pb2.MaterialResults]):
        uniqueNames: list[str] = []
        seen : set[str] = set()
        for mp in materialProperties:
            if mp.materialName not in seen:
                uniqueNames.append(mp.materialName)
                seen.add(mp.materialName)
        return sorted(uniqueNames)
        

# region non-material result

    def _dataTypeNonMaterialResult(self, dataType: Union[str, "SolidsDataType"]) -> bool:
        if isinstance(dataType, SolidsDataType):
            return dataType in self._NON_MATERIAL_RESULT_ENUMS
        normalized = _DataTypeNameNormalizer.normalizeDataTypeName(dataType)
        return normalized in {_DataTypeNameNormalizer.normalizeDataTypeName(dt.name) for dt in self._NON_MATERIAL_RESULT_ENUMS}

    def _getNonMaterialResult(self, dataType: Union[str, "SolidsDataType"]) -> float:
        resolved: SolidsDataType
        if isinstance(dataType, SolidsDataType):
            resolved = dataType
        else:
            normalized = _DataTypeNameNormalizer.normalizeDataTypeName(dataType)
            normalized_to_enum = {_DataTypeNameNormalizer.normalizeDataTypeName(dt.name): dt for dt in self._NON_MATERIAL_RESULT_ENUMS}
            if normalized not in normalized_to_enum:
                available = [dt.name for dt in self._NON_MATERIAL_RESULT_ENUMS]
                raise ValueError(f"Invalid data type: {dataType}. Available: {available}")
            resolved = normalized_to_enum[normalized]
        return getattr(self._grpcNodalResults.nodalValues, resolved.value)

# endregion non-material results


# region Material Results

class SolidsDataAlias:
    alias = {
        SolidsDataType.SIGMA_1_EFFECTIVE: {"stress p major"},
        SolidsDataType.SIGMA_2_EFFECTIVE: {"stress p mean"},
        SolidsDataType.SIGMA_3_EFFECTIVE: {"stress p minor"},
        
        # todo: add more aliases
    }
    

class _DataTypeNameNormalizer:
    @staticmethod
    def normalizeDataTypeName(dataType: str) -> str:
        dataType = ud.normalize('NFKC', dataType).casefold()
        return re.sub(r'[\s\-_+/·.,:;()]+', '', dataType)


class _MaterialDataValues:
    '''
    Provides per-material values and an average across materials.

    Notes:
        - Average is computed on first request and cached.
        - Raises ValueError when requesting a non-existent material.
    '''

    def __init__(self, materialDataValuePair: Iterable[tuple[str, float]]):
        self._dataValueByMaterial : Dict[str, float] = {}
        for materialName, dataValue in materialDataValuePair:
            self._dataValueByMaterial[materialName] = dataValue
        self._average = None

    def getResult(self, materialName: Optional[str] = None) -> float:
        '''
        Required behavior: when materialName is not provided (None), return the
        average value across all materials.
        '''
        if materialName is None:
            return self._getAverage()
        if materialName is not None and materialName not in self._dataValueByMaterial:
            raise ValueError(f"Material {materialName} not found")
        return self._dataValueByMaterial[materialName]
    
    def _getAverage(self) -> float:
        if self._average is None:
            if len(self._dataValueByMaterial) == 0:
                self._average = float("nan")
            else:
                self._average = sum(self._dataValueByMaterial.values()) / len(self._dataValueByMaterial)
        return self._average


class _DataTypeQuery:
    def __init__(self, materialValues: List[SolidsResultsQueryService_pb2.MaterialResults], dataTypeToIndexMap: Dict["SolidsDataType", int]):
        self._required_DataTypeQuery = _RequiredDataTypeMaterialQuery(materialValues, dataTypeToIndexMap)

    def getDataType(self, dataType: Union[str, "SolidsDataType"]) -> _MaterialDataValues:
        '''
        Resolve a data type to its material values accessor.

        Parameters:
            dataType: Union[str, SolidsDataType]
                Either a `SolidsDataType` enum member or a free-form string.
                Free-form strings are normalized (NFKC + casefold + separators removed)
                and matched using `SolidsDataAlias.alias`.

        Returns:
            _MaterialDataValues: Wrapper that provides `getResult(materialName)`.
        '''
        return self._required_DataTypeQuery.getResult(dataType)


class _RequiredDataTypeMaterialQuery:
    """
    Material data query that uses indexed dataTypeValues list instead of named fields.
    
    The values are retrieved from the dataTypeValues list using indices defined in dataTypeToIndexMap.
    """
    def __init__(self, materialValues: List[SolidsResultsQueryService_pb2.MaterialResults], dataTypeToIndexMap: Dict["SolidsDataType", int]):
        self._dataTypeToIndexMap = dataTypeToIndexMap
        self._materialValues = materialValues
        
        # Lazy initialization: _dataTypes will be populated on-demand in getResult()
        self._dataTypes: Dict[str, _MaterialDataValues] = {}
        
        # Build reverse mapping from normalized name to SolidsDataType enum for lazy initialization
        self._normalizedNameToEnum: Dict[str, "SolidsDataType"] = {}
        for dataType, index in dataTypeToIndexMap.items():
            normalizedName = _DataTypeNameNormalizer.normalizeDataTypeName(dataType.name)
            self._normalizedNameToEnum[normalizedName] = dataType

        self._alias = {}
        for dataType, aliases in SolidsDataAlias.alias.items():
            for alias in aliases:
                self._alias[_DataTypeNameNormalizer.normalizeDataTypeName(alias)] = _DataTypeNameNormalizer.normalizeDataTypeName(dataType.name)

    def getResult(self, dataType: Union[str, "SolidsDataType"]) -> _MaterialDataValues:
        # Check for SolidsDataType first since it inherits from str
        normalizedDataType = _DataTypeNameNormalizer.normalizeDataTypeName(dataType.name if isinstance(dataType, SolidsDataType) else dataType)
        
        # Determine canonical name (either direct match or via alias)
        canonical = normalizedDataType
        if normalizedDataType not in self._normalizedNameToEnum:
            # Try alias match
            canonical = self._alias.get(normalizedDataType)
            if canonical is None or canonical not in self._normalizedNameToEnum:
                available = sorted(self._normalizedNameToEnum.keys())
                raise ValueError(f"Invalid data type: {dataType}. Available: {available}")
        
        # Lazy initialization: create and cache if not already present
        if canonical not in self._dataTypes:
            enumDataType = self._normalizedNameToEnum[canonical]
            index = self._dataTypeToIndexMap[enumDataType]
            self._dataTypes[canonical] = _MaterialDataValues(
                self._getMaterialNameDataTypeValue(index, self._materialValues)
            )
        
        return self._dataTypes[canonical]

    def _getMaterialNameDataTypeValue(self, index: int, materialValues: List[SolidsResultsQueryService_pb2.MaterialResults]) -> list[tuple[str, float]]:
        """Get material name and value pairs for a given data type index from dataTypeValues list."""
        nameValueList: list[tuple[str, float]] = []
        for mv in materialValues:
            if hasattr(mv, "materialName") and hasattr(mv, "dataTypeValues"):
                if index < len(mv.dataTypeValues):
                    nameValueList.append((mv.materialName, mv.dataTypeValues[index]))
        return nameValueList


#endregion Material Results

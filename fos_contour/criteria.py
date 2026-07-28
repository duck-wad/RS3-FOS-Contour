"""Failure criterion definitions for local FoS contouring."""

from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING, Iterable

if TYPE_CHECKING:
    from rs3.results.ResultEnums import SolidsDataType


class Criterion(str, Enum):
    """Kinematic field used as the FLAC velocity analog."""

    TOTAL_DISPLACEMENT = "total_displacement"
    MAX_SHEAR_STRAIN = "max_shear_strain"

    @property
    def solids_data_type(self) -> SolidsDataType:
        from rs3.results.ResultEnums import SolidsDataType

        if self is Criterion.TOTAL_DISPLACEMENT:
            return SolidsDataType.TOTAL_DISPLACEMENT
        if self is Criterion.MAX_SHEAR_STRAIN:
            return SolidsDataType.MAX_SHEAR_STRAIN
        raise ValueError(f"Unsupported criterion: {self}")

    @property
    def column_name(self) -> str:
        return self.value


class FailureMode(str, Enum):
    """How the limiting threshold is applied across SRF trials."""

    ABSOLUTE = "absolute"
    """Fail when the absolute field value exceeds the limit."""

    INCREMENTAL = "incremental"
    """Fail when the step-to-step increase exceeds the limit."""


def parse_criterion(name: str) -> Criterion:
    key = name.strip().lower().replace("-", "_").replace(" ", "_")
    aliases = {
        "u": Criterion.TOTAL_DISPLACEMENT,
        "disp": Criterion.TOTAL_DISPLACEMENT,
        "displacement": Criterion.TOTAL_DISPLACEMENT,
        "total_displacement": Criterion.TOTAL_DISPLACEMENT,
        "totaldisplacement": Criterion.TOTAL_DISPLACEMENT,
        "gamma": Criterion.MAX_SHEAR_STRAIN,
        "shear": Criterion.MAX_SHEAR_STRAIN,
        "max_shear_strain": Criterion.MAX_SHEAR_STRAIN,
        "maxshearstrain": Criterion.MAX_SHEAR_STRAIN,
        "shear_strain": Criterion.MAX_SHEAR_STRAIN,
    }
    if key not in aliases:
        valid = ", ".join(c.value for c in Criterion)
        raise ValueError(f"Unknown criterion '{name}'. Choose from: {valid}")
    return aliases[key]


def parse_failure_mode(name: str) -> FailureMode:
    key = name.strip().lower()
    aliases = {
        "absolute": FailureMode.ABSOLUTE,
        "abs": FailureMode.ABSOLUTE,
        "incremental": FailureMode.INCREMENTAL,
        "delta": FailureMode.INCREMENTAL,
        "increment": FailureMode.INCREMENTAL,
    }
    if key not in aliases:
        valid = ", ".join(m.value for m in FailureMode)
        raise ValueError(f"Unknown failure mode '{name}'. Choose from: {valid}")
    return aliases[key]


def percentile(values: Iterable[float], p: float) -> float:
    """Simple percentile helper for limit suggestions."""
    data = sorted(float(v) for v in values)
    if not data:
        raise ValueError("Cannot compute percentile of empty data.")
    if p <= 0:
        return data[0]
    if p >= 100:
        return data[-1]
    rank = (len(data) - 1) * (p / 100.0)
    low = int(rank)
    high = min(low + 1, len(data) - 1)
    weight = rank - low
    return data[low] * (1.0 - weight) + data[high] * weight

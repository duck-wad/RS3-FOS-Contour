"""Export helpers and limit suggestions for FoS contour results."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable

from .criteria import FailureMode, percentile
from .local_fos import LocalFoSResult, collect_values_at_trial
from .rs3_extract import NodeHistory, SRFTrial


def suggest_limit(
    trials: list[SRFTrial],
    histories: dict,
    *,
    failure_mode: FailureMode = FailureMode.ABSOLUTE,
    percentile_at_critical: float = 90.0,
) -> dict[str, float]:
    """
    Suggest candidate limiting values from the kinematic field.

    Uses the last non-converged trial when available, otherwise the last trial.
    Suggestions are starting points for user tuning (same idea as FLAC).
    """
    if not trials:
        raise ValueError("No trials available for suggestions.")

    critical_index = len(trials) - 1
    for i, trial in enumerate(trials):
        if not trial.converged:
            critical_index = i
            break

    values = collect_values_at_trial(histories.values(), critical_index)
    if not values:
        raise RuntimeError("No finite nodal values found at the critical trial.")

    suggestions: dict[str, float] = {
        "critical_srf": trials[critical_index].srf,
        "min": min(values),
        "median": percentile(values, 50),
        "p75": percentile(values, 75),
        "p90": percentile(values, 90),
        "p95": percentile(values, 95),
        "max": max(values),
        "suggested": percentile(values, percentile_at_critical),
    }

    if failure_mode is FailureMode.INCREMENTAL and critical_index > 0:
        deltas: list[float] = []
        for hist in histories.values():
            a = hist.values[critical_index - 1]
            b = hist.values[critical_index]
            if a == a and b == b:
                deltas.append(b - a)
        if deltas:
            suggestions.update(
                {
                    "delta_min": min(deltas),
                    "delta_median": percentile(deltas, 50),
                    "delta_p90": percentile(deltas, 90),
                    "delta_max": max(deltas),
                    "suggested": percentile(deltas, percentile_at_critical),
                }
            )

    return suggestions


def export_csv(result: LocalFoSResult, path: str | Path) -> Path:
    """Write local FoS point cloud to CSV for ParaView / Excel / PyVista."""
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "node_id",
        "x",
        "y",
        "z",
        "local_fos",
        "failed",
        "value_at_failure",
        "final_value",
        "criterion",
        "failure_mode",
        "limit",
        "stage",
    ]

    with out.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for point in result.points:
            writer.writerow(
                {
                    "node_id": point.node_id,
                    "x": point.x,
                    "y": point.y,
                    "z": point.z,
                    "local_fos": point.local_fos,
                    "failed": int(point.failed),
                    "value_at_failure": (
                        "" if point.value_at_failure is None else point.value_at_failure
                    ),
                    "final_value": point.final_value,
                    "criterion": result.criterion.value,
                    "failure_mode": result.failure_mode.value,
                    "limit": result.limit,
                    "stage": result.stage_number,
                }
            )
    return out


def export_srf_summary(trials: Iterable[SRFTrial], path: str | Path) -> Path:
    """Write the SRF trial table (useful for checking compute coverage)."""
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=["index", "srf", "max_total_displacement", "converged"],
        )
        writer.writeheader()
        for trial in trials:
            writer.writerow(
                {
                    "index": trial.index,
                    "srf": trial.srf,
                    "max_total_displacement": trial.max_total_displacement,
                    "converged": int(trial.converged),
                }
            )
    return out

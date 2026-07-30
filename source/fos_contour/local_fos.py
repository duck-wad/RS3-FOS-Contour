"""Compute local FoS (per-node SRF) from kinematic histories."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable

from .criteria import Criterion, FailureMode
from .rs3_extract import NodeHistory, SRFTrial


@dataclass(frozen=True)
class LocalFoSPoint:
    node_id: Any
    x: float
    y: float
    z: float
    local_fos: float
    failed: bool
    value_at_failure: float | None
    final_value: float


@dataclass(frozen=True)
class LocalFoSResult:
    criterion: Criterion
    failure_mode: FailureMode
    limit: float
    stage_number: int
    trials: list[SRFTrial]
    points: list[LocalFoSPoint]

    @property
    def global_min_fos(self) -> float | None:
        failed = [p.local_fos for p in self.points if p.failed]
        return min(failed) if failed else None


def _metric_series(values: list[float], mode: FailureMode) -> list[float]:
    """Return the series compared against the limit for each trial index."""
    if mode is FailureMode.ABSOLUTE:
        return list(values)

    metrics: list[float] = []
    prev: float | None = None
    for value in values:
        if prev is None or value != value or prev != prev:  # NaN-safe
            metrics.append(0.0 if value == value else float("nan"))
        else:
            metrics.append(value - prev)
        prev = value
    return metrics


def compute_local_fos(
    trials: list[SRFTrial],
    histories: dict[Any, NodeHistory],
    *,
    limit: float,
    criterion: Criterion,
    failure_mode: FailureMode = FailureMode.ABSOLUTE,
    stage_number: int = 1,
    stable_if_never_fails: bool = True,
) -> LocalFoSResult:
    """
    Assign each node the highest SRF at which it remained below the limit.

    Parameters
    ----------
    limit
        User-defined threshold on absolute value or incremental change,
        depending on ``failure_mode``.
    stable_if_never_fails
        If True, nodes that never exceed the limit receive the maximum
        computed SRF (still considered stable through the last trial).
        If False, those nodes are marked failed=False with local_fos = max SRF.
    """
    if limit <= 0:
        raise ValueError("limit must be > 0")
    if not trials:
        raise ValueError("trials must not be empty")

    points: list[LocalFoSPoint] = []
    max_srf = max(t.srf for t in trials)

    for hist in histories.values():
        metrics = _metric_series(hist.values, failure_mode)
        local_fos = trials[0].srf
        failed = False
        value_at_failure: float | None = None

        for trial, metric, raw in zip(trials, metrics, hist.values):
            if metric != metric:  # NaN
                continue
            if metric < limit:
                local_fos = trial.srf
            else:
                failed = True
                value_at_failure = raw
                break

        if not failed:
            local_fos = max_srf if stable_if_never_fails else local_fos

        final_value = hist.values[-1] if hist.values else float("nan")
        points.append(
            LocalFoSPoint(
                node_id=hist.node_id,
                x=hist.x,
                y=hist.y,
                z=hist.z,
                local_fos=local_fos,
                failed=failed,
                value_at_failure=value_at_failure,
                final_value=final_value,
            )
        )

    return LocalFoSResult(
        criterion=criterion,
        failure_mode=failure_mode,
        limit=limit,
        stage_number=stage_number,
        trials=list(trials),
        points=points,
    )


def collect_values_at_trial(
    histories: Iterable[NodeHistory],
    trial_index: int,
) -> list[float]:
    """Gather finite nodal values at one trial index (for limit suggestions)."""
    out: list[float] = []
    for hist in histories:
        if 0 <= trial_index < len(hist.values):
            value = hist.values[trial_index]
            if value == value:
                out.append(value)
    return out

"""Extract per-node kinematic histories across SRF trials from an RS3 model."""

from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import TimeoutError as FuturesTimeout
from dataclasses import dataclass
from typing import Any, Callable

from typing import TYPE_CHECKING

from .criteria import Criterion
from .surface import NodeXYZ, select_surface_nodes

if TYPE_CHECKING:
    from rs3.Model import Model
    from rs3.results.ResultEnums import SolidsDataType


def _call_with_timeout(fn: Callable, timeout_s: float | None, label: str):
    if timeout_s is None or timeout_s <= 0:
        return fn()
    with ThreadPoolExecutor(max_workers=1) as pool:
        future = pool.submit(fn)
        try:
            return future.result(timeout=timeout_s)
        except FuturesTimeout as exc:
            raise TimeoutError(
                f"Timed out after {timeout_s:g}s while {label}."
            ) from exc


@dataclass(frozen=True)
class SRFTrial:
    """One Strength Reduction Factor trial stored with the model results."""

    index: int
    srf: float
    max_total_displacement: float
    converged: bool


@dataclass
class NodeHistory:
    """Kinematic history for one mesh node across SRF trials."""

    node_id: Any
    x: float
    y: float
    z: float
    values: list[float]  # aligned with trial list order


def list_srf_trials(model: "Model") -> list[SRFTrial]:
    """Return all SRF result indices available on the model."""
    results = model.Results
    try:
        raw = results.querySRFValues()
    except Exception as exc:  # noqa: BLE001 - surface RS3's opaque gRPC errors
        detail = str(exc)
        if "No computed results exist" in detail or "INTERNAL" in detail:
            raise RuntimeError(
                "RS3 reports no computed results for the open model.\n"
                "Open a finished SSR model in RS3 Interpret (confirm the SRF "
                "ladder is visible), then click Extract again.\n"
                "If this persists, fully quit RS3 and reopen the .rs3v3 that "
                "has a matching .rs3compute file beside it."
            ) from exc
        raise
    trials: list[SRFTrial] = []
    for index, item in enumerate(raw):
        trials.append(
            SRFTrial(
                index=index,
                srf=float(item.SRF),
                max_total_displacement=float(item.MaxTotalDisplacement),
                converged=bool(item.Converged),
            )
        )
    return trials


def _is_finite_srf(value: float) -> bool:
    return value == value and abs(value) != float("inf")


def _nodes_to_xyz(nodes: list) -> dict[Any, NodeXYZ]:
    out: dict[Any, NodeXYZ] = {}
    for node in nodes:
        nid = node.NodeID
        out[nid] = NodeXYZ(
            node_id=nid,
            x=float(node.XCoordinate),
            y=float(node.YCoordinate),
            z=float(node.ZCoordinate),
        )
    return out


def _element_node_lists(elements: list) -> list[list[Any]]:
    return [list(el.AttachedNodes) for el in elements]


def extract_nodal_histories(
    model: "Model",
    *,
    criterion: Criterion = Criterion.TOTAL_DISPLACEMENT,
    criteria: list[Criterion] | None = None,
    stage_number: int = 1,
    entity_name: str | None = None,
    region: Any | None = None,
    include_intersecting: bool = True,
    skip_unavailable: bool = True,
    include_srf_none: bool = False,
    rpc_timeout_s: float | None = 300.0,
    surface_only: bool = False,
    surface_mode: str = "map",
    shell_depth: float = 0.0,
    surface_layers: int = 1,
    max_points: int | None = None,
    include_elements: bool = False,
    progress_callback: Any | None = None,
):
    """
    Pull kinematic field(s) at nodes for every available SRF.

    Pass ``criteria=[...]`` to fetch several fields in one RS3 pass (same mesh
    round-trips). Returns ``dict[Criterion, histories]`` when ``criteria`` is
    set; otherwise returns a single histories dict for ``criterion``.
    """
    crit_list = list(criteria) if criteria else [criterion]
    if not crit_list:
        raise ValueError("At least one criterion is required.")
    multi = criteria is not None

    results = model.Results
    all_trials = list_srf_trials(model)
    if not all_trials:
        raise RuntimeError(
            "No SRF trials found on this model (querySRFValues returned empty).\n"
            "This usually means SSR results are not loaded in RS3.\n"
            "In RS3 Interpret, open the computed .rs3v3, confirm the Factor of "
            "Safety / SRF results are present, then Extract again.\n"
            "Models without a sibling .rs3compute file cannot be used."
        )

    data_types = {c.solids_data_type for c in crit_list}
    used_trials: list[SRFTrial] = []
    histories_by: dict[Criterion, dict[Any, NodeHistory]] = {c: {} for c in crit_list}
    keep_ids: set[Any] | None = None
    element_lists: list[list[Any]] | None = None

    names = ", ".join(c.value for c in crit_list)
    srf_list = [t.srf for t in all_trials if _is_finite_srf(t.srf)]
    if progress_callback and srf_list:
        progress_callback(
            f"Found {len(all_trials)} SRF trials "
            f"(SRF {min(srf_list):g} → {max(srf_list):g}). "
            f"Pulling [{names}] together per trial."
        )

    total = len(all_trials)
    for position, trial in enumerate(all_trials, start=1):
        if not include_srf_none and trial.index == 0:
            if progress_callback:
                progress_callback("Skipping SRF-None baseline (index 0)")
            continue
        if not _is_finite_srf(trial.srf):
            if progress_callback:
                progress_callback(f"Skipping non-finite SRF at index {trial.index}")
            continue

        trial_started = time.monotonic()
        if progress_callback:
            progress_callback(
                f"Trial {position}/{total}: querying SRF={trial.srf:g}…"
            )

        try:
            available = _call_with_timeout(
                lambda t=trial: results.getResultsAvailability(
                    stageNumber=stage_number,
                    srfResultIndex=t.index,
                ),
                rpc_timeout_s,
                f"getResultsAvailability for SRF index {trial.index}",
            )
        except Exception as exc:  # noqa: BLE001 - API docs disagree on 0-based rules
            if skip_unavailable and not isinstance(exc, TimeoutError):
                if progress_callback:
                    progress_callback(
                        f"Availability check failed for SRF index {trial.index}: {exc}"
                    )
                available = True  # still attempt getMeshResults
            else:
                raise

        if not available:
            if skip_unavailable:
                if progress_callback:
                    progress_callback(
                        f"Skipping unavailable SRF index {trial.index} (SRF={trial.srf})"
                    )
                continue
            raise RuntimeError(
                f"Results unavailable for stage={stage_number}, "
                f"srfResultIndex={trial.index}, SRF={trial.srf}"
            )

        if progress_callback:
            progress_callback(
                f"  Trial {position}/{total}: loading mesh results from RS3…"
            )
        solid_list = _call_with_timeout(
            lambda t=trial: results.getMeshResults(
                srfResultIndex=t.index,
                stageNumber=[stage_number],
                requiredDataTypes=data_types,
            ),
            rpc_timeout_s,
            f"getMeshResults for SRF index {trial.index} (SRF={trial.srf:g})",
        )
        if not solid_list:
            raise RuntimeError(
                f"getMeshResults returned no SolidResults for SRF index {trial.index}."
            )
        solid = solid_list[0]
        if progress_callback:
            progress_callback(
                f"  Trial {position}/{total}: streaming nodal [{names}]…"
            )
        nodes = _call_with_timeout(
            lambda: solid.getMeshNodeResults(
                entityName=entity_name,
                region=region,
                includeIntersecting=include_intersecting,
            ),
            rpc_timeout_s,
            f"getMeshNodeResults for SRF index {trial.index} (SRF={trial.srf:g})",
        )

        if include_elements and element_lists is None:
            if progress_callback:
                progress_callback("Fetching element connectivity for solid contours...")
            try:
                raw_elements = _call_with_timeout(
                    lambda: solid.getMeshElementResults(
                        entityName=entity_name,
                        region=region,
                        includeIntersecting=include_intersecting,
                    ),
                    rpc_timeout_s,
                    f"getMeshElementResults (SRF={trial.srf:g})",
                )
                element_lists = _element_node_lists(raw_elements)
                if progress_callback:
                    progress_callback(f"Elements collected: {len(element_lists)}")
            except Exception as exc:  # noqa: BLE001
                if progress_callback:
                    progress_callback(
                        f"Element query failed ({exc}); "
                        "viewer will fall back to point cloud."
                    )
                element_lists = []

        if surface_only and keep_ids is None:
            if progress_callback:
                progress_callback(
                    "Selecting free-surface / near-surface nodes..."
                )
            xyz = _nodes_to_xyz(nodes)
            try:
                elements = _call_with_timeout(
                    lambda: solid.getMeshElementResults(
                        entityName=entity_name,
                        region=region,
                        includeIntersecting=include_intersecting,
                    ),
                    rpc_timeout_s,
                    f"getMeshElementResults for surface detection "
                    f"(SRF={trial.srf:g})",
                )
                element_lists = _element_node_lists(elements)
            except Exception as exc:  # noqa: BLE001 - fall back to topo DSM
                if progress_callback:
                    progress_callback(
                        f"Element query failed ({exc}); "
                        "using topographic surface fallback."
                    )
                element_lists = None

            selection = select_surface_nodes(
                xyz,
                element_lists,
                mode=surface_mode if element_lists else "topo",
                shell_depth=shell_depth,
                surface_layers=surface_layers,
                max_points=max_points,
            )
            keep_ids = set(selection.keep_ids)
            if progress_callback:
                progress_callback(
                    f"Surface filter [{selection.mode}]: kept "
                    f"{selection.kept_count} / {selection.total_nodes} nodes "
                    f"(boundary={len(selection.boundary_ids)}, "
                    f"shell_depth={shell_depth:g}, layers={surface_layers})"
                )
            if not keep_ids:
                raise RuntimeError(
                    "Surface filter retained 0 nodes. "
                    "Try --surface-mode boundary, increase --shell-depth, "
                    "or omit --surface-only."
                )

        trial_slot = len(used_trials)
        used_trials.append(trial)
        kept_this_trial = 0

        for node in nodes:
            node_id = node.NodeID
            if keep_ids is not None and node_id not in keep_ids:
                continue
            kept_this_trial += 1
            x = float(node.XCoordinate)
            y = float(node.YCoordinate)
            z = float(node.ZCoordinate)
            for crit in crit_list:
                value = float(node.getResult(crit.solids_data_type))
                hist_map = histories_by[crit]
                hist = hist_map.get(node_id)
                if hist is None:
                    pad = [float("nan")] * trial_slot
                    hist_map[node_id] = NodeHistory(
                        node_id=node_id,
                        x=x,
                        y=y,
                        z=z,
                        values=pad + [value],
                    )
                else:
                    while len(hist.values) < trial_slot:
                        hist.values.append(float("nan"))
                    hist.values.append(value)

        if progress_callback:
            took = time.monotonic() - trial_started
            if keep_ids is None:
                progress_callback(
                    f"  Trial {position}/{total} done in {took:.1f}s — "
                    f"{len(nodes)} nodes at SRF={trial.srf:g} "
                    f"(converged={trial.converged})"
                )
            else:
                progress_callback(
                    f"  Trial {position}/{total} done in {took:.1f}s — "
                    f"{kept_this_trial} surface nodes of {len(nodes)} "
                    f"at SRF={trial.srf:g} (converged={trial.converged})"
                )

    if not used_trials:
        raise RuntimeError("No usable SRF result indices were available.")

    n = len(used_trials)
    for hist_map in histories_by.values():
        for hist in hist_map.values():
            while len(hist.values) < n:
                hist.values.append(float("nan"))

    payload = histories_by if multi else histories_by[crit_list[0]]
    if include_elements:
        return used_trials, payload, element_lists or []
    return used_trials, payload

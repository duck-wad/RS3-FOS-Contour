"""In-memory contour dataset and fast local-FoS recompute for the viewer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np

from .criteria import Criterion, FailureMode
from .rs3_extract import NodeHistory, SRFTrial

# VTK cell type ids used by PyVista / VTK.
_VTK_TETRA = 10
_VTK_HEXAHEDRON = 12
_VTK_WEDGE = 13
_VTK_PYRAMID = 14


@dataclass
class ContourDataset:
    """Cached SSR nodal histories used by the interactive FoS viewer."""

    trials: list[SRFTrial]
    node_ids: np.ndarray
    xyz: np.ndarray  # (N, 3)
    values: np.ndarray  # (N, T) kinematic field per trial
    criterion: Criterion
    failure_mode: FailureMode
    stage_number: int
    model_path: str = ""
    # Each entry is a list of RS3 node IDs for one element (corners first).
    # Shared by reference across criteria — do not mutate in place.
    elements: list[list[Any]] = field(default_factory=list)
    # Cached exterior surface (shared across criteria via prepare_surface_cache).
    # Indices in exterior_* are into the compact Plotly vertex buffer, not volume nodes.
    exterior_i: list[int] = field(default_factory=list)
    exterior_j: list[int] = field(default_factory=list)
    exterior_k: list[int] = field(default_factory=list)
    # Volume-node indices for each compact surface vertex (FoS lookup).
    surface_node_idx: np.ndarray | None = field(default=None, repr=False, compare=False)
    # Compact surface coordinates (M, 3) — what Plotly actually receives.
    surface_xyz: np.ndarray | None = field(default=None, repr=False, compare=False)
    edge_x: list[float | None] = field(default_factory=list)
    edge_y: list[float | None] = field(default_factory=list)
    edge_z: list[float | None] = field(default_factory=list)
    # Shared cross-section acceleration (corners + AABB); set by prepare_element_accel.
    element_accel: Any = field(default=None, repr=False, compare=False)
    _id_to_index: dict[Any, int] | None = field(default=None, repr=False, compare=False)

    @property
    def n_nodes(self) -> int:
        return int(self.xyz.shape[0])

    @property
    def n_surface_nodes(self) -> int:
        if self.surface_node_idx is None:
            return self.n_nodes
        return int(self.surface_node_idx.shape[0])

    @property
    def n_elements(self) -> int:
        return len(self.elements)

    @property
    def n_exterior_tris(self) -> int:
        return len(self.exterior_i)

    @property
    def srf_values(self) -> np.ndarray:
        return np.asarray([t.srf for t in self.trials], dtype=float)

    @property
    def max_srf(self) -> float:
        return float(self.srf_values.max()) if len(self.trials) else float("nan")

    def node_id_to_index(self) -> dict[Any, int]:
        if self._id_to_index is None:
            self._id_to_index = {nid: i for i, nid in enumerate(self.node_ids.tolist())}
        return self._id_to_index


def histories_to_dataset(
    trials: list[SRFTrial],
    histories: dict[Any, NodeHistory],
    *,
    criterion: Criterion,
    failure_mode: FailureMode,
    stage_number: int,
    model_path: str = "",
    elements: list[list[Any]] | None = None,
) -> ContourDataset:
    """Pack extract results into contiguous arrays for interactive updates."""
    if not trials:
        raise ValueError("No SRF trials to visualize.")
    if not histories:
        raise ValueError("No nodal histories to visualize.")

    items = list(histories.values())
    n = len(items)
    t = len(trials)
    node_ids = np.empty(n, dtype=object)
    xyz = np.empty((n, 3), dtype=float)
    values = np.empty((n, t), dtype=float)

    for i, hist in enumerate(items):
        node_ids[i] = hist.node_id
        xyz[i, 0] = hist.x
        xyz[i, 1] = hist.y
        xyz[i, 2] = hist.z
        row = list(hist.values)
        while len(row) < t:
            row.append(float("nan"))
        values[i, :] = row[:t]

    return ContourDataset(
        trials=list(trials),
        node_ids=node_ids,
        xyz=xyz,
        values=values,
        criterion=criterion,
        failure_mode=failure_mode,
        stage_number=stage_number,
        model_path=model_path,
        # Keep one shared connectivity list across criteria (no deep copy).
        elements=elements if elements is not None else [],
    )


def compute_local_fos_array(
    dataset: ContourDataset,
    limit: float,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Return ``(local_fos, failed)`` arrays for the current limit.

    Same rule as ``compute_local_fos``: highest SRF that stayed below the limit.
    """
    if limit <= 0:
        raise ValueError("limit must be > 0")

    values = dataset.values
    srfs = dataset.srf_values
    n, t = values.shape
    local_fos = np.full(n, srfs[0], dtype=float)
    failed = np.zeros(n, dtype=bool)

    if dataset.failure_mode is FailureMode.ABSOLUTE:
        metrics = values
    else:
        metrics = np.empty_like(values)
        metrics[:, 0] = 0.0
        metrics[:, 1:] = values[:, 1:] - values[:, :-1]
        nan_mask = ~np.isfinite(values)
        metrics[nan_mask] = np.nan

    for j in range(t):
        metric = metrics[:, j]
        still_ok = (~failed) & np.isfinite(metric) & (metric < limit)
        newly_failed = (~failed) & np.isfinite(metric) & (metric >= limit)
        local_fos[still_ok] = srfs[j]
        failed[newly_failed] = True

    never_failed = ~failed
    local_fos[never_failed] = dataset.max_srf
    return local_fos, failed


def _element_corners(node_ids: list[Any]) -> tuple[int, list[Any]] | None:
    """
    Map an RS3 element node list to a linear VTK cell.

    Quadratic tets (10 nodes) use the first 4 corner nodes — zone-style
    contouring like FLAC, without mid-edge nodes.
    """
    n = len(node_ids)
    if n >= 10:
        return _VTK_TETRA, node_ids[:4]
    if n == 4:
        return _VTK_TETRA, node_ids
    if n == 5:
        return _VTK_PYRAMID, node_ids
    if n == 6:
        return _VTK_WEDGE, node_ids
    if n == 8:
        return _VTK_HEXAHEDRON, node_ids
    return None


def build_fos_mesh(dataset: ContourDataset, local_fos: np.ndarray):
    """
    Build a PyVista UnstructuredGrid colored by zone (cell) Local FoS.

    Zone FoS = mean of the element's corner-node local FoS values.
    Falls back to a vertex cloud if no usable elements are available.
    """
    import pyvista as pv

    if not dataset.elements:
        cloud = pv.PolyData(dataset.xyz)
        cloud["Local FoS"] = local_fos
        return cloud, "point"

    id_to_idx = dataset.node_id_to_index()
    cells: list[int] = []
    cell_types: list[int] = []
    zone_fos: list[float] = []

    for attached in dataset.elements:
        mapped = _element_corners(list(attached))
        if mapped is None:
            continue
        vtk_type, corners = mapped
        try:
            indices = [id_to_idx[nid] for nid in corners]
        except KeyError:
            continue
        fos_vals = local_fos[indices]
        if not np.all(np.isfinite(fos_vals)):
            continue
        cells.append(len(indices))
        cells.extend(indices)
        cell_types.append(vtk_type)
        zone_fos.append(float(np.mean(fos_vals)))

    if not cell_types:
        cloud = pv.PolyData(dataset.xyz)
        cloud["Local FoS"] = local_fos
        return cloud, "point"

    grid = pv.UnstructuredGrid(
        np.asarray(cells, dtype=np.int64),
        np.asarray(cell_types, dtype=np.uint8),
        dataset.xyz,
    )
    grid.cell_data["Local FoS"] = np.asarray(zone_fos, dtype=float)
    # Also keep point data for smooth option / probing.
    grid.point_data["Local FoS"] = local_fos
    return grid, "cell"

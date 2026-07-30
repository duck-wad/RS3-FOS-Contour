"""Axis-aligned cross-section cuts through the volume mesh."""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any, Literal

import numpy as np

from .dataset import ContourDataset, _element_corners

PlaneName = Literal["XY", "XZ", "YZ"]
ViewMode = Literal["solid", "section"]

# Plane name → coordinate axis index that is held constant.
PLANE_AXIS: dict[str, int] = {
    "XY": 2,  # constant Z
    "XZ": 1,  # constant Y
    "YZ": 0,  # constant X
}
AXIS_LABEL: dict[int, str] = {0: "X", 1: "Y", 2: "Z"}

# Unique edges for each corner count (local corner indices).
_ELEMENT_EDGES: dict[int, tuple[tuple[int, int], ...]] = {
    4: (  # tet
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 2),
        (1, 3),
        (2, 3),
    ),
    5: (  # pyramid
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
        (0, 4),
        (1, 4),
        (2, 4),
        (3, 4),
    ),
    6: (  # wedge
        (0, 1),
        (1, 2),
        (2, 0),
        (3, 4),
        (4, 5),
        (5, 3),
        (0, 3),
        (1, 4),
        (2, 5),
    ),
    8: (  # hex
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 4),
        (0, 4),
        (1, 5),
        (2, 6),
        (3, 7),
    ),
}

_ON_PLANE_EPS = 1e-9


@dataclass
class SliceVertexBlend:
    """How to rebuild FoS at a slice vertex from volume nodal FoS."""

    # Volume node indices. For a node on the plane, i0 == i1 and t == 0.
    i0: int
    i1: int
    t: float  # position = (1-t)*p0 + t*p1


@dataclass
class SliceMeshCache:
    """Cached cross-section geometry independent of the current limit."""

    plane: str
    axis: int
    position: float
    xyz: np.ndarray  # (M, 3)
    i: list[int]
    j: list[int]
    k: list[int]
    blends: list[SliceVertexBlend] = field(default_factory=list)

    @property
    def n_tris(self) -> int:
        return len(self.i)

    @property
    def n_verts(self) -> int:
        return int(self.xyz.shape[0]) if self.xyz.size else 0


@dataclass
class ElementAccel:
    """Precomputed per-element corner indices and axis AABBs."""

    corners: list[np.ndarray]  # each int array of volume-node indices
    amin: np.ndarray  # (E, 3)
    amax: np.ndarray  # (E, 3)


def plane_axis(plane: str) -> int:
    key = str(plane).upper()
    if key not in PLANE_AXIS:
        raise ValueError(f"Unknown plane '{plane}'. Use XY, XZ, or YZ.")
    return PLANE_AXIS[key]


def model_bounds(dataset: ContourDataset) -> tuple[np.ndarray, np.ndarray]:
    xyz = np.asarray(dataset.xyz, dtype=float)
    if xyz.size == 0:
        return np.zeros(3), np.zeros(3)
    return xyz.min(axis=0), xyz.max(axis=0)


def section_slider_range(
    dataset: ContourDataset, plane: str
) -> tuple[float, float, float]:
    """Return (min, max, midpoint) along the plane normal."""
    mins, maxs = model_bounds(dataset)
    axis = plane_axis(plane)
    lo = float(mins[axis])
    hi = float(maxs[axis])
    if hi < lo:
        lo, hi = hi, lo
    if hi <= lo:
        hi = lo + 1.0
    mid = 0.5 * (lo + hi)
    return lo, hi, mid


def prepare_element_accel(
    datasets: dict[str, ContourDataset],
    *,
    progress_callback=None,
) -> ElementAccel | None:
    """
    Build shared element corner indices + AABBs (lazy / on demand).

    Attaches ``element_accel`` to every dataset (same mesh across criteria).
    """
    if not datasets:
        return None
    sample = next(iter(datasets.values()))
    existing = getattr(sample, "element_accel", None)
    if isinstance(existing, ElementAccel) and existing.corners:
        for ds in datasets.values():
            ds.element_accel = existing  # type: ignore[attr-defined]
        return existing

    if not sample.elements:
        empty = ElementAccel(corners=[], amin=np.zeros((0, 3)), amax=np.zeros((0, 3)))
        for ds in datasets.values():
            ds.element_accel = empty  # type: ignore[attr-defined]
        return empty

    n_el = sample.n_elements
    if progress_callback:
        progress_callback(
            "Indexing %s elements for cross-sections…" % f"{n_el:,}"
        )

    id_to_idx = sample.node_id_to_index()
    xyz = np.asarray(sample.xyz, dtype=float)
    corners_list: list[np.ndarray] = []
    amin = np.empty((n_el, 3), dtype=float)
    amax = np.empty((n_el, 3), dtype=float)
    count = 0
    t0 = time.monotonic()
    report_every = max(n_el // 5, 50_000)

    for ei, attached in enumerate(sample.elements):
        if progress_callback and ei > 0 and ei % report_every == 0:
            pct = 100.0 * ei / n_el
            progress_callback(
                "  Cross-section index: %s/%s (%.0f%%)…"
                % (f"{ei:,}", f"{n_el:,}", pct)
            )
        mapped = _element_corners(
            attached if isinstance(attached, list) else list(attached)
        )
        if mapped is None:
            continue
        _vtk, corner_ids = mapped
        try:
            idxs = np.fromiter(
                (id_to_idx[nid] for nid in corner_ids),
                dtype=np.int64,
                count=len(corner_ids),
            )
        except KeyError:
            continue
        pts = xyz[idxs]
        corners_list.append(idxs)
        amin[count] = pts.min(axis=0)
        amax[count] = pts.max(axis=0)
        count += 1

    if count == 0:
        accel = ElementAccel(
            corners=[], amin=np.zeros((0, 3)), amax=np.zeros((0, 3))
        )
    else:
        accel = ElementAccel(
            corners=corners_list,
            amin=amin[:count].copy(),
            amax=amax[:count].copy(),
        )

    for ds in datasets.values():
        ds.element_accel = accel  # type: ignore[attr-defined]

    if progress_callback:
        progress_callback(
            "Cross-section index ready (%s elements) in %.1fs."
            % (f"{count:,}", time.monotonic() - t0)
        )
    return accel


def _get_accel(dataset: ContourDataset) -> ElementAccel | None:
    accel = getattr(dataset, "element_accel", None)
    if isinstance(accel, ElementAccel):
        return accel
    # Lazy one-shot build for a single dataset.
    return prepare_element_accel({dataset.criterion.value: dataset})


def interpolate_slice_field(
    blends: list[SliceVertexBlend],
    field: np.ndarray,
) -> np.ndarray:
    """Linearly interpolate a nodal field onto slice vertices."""
    arr = np.asarray(field, dtype=float)
    if not blends:
        return np.zeros(0, dtype=float)
    i0 = np.fromiter((b.i0 for b in blends), dtype=np.int64, count=len(blends))
    i1 = np.fromiter((b.i1 for b in blends), dtype=np.int64, count=len(blends))
    t = np.fromiter((b.t for b in blends), dtype=float, count=len(blends))
    v0 = arr[i0]
    v1 = arr[i1]
    same = i0 == i1
    out = (1.0 - t) * v0 + t * v1
    out[same] = v0[same]
    return out


def interpolate_slice_failed(
    blends: list[SliceVertexBlend],
    failed: np.ndarray,
) -> np.ndarray:
    """A slice vertex 'failed' if either contributing volume node failed."""
    mask = np.asarray(failed, dtype=bool)
    if not blends:
        return np.zeros(0, dtype=bool)
    i0 = np.fromiter((b.i0 for b in blends), dtype=np.int64, count=len(blends))
    i1 = np.fromiter((b.i1 for b in blends), dtype=np.int64, count=len(blends))
    return mask[i0] | mask[i1]


def cut_mesh_with_plane(
    dataset: ContourDataset,
    *,
    plane: str,
    position: float,
) -> SliceMeshCache:
    """
    Intersect the volume mesh with an axis-aligned plane.

    Returns triangle connectivity plus vertex blends for fast FoS updates.
    """
    axis = plane_axis(plane)
    accel = _get_accel(dataset)
    empty = SliceMeshCache(
        plane=str(plane).upper(),
        axis=axis,
        position=float(position),
        xyz=np.zeros((0, 3), dtype=float),
        i=[],
        j=[],
        k=[],
        blends=[],
    )
    if accel is None or not accel.corners:
        return empty

    xyz = np.asarray(dataset.xyz, dtype=float)
    pos = float(position)
    amin = accel.amin[:, axis]
    amax = accel.amax[:, axis]
    # Elements that straddle (or touch) the plane.
    hit = np.nonzero((amin <= pos + _ON_PLANE_EPS) & (amax >= pos - _ON_PLANE_EPS))[0]
    if hit.size == 0:
        return empty

    # Dedup vertices by quantized key so shared edge cuts merge.
    vert_map: dict[tuple[Any, ...], int] = {}
    verts_xyz: list[np.ndarray] = []
    blends: list[SliceVertexBlend] = []
    tris_i: list[int] = []
    tris_j: list[int] = []
    tris_k: list[int] = []

    def _vert_key(i0: int, i1: int, t: float) -> tuple[Any, ...]:
        if i0 == i1 or abs(t) < 1e-12:
            return ("n", int(i0))
        a, b = (i0, i1) if i0 < i1 else (i1, i0)
        tt = t if i0 < i1 else 1.0 - t
        return ("e", int(a), int(b), round(float(tt), 6))

    def _add_vert(i0: int, i1: int, t: float, point: np.ndarray) -> int:
        key = _vert_key(i0, i1, t)
        existing = vert_map.get(key)
        if existing is not None:
            return existing
        idx = len(verts_xyz)
        vert_map[key] = idx
        verts_xyz.append(point.copy())
        if i0 == i1 or abs(t) < 1e-12:
            blends.append(SliceVertexBlend(i0=int(i0), i1=int(i0), t=0.0))
        elif i0 < i1:
            blends.append(SliceVertexBlend(i0=int(i0), i1=int(i1), t=float(t)))
        else:
            blends.append(SliceVertexBlend(i0=int(i1), i1=int(i0), t=float(1.0 - t)))
        return idx

    u_axis = (axis + 1) % 3
    v_axis = (axis + 2) % 3

    for ei in hit.tolist():
        corners = accel.corners[ei]
        n = int(corners.shape[0])
        edges = _ELEMENT_EDGES.get(n)
        if edges is None:
            continue
        coords = xyz[corners]
        d = coords[:, axis] - pos

        poly: list[int] = []
        seen_local: set[int] = set()

        # Nodes exactly on the plane.
        for li, di in enumerate(d):
            if abs(float(di)) <= _ON_PLANE_EPS:
                vi = _add_vert(int(corners[li]), int(corners[li]), 0.0, coords[li])
                if vi not in seen_local:
                    seen_local.add(vi)
                    poly.append(vi)

        # Edge intersections.
        for a, b in edges:
            da = float(d[a])
            db = float(d[b])
            if abs(da) <= _ON_PLANE_EPS or abs(db) <= _ON_PLANE_EPS:
                continue
            if da * db > 0:
                continue
            t = da / (da - db)
            t = float(np.clip(t, 0.0, 1.0))
            pt = (1.0 - t) * coords[a] + t * coords[b]
            # Snap plane coordinate exactly.
            pt = pt.copy()
            pt[axis] = pos
            vi = _add_vert(int(corners[a]), int(corners[b]), t, pt)
            if vi not in seen_local:
                seen_local.add(vi)
                poly.append(vi)

        if len(poly) < 3:
            continue

        # Order polygon by angle in the plane.
        pts = np.asarray([verts_xyz[i] for i in poly], dtype=float)
        center = pts.mean(axis=0)
        ang = np.arctan2(pts[:, v_axis] - center[v_axis], pts[:, u_axis] - center[u_axis])
        order = np.argsort(ang)
        ordered = [poly[int(i)] for i in order]

        # Drop near-duplicates after ordering.
        cleaned: list[int] = []
        for vi in ordered:
            if not cleaned:
                cleaned.append(vi)
                continue
            if vi == cleaned[-1]:
                continue
            if np.linalg.norm(verts_xyz[vi] - verts_xyz[cleaned[-1]]) < 1e-10:
                continue
            cleaned.append(vi)
        if len(cleaned) >= 3 and cleaned[0] == cleaned[-1]:
            cleaned.pop()
        if len(cleaned) >= 3 and np.linalg.norm(
            verts_xyz[cleaned[0]] - verts_xyz[cleaned[-1]]
        ) < 1e-10:
            cleaned.pop()
        if len(cleaned) < 3:
            continue

        # Fan triangulate.
        v0 = cleaned[0]
        for k in range(1, len(cleaned) - 1):
            tris_i.append(v0)
            tris_j.append(cleaned[k])
            tris_k.append(cleaned[k + 1])

    if not verts_xyz or not tris_i:
        return empty

    return SliceMeshCache(
        plane=str(plane).upper(),
        axis=axis,
        position=pos,
        xyz=np.vstack(verts_xyz),
        i=tris_i,
        j=tris_j,
        k=tris_k,
        blends=blends,
    )

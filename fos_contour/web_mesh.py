"""Build Plotly Mesh3d arrays from a ContourDataset + local FoS field."""

from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any

import numpy as np

from .dataset import ContourDataset, _element_corners


_TET_FACES = (
    (0, 1, 2),
    (0, 1, 3),
    (0, 2, 3),
    (1, 2, 3),
)
_HEX_FACES = (
    (0, 1, 2),
    (0, 2, 3),
    (4, 5, 6),
    (4, 6, 7),
    (0, 1, 5),
    (0, 5, 4),
    (1, 2, 6),
    (1, 6, 5),
    (2, 3, 7),
    (2, 7, 6),
    (3, 0, 4),
    (3, 4, 7),
)
_WEDGE_FACES = (
    (0, 1, 2),
    (3, 4, 5),
    (0, 1, 4),
    (0, 4, 3),
    (1, 2, 5),
    (1, 5, 4),
    (2, 0, 3),
    (2, 3, 5),
)
_PYRAMID_FACES = (
    (0, 1, 2),
    (0, 2, 3),
    (0, 1, 4),
    (1, 2, 4),
    (2, 3, 4),
    (3, 0, 4),
)


@dataclass
class PlotlyMesh:
    """Arrays ready for ``plotly.graph_objects.Mesh3d``."""

    x: Any
    y: Any
    z: Any
    i: list[int]
    j: list[int]
    k: list[int]
    intensity: list[float]
    intensitymode: str
    clim: tuple[float, float]


def _faces_for_corners(n_corners: int) -> tuple[tuple[int, int, int], ...]:
    if n_corners == 4:
        return _TET_FACES
    if n_corners == 5:
        return _PYRAMID_FACES
    if n_corners == 6:
        return _WEDGE_FACES
    if n_corners == 8:
        return _HEX_FACES
    return ()


def fos_color_limits(dataset: ContourDataset) -> tuple[float, float]:
    """
    Fixed FoS color range from the SRF trial ladder.

    Never-fail nodes are colored gray separately (not auto-scaled into blue).
    """
    srfs = dataset.srf_values
    if srfs.size == 0:
        return (1.0, 2.0)
    lo = float(np.min(srfs))
    hi = float(np.max(srfs))
    if hi <= lo:
        lo = hi - 1.0 if hi > 1.0 else 0.0
    return lo, hi


# FLAC-style FoS palette: red (critical) → dark blue (safer).
# Never-fail rock is NOT on this ladder — it stays neutral gray.
_FOS_DISCRETE_COLORS = (
    "rgb(200,0,0)",
    "rgb(230,90,0)",
    "rgb(245,190,0)",
    "rgb(170,210,40)",
    "rgb(40,180,70)",
    "rgb(0,175,200)",
    "rgb(20,100,200)",
    "rgb(0,40,160)",
)
_NEVER_FAIL_GRAY = "rgb(176,176,176)"
# Crease lines: dark enough to read as FLAC-style folds, but only creases so
# the trace stays small on large meshes.
_EDGE_LINE = dict(color="rgba(0,0,0,0.85)", width=3)


def fos_contour_levels(
    clim: tuple[float, float],
    *,
    step: float = 0.1,
) -> list[float]:
    """
    Discrete FoS contour levels for a FLAC-style stepped legend.

    Uses a regular ``step`` ladder across ``clim`` so colorbar bands are evenly
    spaced (avoiding squashed bands when SRF trials cluster).
    """
    lo, hi = float(clim[0]), float(clim[1])
    if hi <= lo:
        return [lo]

    start = float(np.floor(lo / step + 1e-12) * step)
    stop = float(np.ceil(hi / step - 1e-12) * step)
    n = int(round((stop - start) / step)) + 1
    levels = [round(start + i * step, 10) for i in range(max(n, 2))]

    if len(levels) > 12:
        keep = [0]
        mid = np.linspace(1, len(levels) - 2, 10)
        keep.extend(int(round(i)) for i in mid)
        keep.append(len(levels) - 1)
        seen: set[int] = set()
        out: list[float] = []
        for i in keep:
            if i in seen:
                continue
            seen.add(i)
            out.append(float(levels[i]))
        levels = out if len(out) >= 2 else [lo, hi]

    return [float(v) for v in levels]


def discrete_fos_colorscale(levels: list[float]) -> list[list]:
    """
    Equal-height FoS bands + a final never-fail gray slot (FLAC-style).

    Intensity must be band midpoints: FoS → 0.5 … n-0.5, never-fail → n+0.5.
    """
    n = max(len(levels), 1)
    n_palette = len(_FOS_DISCRETE_COLORS)
    if len(levels) <= 1:
        colors = [_FOS_DISCRETE_COLORS[0]]
    else:
        colors = [
            _FOS_DISCRETE_COLORS[int(round(i * (n_palette - 1) / (n - 1)))]
            for i in range(n)
        ]

    # Total slots = n FoS + 1 gray
    total = n + 1
    scale: list[list] = []
    for i, color in enumerate(colors):
        t0 = i / total
        t1 = (i + 1) / total
        scale.append([t0, color])
        scale.append([t1, color])
    g0 = n / total
    scale.append([g0, _NEVER_FAIL_GRAY])
    scale.append([1.0, _NEVER_FAIL_GRAY])
    return scale


def fos_colorbar(levels: list[float]) -> dict:
    """FoS ticks only — gray never-fail is off-legend, like FLAC."""
    n = len(levels)
    if n == 0:
        return dict(title="Local FoS", thickness=18, len=0.7)
    tickvals = [i + 0.5 for i in range(n)]
    ticktext = [f"{v:.3g}" for v in levels]
    return dict(
        title="Local FoS",
        thickness=18,
        len=0.7,
        tickmode="array",
        tickvals=tickvals,
        ticktext=ticktext,
        outlinewidth=0,
    )


def fos_to_band_index(
    fos_values: np.ndarray | list[float],
    levels: list[float],
    *,
    failed: np.ndarray | list[bool] | None = None,
) -> list[float]:
    """Map failed FoS → discrete band centers; never-fail → gray slot."""
    n = max(len(levels), 1)
    gray_mid = float(n) + 0.5
    if not levels:
        return [gray_mid for _ in fos_values]

    arr = np.asarray(
        [float(v) if np.isfinite(v) else float("nan") for v in fos_values],
        dtype=float,
    )
    if failed is None:
        # Without a mask, treat non-finite / top-of-ladder as never-fail.
        fail_mask = np.isfinite(arr)
    else:
        fail_mask = np.asarray(failed, dtype=bool)
        if fail_mask.shape != arr.shape:
            fail_mask = np.resize(fail_mask, arr.shape)

    out = np.full(arr.shape, gray_mid, dtype=float)
    if fail_mask.any() and levels:
        lvl = np.asarray(levels, dtype=float)
        sub = arr[fail_mask]
        # Non-finite failed values fall back to the lowest (most critical) band.
        sub = np.where(np.isfinite(sub), sub, lvl[0])
        idx = np.abs(sub[:, None] - lvl[None, :]).argmin(axis=1)
        out[fail_mask] = idx.astype(float) + 0.5
    return out.tolist()


def _collect_exterior_triangles(
    dataset: ContourDataset,
    *,
    progress_callback=None,
) -> list[tuple[int, int, int]]:
    """Return exterior mesh triangles as volume vertex-index triples."""
    id_to_idx = dataset.node_id_to_index()
    # Packed key = sorted(a,b,c) in 20-bit fields (supports < ~1M nodes).
    face_counts: dict[int, int] = {}
    face_tri: dict[int, tuple[int, int, int]] = {}
    n_el = len(dataset.elements)
    report_every = max(n_el // 5, 100_000) if n_el else 1

    for ei, attached in enumerate(dataset.elements):
        if progress_callback and ei > 0 and ei % report_every == 0:
            progress_callback(
                f"  Exterior faces: {ei:,}/{n_el:,} elements "
                f"({100.0 * ei / n_el:.0f}%)…"
            )
        mapped = _element_corners(attached if isinstance(attached, list) else list(attached))
        if mapped is None:
            continue
        _vtk_type, corners = mapped
        try:
            indices = [id_to_idx[nid] for nid in corners]
        except KeyError:
            continue
        for face in _faces_for_corners(len(indices)):
            a = indices[face[0]]
            b = indices[face[1]]
            c = indices[face[2]]
            # Sort for key without allocating a tuple when possible.
            x, y, z = a, b, c
            if x > y:
                x, y = y, x
            if y > z:
                y, z = z, y
            if x > y:
                x, y = y, x
            key = (x << 40) | (y << 20) | z
            face_counts[key] = face_counts.get(key, 0) + 1
            face_tri[key] = (a, b, c)

    return [face_tri[key] for key, count in face_counts.items() if count == 1]


def _compact_surface(
    dataset: ContourDataset,
    tris: list[tuple[int, int, int]],
) -> tuple[np.ndarray, np.ndarray, list[int], list[int], list[int]]:
    """
    Remap exterior triangles onto a compact vertex buffer.

    Plotly only needs surface vertices — sending all volume nodes is the
    main reason large open-pit figures take so long to load.
    """
    if not tris:
        empty = np.zeros((0,), dtype=np.int64)
        return empty, np.zeros((0, 3), dtype=float), [], [], []

    used: set[int] = set()
    for a, b, c in tris:
        used.add(a)
        used.add(b)
        used.add(c)
    volume_idx = np.fromiter(sorted(used), dtype=np.int64, count=len(used))
    remap = {int(v): i for i, v in enumerate(volume_idx.tolist())}
    i_idx = [remap[a] for a, b, c in tris]
    j_idx = [remap[b] for a, b, c in tris]
    k_idx = [remap[c] for a, b, c in tris]
    xyz = dataset.xyz[volume_idx]
    return volume_idx, xyz, i_idx, j_idx, k_idx


def build_plotly_mesh(
    dataset: ContourDataset,
    local_fos: np.ndarray,
) -> PlotlyMesh:
    """Convert solid mesh + nodal FoS into Plotly Mesh3d arrays."""
    if dataset.n_nodes == 0:
        raise ValueError("Dataset has no nodes.")

    clim = fos_color_limits(dataset)

    if dataset.surface_node_idx is not None and dataset.surface_xyz is not None:
        xyz = dataset.surface_xyz
        fos_src = np.asarray(local_fos, dtype=float)[dataset.surface_node_idx]
        i_idx = dataset.exterior_i
        j_idx = dataset.exterior_j
        k_idx = dataset.exterior_k
    else:
        xyz = dataset.xyz
        fos_src = np.asarray(local_fos, dtype=float)
        if dataset.exterior_i:
            i_idx = dataset.exterior_i
            j_idx = dataset.exterior_j
            k_idx = dataset.exterior_k
        elif dataset.elements:
            tris = _collect_exterior_triangles(dataset)
            i_idx = [t[0] for t in tris]
            j_idx = [t[1] for t in tris]
            k_idx = [t[2] for t in tris]
        else:
            i_idx, j_idx, k_idx = [], [], []

    intensity = [
        float(v) if np.isfinite(v) else float(dataset.max_srf) for v in fos_src
    ]

    return PlotlyMesh(
        # Keep numpy — Plotly accepts it and skips a huge list copy.
        x=xyz[:, 0],
        y=xyz[:, 1],
        z=xyz[:, 2],
        i=i_idx,
        j=j_idx,
        k=k_idx,
        intensity=intensity,
        intensitymode="vertex",
        clim=clim,
    )


def _edge_key(a: int, b: int) -> tuple[int, int]:
    return (a, b) if a < b else (b, a)


def _triangle_normal(
    xyz: np.ndarray, tri: tuple[int, int, int]
) -> np.ndarray | None:
    a, b, c = xyz[tri[0]], xyz[tri[1]], xyz[tri[2]]
    n = np.cross(b - a, c - a)
    length = float(np.linalg.norm(n))
    if length < 1e-18:
        return None
    return n / length


def crease_edge_segments(
    dataset: ContourDataset,
    triangles: list[tuple[int, int, int]],
    *,
    crease_deg: float = 28.0,
) -> tuple[list[float | None], list[float | None], list[float | None]]:
    """Boundary + sharp crease edges only (light depth cue, not full wireframe)."""
    if not triangles:
        return [], [], []

    xyz = dataset.xyz.astype(float, copy=False)
    cos_thresh = float(np.cos(np.deg2rad(crease_deg)))
    edge_faces: dict[tuple[int, int], list[np.ndarray]] = {}
    for tri in triangles:
        normal = _triangle_normal(xyz, tri)
        if normal is None:
            continue
        for u, v in ((tri[0], tri[1]), (tri[1], tri[2]), (tri[2], tri[0])):
            edge_faces.setdefault(_edge_key(u, v), []).append(normal)

    xs: list[float | None] = []
    ys: list[float | None] = []
    zs: list[float | None] = []
    for (ia, ib), normals in edge_faces.items():
        keep = len(normals) == 1
        if not keep and len(normals) >= 2:
            for i in range(len(normals)):
                for j in range(i + 1, len(normals)):
                    if float(np.dot(normals[i], normals[j])) < cos_thresh:
                        keep = True
                        break
                if keep:
                    break
        if not keep:
            continue
        a = xyz[ia]
        b = xyz[ib]
        xs.extend([float(a[0]), float(b[0]), None])
        ys.extend([float(a[1]), float(b[1]), None])
        zs.extend([float(a[2]), float(b[2]), None])
    return xs, ys, zs


def prepare_surface_cache(
    datasets: dict[str, ContourDataset],
    *,
    progress_callback=None,
) -> None:
    """
    Build the solid exterior mesh + crease edges once; attach to every dataset.

    Only surface vertices are sent to Plotly (volume nodes stay in memory for
    FoS math), which keeps the solid contour affordable on large models.
    """
    if not datasets:
        return
    sample = next(iter(datasets.values()))
    if sample.surface_xyz is not None:
        return

    n_el = sample.n_elements
    if n_el == 0:
        if progress_callback:
            progress_callback("No element connectivity — point display only.")
        return

    if progress_callback:
        progress_callback(
            f"Building exterior surface from {n_el:,} elements…"
        )
    t0 = time.monotonic()
    tris = _collect_exterior_triangles(sample, progress_callback=progress_callback)
    volume_idx, surf_xyz, i_idx, j_idx, k_idx = _compact_surface(sample, tris)
    if progress_callback:
        progress_callback(
            f"Exterior: {len(tris):,} tris, {len(volume_idx):,} surface verts "
            f"in {time.monotonic() - t0:.1f}s."
        )

    t1 = time.monotonic()
    compact = ContourDataset(
        trials=sample.trials,
        node_ids=sample.node_ids[volume_idx],
        xyz=surf_xyz,
        values=sample.values[volume_idx],
        criterion=sample.criterion,
        failure_mode=sample.failure_mode,
        stage_number=sample.stage_number,
        model_path=sample.model_path,
    )
    ex, ey, ez = crease_edge_segments(compact, list(zip(i_idx, j_idx, k_idx)))
    if progress_callback:
        n_seg = sum(1 for v in ex if v is None)
        progress_callback(
            f"Crease edges: {n_seg:,} segments in {time.monotonic() - t1:.1f}s."
        )

    for ds in datasets.values():
        ds.surface_node_idx = volume_idx
        ds.surface_xyz = surf_xyz
        ds.exterior_i = i_idx
        ds.exterior_j = j_idx
        ds.exterior_k = k_idx
        ds.edge_x = ex
        ds.edge_y = ey
        ds.edge_z = ez


_FLAT_LIGHTING = dict(
    ambient=1.0, diffuse=0.0, specular=0.0, roughness=1.0, fresnel=0.0
)


def _scene_axis_ranges(dataset: ContourDataset) -> dict:
    """Fixed scene bounds so Plotly does not auto-fit on every update."""
    xyz = dataset.xyz
    if xyz.size == 0:
        return {}
    mins = xyz.min(axis=0)
    maxs = xyz.max(axis=0)
    span = np.maximum(maxs - mins, 1e-9)
    pad = 0.08 * float(span.max())
    return {
        "xaxis": dict(
            title="X",
            range=[float(mins[0] - pad), float(maxs[0] + pad)],
            autorange=False,
        ),
        "yaxis": dict(
            title="Y",
            range=[float(mins[1] - pad), float(maxs[1] + pad)],
            autorange=False,
        ),
        "zaxis": dict(
            title="Z",
            range=[float(mins[2] - pad), float(maxs[2] + pad)],
            autorange=False,
        ),
    }


def make_fos_figure(
    dataset: ContourDataset,
    local_fos: np.ndarray,
    *,
    failed: np.ndarray | None = None,
    title: str | None = None,
    camera: dict | None = None,
):
    """Build a Plotly Figure for the FoS contour mesh."""
    import plotly.graph_objects as go

    mesh = build_plotly_mesh(dataset, local_fos)
    fig = go.Figure()

    levels = fos_contour_levels(mesh.clim)
    colorscale = discrete_fos_colorscale(levels)
    colorbar = fos_colorbar(levels)
    raw_fos = mesh.intensity
    failed_surf = failed
    if failed is not None and dataset.surface_node_idx is not None:
        failed_surf = np.asarray(failed, dtype=bool)[dataset.surface_node_idx]
    band = fos_to_band_index(raw_fos, levels, failed=failed_surf)
    n_levels = max(len(levels), 1)
    cmax = float(n_levels + 1)  # FoS bands + never-fail gray

    if mesh.i:
        # Always ambient-only so FoS bands stay flat (no per-face mottling).
        fig.add_trace(
            go.Mesh3d(
                x=mesh.x,
                y=mesh.y,
                z=mesh.z,
                i=mesh.i,
                j=mesh.j,
                k=mesh.k,
                intensity=band,
                customdata=raw_fos,
                intensitymode="vertex",
                colorscale=colorscale,
                cmin=0.0,
                cmax=cmax,
                flatshading=False,
                showscale=True,
                colorbar=colorbar,
                lighting=dict(_FLAT_LIGHTING),
                lightposition=dict(x=0, y=0, z=100),
                name="Local FoS",
                hovertemplate="FoS=%{customdata:.3g}<extra></extra>",
            )
        )
        if dataset.edge_x:
            fig.add_trace(
                go.Scatter3d(
                    x=dataset.edge_x,
                    y=dataset.edge_y,
                    z=dataset.edge_z,
                    mode="lines",
                    line=dict(_EDGE_LINE),
                    hoverinfo="skip",
                    showlegend=False,
                    name="Edges",
                )
            )
    else:
        fig.add_trace(
            go.Scatter3d(
                x=mesh.x,
                y=mesh.y,
                z=mesh.z,
                mode="markers",
                marker=dict(
                    size=2.5,
                    color=band,
                    colorscale=colorscale,
                    cmin=0.0,
                    cmax=cmax,
                    colorbar=colorbar,
                    opacity=0.95,
                ),
                customdata=raw_fos,
                name="Local FoS (nodes)",
                hovertemplate="FoS=%{customdata:.3g}<extra></extra>",
            )
        )

    scene = dict(
        aspectmode="data",
        bgcolor="white",
        uirevision="fos-contour",
        **_scene_axis_ranges(dataset),
    )
    if camera:
        scene["camera"] = camera

    fig.update_layout(
        title=title or "Local FoS Contours",
        margin=dict(l=0, r=0, t=40, b=0),
        paper_bgcolor="white",
        uirevision="fos-contour",
        scene=scene,
    )
    return fig


def intensities_for_limit(
    dataset: ContourDataset,
    local_fos: np.ndarray,
    *,
    failed: np.ndarray | None = None,
) -> tuple[list[float], tuple[float, float], list[float]]:
    """Band-index intensities + clim + raw FoS (for Dash Patch / hover)."""
    clim = fos_color_limits(dataset)
    levels = fos_contour_levels(clim)
    fos_src = np.asarray(local_fos, dtype=float)
    failed_src = failed
    if dataset.surface_node_idx is not None:
        fos_src = fos_src[dataset.surface_node_idx]
        if failed is not None:
            failed_src = np.asarray(failed, dtype=bool)[dataset.surface_node_idx]
    raw = [
        float(v) if np.isfinite(v) else float(dataset.max_srf) for v in fos_src
    ]
    band = fos_to_band_index(raw, levels, failed=failed_src)
    n_levels = max(len(levels), 1)
    return band, (0.0, float(n_levels + 1)), raw

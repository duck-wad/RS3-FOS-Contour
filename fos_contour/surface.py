"""Identify free-surface / near-surface mesh nodes for FoS mapping."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping, Sequence

# Face definitions: each face is a tuple of local node indices.
# For quadratic elements, include mid-edge nodes so they are marked as boundary.
_ELEMENT_FACES: dict[int, tuple[tuple[int, ...], ...]] = {
    4: (  # linear tetrahedron
        (0, 1, 2),
        (0, 1, 3),
        (0, 2, 3),
        (1, 2, 3),
    ),
    10: (  # quadratic tetrahedron (corners 0-3, mids 4-9)
        # face corners + mid-edge nodes
        (0, 1, 2, 4, 5, 6),
        (0, 1, 3, 4, 8, 7),
        (0, 2, 3, 6, 9, 7),
        (1, 2, 3, 5, 9, 8),
    ),
    5: (  # pyramid
        (0, 1, 2, 3),
        (0, 1, 4),
        (1, 2, 4),
        (2, 3, 4),
        (3, 0, 4),
    ),
    6: (  # wedge / pentahedron
        (0, 1, 2),
        (3, 4, 5),
        (0, 1, 4, 3),
        (1, 2, 5, 4),
        (2, 0, 3, 5),
    ),
    8: (  # hexahedron
        (0, 1, 2, 3),
        (4, 5, 6, 7),
        (0, 1, 5, 4),
        (1, 2, 6, 5),
        (2, 3, 7, 6),
        (3, 0, 4, 7),
    ),
}


def _face_match_key(node_ids: Sequence[object], local_face: tuple[int, ...]) -> tuple:
    """
    Canonical key for face matching.

    For triangular faces (3 or 6 nodes), key off the three corner nodes only so
    linear/quadratic faces still match across shared elements.
    """
    if len(local_face) in (3, 6):
        corners = tuple(node_ids[i] for i in local_face[:3])
        return ("tri",) + tuple(sorted(corners))
    return ("poly",) + tuple(sorted(node_ids[i] for i in local_face))


def boundary_node_ids(elements: Iterable[Sequence[object]]) -> set:
    """
    Nodes that lie on a mesh face belonging to exactly one element.

    These are the geometric free-surface / domain-boundary nodes.
    """
    face_counts: dict[tuple, int] = {}
    face_nodes: dict[tuple, tuple] = {}

    for attached in elements:
        nodes = list(attached)
        faces = _ELEMENT_FACES.get(len(nodes))
        if faces is None:
            continue
        for face in faces:
            key = _face_match_key(nodes, face)
            ids = tuple(nodes[i] for i in face)
            face_counts[key] = face_counts.get(key, 0) + 1
            face_nodes[key] = ids

    boundary: set = set()
    for key, count in face_counts.items():
        if count == 1:
            boundary.update(face_nodes[key])
    return boundary


@dataclass(frozen=True)
class NodeXYZ:
    node_id: object
    x: float
    y: float
    z: float


@dataclass(frozen=True)
class SurfaceSelection:
    """Result of surface / near-surface filtering."""

    keep_ids: frozenset
    boundary_ids: frozenset
    total_nodes: int
    mode: str
    shell_depth: float
    surface_layers: int

    @property
    def kept_count(self) -> int:
        return len(self.keep_ids)


def _aabb(nodes: Mapping[object, NodeXYZ]) -> tuple[float, float, float, float, float, float]:
    xs = [n.x for n in nodes.values()]
    ys = [n.y for n in nodes.values()]
    zs = [n.z for n in nodes.values()]
    return min(xs), max(xs), min(ys), max(ys), min(zs), max(zs)


def map_surface_node_ids(
    boundary_ids: set,
    nodes: Mapping[object, NodeXYZ],
    *,
    box_tol_fraction: float = 1e-3,
    exclude_bottom: bool = True,
    exclude_vertical_sides: bool = True,
) -> set:
    """
    Keep free-surface nodes that form the 'map' (topography / pit face).

    Drops mesh-boundary nodes on the exterior analysis-box bottom, and
    vertical box sides below the top face (supports / far-field walls).
    Top-rim nodes that also lie on a side face are kept.
    """
    if not boundary_ids:
        return set()

    subset = {nid: nodes[nid] for nid in boundary_ids if nid in nodes}
    if not subset:
        return set()

    # Prefer full-model AABB for stable side/bottom detection.
    xmin, xmax, ymin, ymax, zmin, zmax = _aabb(nodes if nodes else subset)

    diag = (
        (xmax - xmin) ** 2 + (ymax - ymin) ** 2 + (zmax - zmin) ** 2
    ) ** 0.5
    tol = max(diag * box_tol_fraction, 1e-9)

    kept: set = set()
    for nid, node in subset.items():
        on_bottom = exclude_bottom and abs(node.z - zmin) <= tol
        on_vertical_side = (
            abs(node.x - xmin) <= tol
            or abs(node.x - xmax) <= tol
            or abs(node.y - ymin) <= tol
            or abs(node.y - ymax) <= tol
        )
        # Keep the crest / top face even when it touches a vertical box side.
        on_lower_side = (
            exclude_vertical_sides
            and on_vertical_side
            and node.z < (zmax - tol)
        )
        if on_bottom or on_lower_side:
            continue
        kept.add(nid)
    return kept


def topographic_surface_node_ids(
    nodes: Mapping[object, NodeXYZ],
    *,
    bin_size: float | None = None,
    shell_depth: float = 0.0,
) -> set:
    """
    Fallback when element topology is unavailable.

    Build a coarse DSM from max-Z per XY bin and keep nodes within
    ``shell_depth`` below that local surface (0 => only the bin-top nodes).
    """
    if not nodes:
        return set()

    xmin, xmax, ymin, ymax, zmin, zmax = _aabb(nodes)
    span = max(xmax - xmin, ymax - ymin, 1e-9)
    if bin_size is None or bin_size <= 0:
        # ~100 bins along the longer horizontal axis.
        bin_size = span / 100.0

    tops: dict[tuple[int, int], float] = {}
    for node in nodes.values():
        ix = int((node.x - xmin) / bin_size)
        iy = int((node.y - ymin) / bin_size)
        key = (ix, iy)
        prev = tops.get(key)
        if prev is None or node.z > prev:
            tops[key] = node.z

    depth = max(0.0, shell_depth)
    kept: set = set()
    for nid, node in nodes.items():
        ix = int((node.x - xmin) / bin_size)
        iy = int((node.y - ymin) / bin_size)
        top = tops.get((ix, iy))
        if top is None:
            continue
        if (top - node.z) <= depth + 1e-12:
            kept.add(nid)
    return kept


def expand_by_element_layers(
    seed_ids: set,
    elements: Iterable[Sequence[object]],
    *,
    layers: int,
) -> set:
    """Grow a node set by N rings of element adjacency."""
    if layers <= 0:
        return set(seed_ids)

    node_to_elems: dict[object, list[tuple]] = {}
    elem_list: list[tuple] = []
    for attached in elements:
        nodes = tuple(attached)
        elem_list.append(nodes)
        for nid in nodes:
            node_to_elems.setdefault(nid, []).append(nodes)

    kept = set(seed_ids)
    frontier = set(seed_ids)
    for _ in range(layers):
        nxt: set = set()
        for nid in frontier:
            for elem in node_to_elems.get(nid, []):
                for other in elem:
                    if other not in kept:
                        nxt.add(other)
        kept.update(nxt)
        frontier = nxt
        if not frontier:
            break
    return kept


def expand_by_depth(
    seed_ids: set,
    nodes: Mapping[object, NodeXYZ],
    *,
    shell_depth: float,
) -> set:
    """Include any node within ``shell_depth`` of a seed node (Euclidean)."""
    if shell_depth <= 0 or not seed_ids:
        return set(seed_ids)

    seeds = [nodes[nid] for nid in seed_ids if nid in nodes]
    if not seeds:
        return set(seed_ids)

    cell = shell_depth
    grid: dict[tuple[int, int, int], list[NodeXYZ]] = {}
    for seed in seeds:
        key = (
            int(seed.x / cell),
            int(seed.y / cell),
            int(seed.z / cell),
        )
        grid.setdefault(key, []).append(seed)

    depth2 = shell_depth * shell_depth
    kept = set(seed_ids)
    for nid, node in nodes.items():
        if nid in kept:
            continue
        ix = int(node.x / cell)
        iy = int(node.y / cell)
        iz = int(node.z / cell)
        hit = False
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for dz in (-1, 0, 1):
                    for seed in grid.get((ix + dx, iy + dy, iz + dz), []):
                        ddx = node.x - seed.x
                        ddy = node.y - seed.y
                        ddz = node.z - seed.z
                        if ddx * ddx + ddy * ddy + ddz * ddz <= depth2:
                            kept.add(nid)
                            hit = True
                            break
                    if hit:
                        break
                if hit:
                    break
            if hit:
                break
    return kept


def decimate_ids(
    ids: Iterable[object],
    nodes: Mapping[object, NodeXYZ],
    *,
    max_points: int,
) -> set:
    """
    Spatially bin and keep up to ``max_points`` nodes (stable, deterministic).

    Prefer higher-Z nodes in each bin so the visible map surface is preserved.
    """
    id_list = [nid for nid in ids if nid in nodes]
    if max_points <= 0 or len(id_list) <= max_points:
        return set(id_list)

    xmin, xmax, ymin, ymax, _, _ = _aabb({nid: nodes[nid] for nid in id_list})
    span = max(xmax - xmin, ymax - ymin, 1e-9)
    # Aim for ~max_points bins; one keeper per bin.
    bins_1d = max(int(max_points**0.5), 1)
    bin_size = span / bins_1d

    best: dict[tuple[int, int], object] = {}
    best_z: dict[tuple[int, int], float] = {}
    for nid in id_list:
        node = nodes[nid]
        key = (
            int((node.x - xmin) / bin_size),
            int((node.y - ymin) / bin_size),
        )
        prev_z = best_z.get(key)
        if prev_z is None or node.z > prev_z:
            best[key] = nid
            best_z[key] = node.z

    kept = list(best.values())
    if len(kept) > max_points:
        # Deterministic trim: sort by id string/number.
        kept = sorted(kept, key=lambda x: str(x))[:max_points]
    return set(kept)


def select_surface_nodes(
    nodes: Mapping[object, NodeXYZ],
    elements: Sequence[Sequence[object]] | None,
    *,
    mode: str = "map",
    shell_depth: float = 0.0,
    surface_layers: int = 0,
    max_points: int | None = None,
    box_tol_fraction: float = 1e-3,
) -> SurfaceSelection:
    """
    Choose nodes for FoS contouring.

    mode
        ``map``: free-surface nodes excluding analysis-box bottom/sides.
        ``boundary``: all mesh-boundary nodes.
        ``topo``: DSM-style near-surface (no element connectivity required).
    """
    mode_key = mode.strip().lower()
    total = len(nodes)

    if mode_key == "topo" or not elements:
        boundary = topographic_surface_node_ids(nodes, shell_depth=0.0)
        seed = topographic_surface_node_ids(nodes, shell_depth=shell_depth)
        used_mode = "topo" if mode_key == "topo" or not elements else mode_key
        if not elements and mode_key != "topo":
            used_mode = "topo"
    else:
        boundary = boundary_node_ids(elements)
        if not boundary:
            # Unrecognized element topologies (e.g. higher-order) yield no faces.
            boundary = topographic_surface_node_ids(nodes, shell_depth=0.0)
            seed = topographic_surface_node_ids(nodes, shell_depth=shell_depth)
            used_mode = "topo"
        elif mode_key == "boundary":
            seed = set(boundary)
            used_mode = mode_key
        elif mode_key == "map":
            seed = map_surface_node_ids(
                boundary,
                nodes,
                box_tol_fraction=box_tol_fraction,
            )
            # If filtering removed everything, fall back to full boundary.
            if not seed:
                seed = set(boundary)
            used_mode = mode_key
        else:
            raise ValueError(
                f"Unknown surface mode '{mode}'. Use map | boundary | topo."
            )
        if used_mode != "topo":
            if surface_layers > 0:
                seed = expand_by_element_layers(
                    seed, elements, layers=surface_layers
                )
            if shell_depth > 0:
                seed = expand_by_depth(seed, nodes, shell_depth=shell_depth)

    if max_points is not None:
        seed = decimate_ids(seed, nodes, max_points=max_points)

    return SurfaceSelection(
        keep_ids=frozenset(seed),
        boundary_ids=frozenset(boundary),
        total_nodes=total,
        mode=used_mode,
        shell_depth=shell_depth,
        surface_layers=surface_layers,
    )

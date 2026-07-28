"""Tests for axis-aligned FoS cross-section cuts."""

from __future__ import annotations

import numpy as np

from fos_contour.criteria import Criterion, FailureMode
from fos_contour.dataset import ContourDataset
from fos_contour.rs3_extract import SRFTrial
from fos_contour.slice_plane import (
    cut_mesh_with_plane,
    interpolate_slice_field,
    prepare_element_accel,
    section_slider_range,
)


def _two_tet_dataset() -> ContourDataset:
    trials = [
        SRFTrial(
            index=1, srf=1.2, max_total_displacement=1.0, converged=True
        )
    ]
    xyz = np.array(
        [
            [0.0, 0.0, 0.0],
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
            [0.0, 0.0, -1.0],
        ],
        dtype=float,
    )
    node_ids = np.array([10, 11, 12, 13, 14], dtype=object)
    values = np.ones((5, 1), dtype=float)
    elements = [[10, 11, 12, 13], [10, 11, 12, 14]]
    return ContourDataset(
        trials=trials,
        node_ids=node_ids,
        xyz=xyz,
        values=values,
        criterion=Criterion.TOTAL_DISPLACEMENT,
        failure_mode=FailureMode.ABSOLUTE,
        stage_number=1,
        model_path="test",
        elements=elements,
    )


def test_xy_cut_through_shared_face():
    ds = _two_tet_dataset()
    prepare_element_accel({"total_displacement": ds})
    cut = cut_mesh_with_plane(ds, plane="XY", position=0.0)
    assert cut.n_verts >= 3
    assert cut.n_tris >= 1
    assert np.allclose(cut.xyz[:, 2], 0.0, atol=1e-8)


def test_yz_cut_and_interpolate():
    ds = _two_tet_dataset()
    prepare_element_accel({"total_displacement": ds})
    cut = cut_mesh_with_plane(ds, plane="YZ", position=0.25)
    assert cut.n_tris >= 1
    fos = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    interp = interpolate_slice_field(cut.blends, fos)
    assert interp.shape == (cut.n_verts,)
    assert np.all(np.isfinite(interp))


def test_section_slider_range():
    ds = _two_tet_dataset()
    lo, hi, mid = section_slider_range(ds, "XZ")
    assert lo <= mid <= hi
    assert hi > lo

"""Unit tests for array-based local FoS used by the viewer."""

from __future__ import annotations

import unittest

import numpy as np

from fos_contour.criteria import Criterion, FailureMode
from fos_contour.dataset import (
    ContourDataset,
    build_fos_mesh,
    compute_local_fos_array,
)
from fos_contour.rs3_extract import SRFTrial
from fos_contour.web_mesh import build_plotly_mesh


class TestDatasetFoS(unittest.TestCase):
    def test_absolute_matches_expected(self) -> None:
        trials = [
            SRFTrial(0, 1.0, 0.0, True),
            SRFTrial(1, 1.1, 0.0, True),
            SRFTrial(2, 1.2, 0.0, True),
        ]
        values = np.array(
            [
                [0.01, 0.02, 0.20],  # fails at 1.2 → FoS 1.1
                [0.01, 0.01, 0.01],  # never fails → max 1.2
            ],
            dtype=float,
        )
        dataset = ContourDataset(
            trials=trials,
            node_ids=np.array([1, 2], dtype=object),
            xyz=np.zeros((2, 3)),
            values=values,
            criterion=Criterion.TOTAL_DISPLACEMENT,
            failure_mode=FailureMode.ABSOLUTE,
            stage_number=1,
        )
        fos, failed = compute_local_fos_array(dataset, limit=0.04)
        self.assertTrue(failed[0])
        self.assertAlmostEqual(fos[0], 1.1)
        self.assertFalse(failed[1])
        self.assertAlmostEqual(fos[1], 1.2)

    def test_build_mesh_from_tets(self) -> None:
        trials = [SRFTrial(0, 1.0, 0.0, True), SRFTrial(1, 1.5, 0.0, True)]
        xyz = np.array(
            [
                [0.0, 0.0, 0.0],
                [1.0, 0.0, 0.0],
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 1.0],
            ]
        )
        values = np.ones((4, 2)) * 0.01
        values[0, 1] = 1.0
        dataset = ContourDataset(
            trials=trials,
            node_ids=np.array([10, 11, 12, 13], dtype=object),
            xyz=xyz,
            values=values,
            criterion=Criterion.TOTAL_DISPLACEMENT,
            failure_mode=FailureMode.ABSOLUTE,
            stage_number=1,
            elements=[[10, 11, 12, 13]],
        )
        fos, _ = compute_local_fos_array(dataset, limit=0.5)
        mesh, kind = build_fos_mesh(dataset, fos)
        self.assertEqual(kind, "cell")
        self.assertEqual(mesh.n_cells, 1)
        self.assertIn("Local FoS", mesh.cell_data)

    def test_build_plotly_mesh(self) -> None:
        trials = [SRFTrial(0, 1.0, 0.0, True), SRFTrial(1, 1.5, 0.0, True)]
        xyz = np.array(
            [
                [0.0, 0.0, 0.0],
                [1.0, 0.0, 0.0],
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 1.0],
            ]
        )
        values = np.ones((4, 2)) * 0.01
        dataset = ContourDataset(
            trials=trials,
            node_ids=np.array([10, 11, 12, 13], dtype=object),
            xyz=xyz,
            values=values,
            criterion=Criterion.TOTAL_DISPLACEMENT,
            failure_mode=FailureMode.ABSOLUTE,
            stage_number=1,
            elements=[[10, 11, 12, 13]],
        )
        fos, _ = compute_local_fos_array(dataset, limit=0.5)
        mesh = build_plotly_mesh(dataset, fos)
        # Shared vertices + exterior faces (single tet → 4 triangles, 4 nodes).
        self.assertEqual(len(mesh.x), 4)
        self.assertEqual(len(mesh.intensity), 4)
        self.assertEqual(len(mesh.i), 4)
        self.assertEqual(mesh.intensitymode, "vertex")
        self.assertEqual(mesh.clim, (1.0, 1.5))
        self.assertTrue(all(np.isfinite(mesh.intensity)))


if __name__ == "__main__":
    unittest.main()

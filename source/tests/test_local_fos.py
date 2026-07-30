"""
Lightweight unit tests for local FoS logic (no RS3 connection required).

Run: python -m unittest tests.test_local_fos
"""

from __future__ import annotations

import unittest

from fos_contour.criteria import Criterion, FailureMode
from fos_contour.local_fos import compute_local_fos
from fos_contour.rs3_extract import NodeHistory, SRFTrial


def _trials(*srfs: float) -> list[SRFTrial]:
    return [
        SRFTrial(index=i, srf=s, max_total_displacement=0.0, converged=True)
        for i, s in enumerate(srfs)
    ]


class TestLocalFoS(unittest.TestCase):
    def test_absolute_threshold(self) -> None:
        trials = _trials(1.0, 1.1, 1.2, 1.3)
        histories = {
            1: NodeHistory(1, 0, 0, 0, [0.01, 0.02, 0.05, 0.20]),
            2: NodeHistory(2, 1, 0, 0, [0.01, 0.01, 0.01, 0.01]),
        }
        result = compute_local_fos(
            trials,
            histories,
            limit=0.04,
            criterion=Criterion.TOTAL_DISPLACEMENT,
            failure_mode=FailureMode.ABSOLUTE,
        )
        by_id = {p.node_id: p for p in result.points}
        self.assertTrue(by_id[1].failed)
        self.assertAlmostEqual(by_id[1].local_fos, 1.1)
        self.assertFalse(by_id[2].failed)
        self.assertAlmostEqual(by_id[2].local_fos, 1.3)

    def test_incremental_threshold(self) -> None:
        trials = _trials(1.0, 1.1, 1.2)
        histories = {
            1: NodeHistory(1, 0, 0, 0, [0.10, 0.11, 0.50]),  # big jump at 1.2
        }
        result = compute_local_fos(
            trials,
            histories,
            limit=0.05,
            criterion=Criterion.TOTAL_DISPLACEMENT,
            failure_mode=FailureMode.INCREMENTAL,
        )
        point = result.points[0]
        self.assertTrue(point.failed)
        self.assertAlmostEqual(point.local_fos, 1.1)


if __name__ == "__main__":
    unittest.main()

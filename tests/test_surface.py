"""Unit tests for surface / near-surface node selection."""

from __future__ import annotations

import unittest

from fos_contour.surface import (
    NodeXYZ,
    boundary_node_ids,
    map_surface_node_ids,
    select_surface_nodes,
    topographic_surface_node_ids,
)


def _tet_box() -> tuple[dict, list[list[int]]]:
    """
    Two tets filling a unit cube-ish volume with a clear top face.

    Nodes:
      0 (0,0,0) 1 (1,0,0) 2 (0,1,0) 3 (0,0,1) 4 (1,1,1)
    """
    nodes = {
        0: NodeXYZ(0, 0, 0, 0),
        1: NodeXYZ(1, 1, 0, 0),
        2: NodeXYZ(2, 0, 1, 0),
        3: NodeXYZ(3, 0, 0, 1),
        4: NodeXYZ(4, 1, 1, 1),
    }
    # Not a perfect partition; enough shared/unshared faces for boundary test.
    elements = [
        [0, 1, 2, 3],
        [1, 2, 3, 4],
    ]
    return nodes, elements


class TestSurfaceSelection(unittest.TestCase):
    def test_boundary_faces(self) -> None:
        _, elements = _tet_box()
        boundary = boundary_node_ids(elements)
        self.assertTrue(boundary)
        self.assertIn(0, boundary)
        self.assertIn(4, boundary)

    def test_map_excludes_bottom(self) -> None:
        nodes, elements = _tet_box()
        boundary = boundary_node_ids(elements)
        mapped = map_surface_node_ids(boundary, nodes)
        # Bottom corner (0,0,0) should be excluded as box bottom/side.
        self.assertNotIn(0, mapped)
        # Top-ish node should remain.
        self.assertIn(4, mapped)

    def test_topo_shell(self) -> None:
        nodes = {
            1: NodeXYZ(1, 0, 0, 10),
            2: NodeXYZ(2, 0, 0, 9),
            3: NodeXYZ(3, 0, 0, 0),
        }
        shallow = topographic_surface_node_ids(nodes, shell_depth=0.0)
        self.assertEqual(shallow, {1})
        deep = topographic_surface_node_ids(nodes, shell_depth=1.5)
        self.assertEqual(deep, {1, 2})

    def test_select_map_with_layers(self) -> None:
        nodes, elements = _tet_box()
        selection = select_surface_nodes(
            nodes,
            elements,
            mode="map",
            shell_depth=0.0,
            surface_layers=0,
        )
        self.assertGreater(selection.kept_count, 0)
        self.assertLessEqual(selection.kept_count, selection.total_nodes)

    def test_quadratic_tet_boundary(self) -> None:
        # Two quadratic tets sharing face 0-1-2
        # corners 0,1,2,3 and 0,1,2,4 ; mids follow standard tet10 layout
        elements = [
            [0, 1, 2, 3, 10, 11, 12, 13, 14, 15],
            [0, 1, 2, 4, 10, 11, 12, 16, 17, 18],
        ]
        boundary = boundary_node_ids(elements)
        # Shared face corners should not be exclusive to boundary-only logic
        # but nodes only on outer faces should appear.
        self.assertIn(3, boundary)
        self.assertIn(4, boundary)
        self.assertTrue(boundary)
        nodes = {
            i: NodeXYZ(i, float(i), 0.0, float(i % 3))
            for i in range(50)
        }
        selection = select_surface_nodes(
            nodes,
            None,
            mode="topo",
            shell_depth=10.0,
            max_points=10,
        )
        self.assertLessEqual(selection.kept_count, 10)


if __name__ == "__main__":
    unittest.main()

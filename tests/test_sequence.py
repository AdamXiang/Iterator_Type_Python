import math
import pytest
from custom_sequence.polygon import Polygon

REL_TOL = 1e-3
ABS_TOL = 1e-3


@pytest.mark.parametrize(
    "vertices, circumradius, expected",
    [
        # vertices, circumradius, (interior_angle, area, side_length, perimeter, apothem)
        (3, 1, (60, None, None, None, None)),                  # Triangle
        (4, 1, (90, 2.0, math.sqrt(2), 4 * math.sqrt(2), 0.707)),  # Square
        (6, 2, (120, 10.3923, 2, 12, 1.73205)),                 # Hexagon
    ],
)
def test_polygon_properties(vertices, circumradius, expected):
    polygon = Polygon(vertices, circumradius)

    # Unpack expected values
    interior_angle, area, side_length, perimeter, apothem = expected

    # Interior angle
    if interior_angle is not None:
        assert math.isclose(polygon.interior_angle, interior_angle, rel_tol=REL_TOL, abs_tol=ABS_TOL)

    # Area
    if area is not None:
        assert math.isclose(polygon.area, area, rel_tol=REL_TOL, abs_tol=ABS_TOL)

    # Side length
    if side_length is not None:
        assert math.isclose(polygon.side_length, side_length, rel_tol=REL_TOL, abs_tol=ABS_TOL)

    # Perimeter
    if perimeter is not None:
        assert math.isclose(polygon.perimeter, perimeter, rel_tol=REL_TOL, abs_tol=ABS_TOL)

    # Apothem
    if apothem is not None:
        assert math.isclose(polygon.apothem, apothem, rel_tol=REL_TOL, abs_tol=ABS_TOL)


def test_polygon_str():
    polygon = Polygon(3, 1)
    assert str(polygon) == "Polygon(vertices_number=3, circumradius=1)"


def test_polygon_vertex_and_edge_counts():
    polygon = Polygon(5, 10)
    assert polygon.count_vertices == 5
    assert polygon.count_edges == 5
    assert polygon.circumradius == 10


# --- Equality & Comparison Tests ---
@pytest.mark.parametrize(
    "p1, p2, expected_eq, expected_gt",
    [
        # Equality cases
        (Polygon(4, 10), Polygon(4, 10), True, False),    # Same polygon
        (Polygon(4, 10), Polygon(4, 5), False, True),     # Same vertices, different circumradius
        (Polygon(4, 10), Polygon(5, 10), False, False),   # Different vertices

        # Greater than cases (by area)
        (Polygon(6, 2), Polygon(3, 1), False, True),      # Larger hexagon > smaller triangle
        (Polygon(3, 1), Polygon(6, 2), False, False),     # Smaller triangle < larger hexagon
    ],
)
def test_polygon_equality_and_comparison(p1, p2, expected_eq, expected_gt):
    # Equality check
    assert (p1 == p2) is expected_eq
    assert (p1 != p2) is (not expected_eq)

    # Greater-than / less-than check
    assert (p1 > p2) is expected_gt
    assert (p1 < p2) is (not expected_eq and not expected_gt)

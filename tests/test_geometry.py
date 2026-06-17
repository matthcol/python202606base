

import pytest

from geometry import Point


@pytest.mark.parametrize(
        "x1, y1, x2, y2, expected_distance",
        [
            (1.0, 2.5, 1.0, 2.5, 0.0),
            (1.0, 2.5, 4.0, 6.5, 5.0),
            (4.0, 6.5, 1.0, 2.5, 5.0),
        ],
        ids=[
            "same point",
            "triangle 345",
            "triangle 345 reverse",
        ]
)
def test_point_distance(x1: float, y1: float, x2: float, y2: float, expected_distance: float):
    p1 = Point(x=x1, y=y1)
    p2 = Point(x=x2, y=y2)
    actual_distance = p1.distance(p2)
    assert actual_distance == expected_distance


def test_point_translate(point_a: Point):
    point_a.translate(1.0, -1.0)
    assert 13.5 == point_a.x
    assert 6.25 == point_a.y
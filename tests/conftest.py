import pytest

from geometry import Point


@pytest.fixture
def point_a() -> Point:
    return Point(x=12.5, y=7.25, name="A")
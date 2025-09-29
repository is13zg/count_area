import math
import pytest
from geometry import Triangle, get_area


def test_triangle_area():
    c = Triangle(3, 4, 5)
    assert get_area(c) == pytest.approx(3.0 * 4.0 * 0.5)


def test_invalid_triangle():
    with pytest.raises(ValueError):
        c = Triangle(1, 2, 3)

    with pytest.raises(ValueError):
        c = Triangle(1, 2, -3)

    with pytest.raises(ValueError):
        c = Triangle(0.5, 0, 0.5)


def test_right_triangle():
    assert Triangle(3, 4, 5).is_right_triangle()
    assert Triangle(12, 13, 5).is_right_triangle()
    assert not Triangle(1.5, 2, 3).is_right_triangle()

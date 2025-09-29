import math
import pytest
from geometry import Circle, get_area


def test_circle_area():
    c = Circle(2.0)
    assert get_area(c) == pytest.approx(math.pi * 4.0)


def test_invalid_circle():
    for r in [0, -1, -0.01, None]:
        with pytest.raises(ValueError):
            Circle(r)

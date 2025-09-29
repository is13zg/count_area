from dataclasses import dataclass
import pytest
from geometry import get_area, Shape


@dataclass
class Rectangle(Shape):
    w: float
    h: float

    def get_area(self):
        return self.w * self.h


def test_get_area_rectangle():
    shape = Rectangle(2, 5)
    assert get_area(shape) == pytest.approx(10.0)

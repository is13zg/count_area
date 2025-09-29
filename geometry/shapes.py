from abc import ABC, abstractmethod
from dataclasses import dataclass
from math import pi


class Shape(ABC):

    @abstractmethod
    def get_area(self):
        pass


@dataclass
class Circle(Shape):
    radius: float

    def get_area(self) -> float:
        return self.radius ** 2 * pi


@dataclass
class Triangle(Shape):
    a: float
    b: float
    c: float

    def get_area(self) -> float:
        p = 0.5 * (self.a + self.b + self.c)
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def is_right_triangle(self, eps: float = 1e-9) -> bool:
        x, y, z = sorted((self.a, self.b, self.c))
        return z ** 2 - x ** 2 - y ** 2 < eps * (x * x + y * y + z * z)

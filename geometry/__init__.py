from .shapes import Shape
from .shapes import Circle
from .shapes import Triangle
from .utils import get_area

__all__ = [name for name, obj in globals().items()
           if not name.startswith("_")]

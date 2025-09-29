from geometry.shapes import Shape


def get_area(obj: Shape) -> float:
    if hasattr(obj, "get_area") and callable(obj.get_area):
        return float(obj.get_area())
    raise TypeError(f"No way to calculate area {type(obj)}")

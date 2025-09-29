import geometry

if __name__ == "__main__":
    cr = geometry.Circle(10)
    tr = geometry.Triangle(300, 400, 500)

    print(geometry.get_area(cr))
    print(geometry.get_area(tr))
    print(tr.is_right_triangle())

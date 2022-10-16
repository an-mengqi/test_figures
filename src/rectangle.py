from src.base import Figure


class Rectangle(Figure):
    """Creates a rectangle with given sides"""
    def __init__(self, side1, side2):
        super().__init__()
        self.name = "rectangle"
        self.area = side1 * side2
        self.perimeter = side1 + side2

from src.base import Figure


class Rectangle(Figure):
    NAME = "rectangle"
    """Creates a rectangle with given sides"""
    def __init__(self, side1, side2):
        super().__init__()
        self.side1 = side1
        self.side2 = side2

    @property
    def area(self):
        return self.side1 * self.side2

    @property
    def perimeter(self):
        return self.side1 + self.side2

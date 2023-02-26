import math

from src.base import Figure


class Triangle(Figure):
    NAME = "triangle"
    """Checks if it is possible to create a triangle with given sides and
     either creates it, or raises an error"""
    def __init__(self, side1, side2, side3):
        super().__init__()
        if (side1 + side2) > side3 and \
                (side1 + side3) > side2 and \
                (side2 + side3) > side1:
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3
        else:
            raise ValueError("These sides cannot create a triangle!!!")

    @property
    def perimeter(self):
        return (self.side1 + self.side2 + self.side3) / 2

    @property
    def area(self):
        return math.sqrt(self.perimeter
                         * (self.perimeter - self.side1)
                         * (self.perimeter - self.side2)
                         * (self.perimeter - self.side3))

import math

from src.base import Figure


class Triangle(Figure):
    """Checks if it is possible to create a triangle with given sides and
     either creates it, or raises an error"""
    def __init__(self, side1, side2, side3):
        super().__init__()
        if (side1 + side2) > side3 and \
                (side1 + side3) > side2 and \
                (side2 + side3) > side1:
            self.name = "triangle"
            self.perimeter = (side1 + side2 + side3) / 2
            self.area = math.sqrt(self.perimeter
                                  * (self.perimeter - side1)
                                  * (self.perimeter - side2)
                                  * (self.perimeter - side3))
        else:
            raise ValueError("These sides cannot create a triangle!!!")
        
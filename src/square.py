from src.base import Figure


class Square(Figure):
    NAME = "square"
    """Creates a square with given side"""
    def __init__(self, side1):
        super().__init__()
        self.side1 = side1

    @property
    def area(self):
        return self.side1 ** 2

    @property
    def perimeter(self):
        return self.side1 * 2

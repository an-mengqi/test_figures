from src.base import Figure


class Square(Figure):
    """Creates a square with given side"""
    def __init__(self, side1):
        super().__init__()
        self.name = "square"
        self.area = side1 ** 2
        self.perimeter = side1 * 2

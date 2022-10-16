from src.base import Figure


class Circle(Figure):
    """Creates a circle with given radius"""
    def __init__(self, radius):
        super().__init__()
        self.name = "circle"
        self.area = 3.14 * (radius ** 2)
        self.perimeter = (2 * radius) * 3.14

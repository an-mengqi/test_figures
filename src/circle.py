from src.base import Figure


class Circle(Figure):
    NAME = "circle"
    """Creates a circle with given radius"""
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    @property
    def area(self):
        return 3.14 * (self.radius ** 2)

    @property
    def perimeter(self):
        return (2 * self.radius) * 3.14

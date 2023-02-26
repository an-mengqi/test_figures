from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


class TestBase:

    def get_figure_attr(self, figure, attribute):
        return getattr(figure, attribute)

    def create_figure(self, figure):
        """Create a figure with right sides"""
        if figure == "triangle":
            return Triangle(4, 5, 7)
        elif figure == "square":
            return Square(5)
        elif figure == "rectangle":
            return Rectangle(3, 6)
        elif figure == "circle":
            return Circle(4)
        else:
            raise AttributeError("Wrong figure name was entered!")

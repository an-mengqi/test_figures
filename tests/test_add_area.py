import numbers
import pytest

from test_base import TestBase


class TestAddArea(TestBase):

    def test_add_area_positive(self):
        """Work of add_area function"""
        triangle = TestBase.create_figure(self, "triangle")
        square = TestBase.create_figure(self, "square")
        two_figures_area = triangle.add_area(square)
        assert isinstance(two_figures_area, numbers.Number) is True

    def test_add_area_negative(self):
        """Error is raised when given value to add_area func is not a figure"""
        not_a_figure = 'not a figure'
        triangle = TestBase.create_figure(self, "triangle")
        with pytest.raises(ValueError):
            triangle.add_area(not_a_figure)

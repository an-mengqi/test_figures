import pytest

from src.triangle import Triangle
from test_base import TestBase


class TestCreateFigure(TestBase):

    @pytest.mark.parametrize("figure_name", ["triangle",
                                             "square",
                                             "rectangle",
                                             "circle"])
    def test_create_figure(self, figure_name):
        """Figures with right sides are created (exist)"""
        figure = TestBase.create_figure(self, figure_name)
        assert figure is not None

    def test_create_triangle_negative(self):
        """ValueError is raised when it is impossible to create a triangle
         with given sides"""
        with pytest.raises(ValueError):
            Triangle(4, 5, 10)

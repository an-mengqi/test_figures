import numbers
import pytest

from test_base import TestBase


class TestGetAttr(TestBase):

    @pytest.mark.parametrize("figure_name", ["triangle",
                                             "square",
                                             "rectangle",
                                             "circle"])
    def test_get_figure_name(self, figure_name):
        """Figure has attribute 'name' with the right value"""
        figure = TestBase.create_figure(self, figure_name)
        assert hasattr(figure, "NAME")
        figure_attribute = TestBase.get_figure_attr(self, figure, "NAME")
        assert figure_attribute == figure_name

    @pytest.mark.parametrize("figure_name", ["triangle",
                                             "square",
                                             "rectangle",
                                             "circle"])
    def test_get_figure_perimeter(self, figure_name):
        """Figure's perimeter is counted and it is a number"""
        figure = TestBase.create_figure(self, figure_name)
        assert hasattr(figure, "perimeter")
        figure_attribute = TestBase.get_figure_attr(self, figure, "perimeter")
        assert isinstance(figure_attribute, numbers.Number) is True

    @pytest.mark.parametrize("figure_name", ["triangle",
                                             "square",
                                             "rectangle",
                                             "circle"])
    def test_get_figure_area(self, figure_name):
        """Figure's area is counted and it is a number"""
        figure = TestBase.create_figure(self, figure_name)
        assert hasattr(figure, "area")
        figure_attribute = TestBase.get_figure_attr(self, figure, "area")
        assert isinstance(figure_attribute, numbers.Number) is True

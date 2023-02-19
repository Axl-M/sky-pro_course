import pytest
from Circle_class import Circle

class TestCircle:
    def test_get_radius(self):
        circle = Circle(1)
        assert circle.get_radius() == 1, "Ошибка в радиусе"

    def test_get_diametr(self):
        circle = Circle(1)
        assert circle.get_diametr() == 2, "Ошибка в диаметре"

    def test_get_perimetr(self):
        circle = Circle(1)
        assert round(circle.get_perimetr(), 2) == 6.28, "Ошибка в периметре"

    def test_init_type_error(self):
        with pytest.raises(TypeError):
            circle = Circle("1")

    def test_init_value_error(self):
        with pytest.raises(ValueError):
            circle = Circle(-1)
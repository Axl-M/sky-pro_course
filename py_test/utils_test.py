import pytest
from utils import double, get_circle_square, get_verbal_grade

# def test_double():
#     assert double(2) == 4

#
# def test_get_circle_square_normal_0():
#     square = get_circle_square(0)
#     assert square == 0, "Неверное значение для 0"
# def test_get_circle_square_normal_1():
#     square = get_circle_square(1)
#     assert round(square, 2) == 3.14, "Неверное значение для 1"
# def test_get_circle_square_normal_3():
#     square = get_circle_square(3)
#     assert round(square, 2) == 28.27, "Неверное значение для 3"
#
# def test_getcircle_square_value_error():
#     with pytest.raises(ValueError):
#         get_circle_square(-2)
# def test_get_circle_square_type_error():
#     with pytest.raises(TypeError):
#         get_circle_square("2")


grade_parameters = [
    (2, "Плохо"),
    (3, "Удовлетворительно"),
    (4, "Хорошо"),
    (5, "Отлично")
]

@pytest.mark.parametrize("grade_int, grade_str", grade_parameters)
def test_get_verbal_grade(grade_int, grade_str):
    assert get_verbal_grade(grade_int) == grade_str

# Добавляем тесты на выбрасываемые исключения:
# def test_get_verbal_grade_value_error_1():
#     with pytest.raises(ValueError):
#         assert get_verbal_grade(1)
# def test_get_verbal_grade_value_error_6():
#     with pytest.raises(ValueError):
#         assert get_verbal_grade(6)
# def test_get_verbal_grade_type_error_str():
#     with pytest.raises(TypeError):
#         assert get_verbal_grade("5")
# def test_get_verbal_grade_type_error_float():
#     with pytest.raises(TypeError):
#         assert get_verbal_grade(5.0)

# параметризируем всё
grade_exceptions = [
    (1, ValueError),
    (6, ValueError),
    ("5", TypeError),
    (5.0, TypeError),
]

@pytest.mark.parametrize("grade_int, exception", grade_exceptions)
def test_get_verbal_grade_exceptions(grade_int, exception):
    with pytest.raises(exception):
        assert get_verbal_grade(grade_int)
import pytest
from app import sum_func

import conftest

# делаем фикстуры для чисел
# class TestSumFunc:
#     def test_sum_positive(self):
#         c = sum_func(1, 1)
#         assert c == 2
#     def test_sum_positive_and_negative(self):
#         c = sum_func(1, -1)
#         assert c ==  0
#     def test_sum_negative2(self):
#         c = sum_func(-30, -10)
#         assert c == -40


# фикстуры можно вынести в отдельный файл conftest.ру
# @pytest.fixture()
# def positive_numbers():
#     return [1, 1]
#
# @pytest.fixture()
# def negative_numbers():
#     return [-10, -30]
#
# @pytest.fixture()
# def positive_and_negative_numbers():
#     return [1, -1]

class TestSumFunc:
    def test_sum_positive(self, positive_numbers):
        c = sum_func(positive_numbers[0], positive_numbers[1])
        assert c    > 0
        assert c == 2
    def test_sum_negative(self, negative_numbers):
        c = sum_func(negative_numbers[0], negative_numbers[1])
        assert c    < 0
        assert c ==  -40
    def test_sum_positive_and_negative(self, positive_and_negative_numbers):
        c = sum_func(positive_and_negative_numbers[0], positive_and_negative_numbers[1])
        assert c == 0

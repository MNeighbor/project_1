import project_1
import unittest
import math


class ProjectTest(unittest.TestCase):
    """Тестирует программу project_1.py"""

    def test_min_numeric(self):
        """Функция находящая минимальное значение работает правильно?"""
        new_value = project_1.min_numeric(['1', '4', '2', '3'])
        self.assertEquals(new_value, 1.0)

    def test_max_numeric(self):
        """Функция находящая максимальное значение работает правильно?"""
        new_value = project_1.max_numeric(['1', '4', '2', '3'])
        self.assertEquals(new_value, 4.0)

    def test_sum_numeric(self):
        """Функция находящая сумму чисел работает правильно?"""
        new_value = project_1.sum_numeric(['1', '4', '2', '3'])
        self.assertEquals(new_value, 10.0)

    def test_mult_numeric(self):
        """Функция находящая произведение чисел работает правильно?"""
        new_value = project_1.mult_numeric([['1', '4', '2', '3'], ["2", "8", "4", "6"]])
        self.assertEquals(new_value, 9216.0)

    def test_mult_numeric_overflow(self):
        """На вход подается бесконечность, программа при этом работает?"""
        new_value = project_1.mult_numeric(math.inf)
        self.assertEquals(new_value, float("inf"))

    def test_read_file(self):
        """На чтение подается файл, чтение происходит?"""
        new_value = project_1.read_file(r"project_1.txt")
        self.assertEquals(new_value, [['1', '4', '2', '3']])

if __name__ == '__main__':
    unittest.main()

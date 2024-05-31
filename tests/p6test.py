import unittest
from papk.p6 import ploshad

class TestsOfWordsCounter(unittest.TestCase): # создаем класс тестирования наследующий класс юнит тестов
    def test_otric_len(self):
        self.assertEqual(ploshad(-1, 2), "длина не может быть отрицательной") # проверка на отрицательность длины
    def test_null_len(self):
        self.assertEqual(ploshad(0, 2), "длина не может равняться нулю") # проверка на то, является ли длина нулем
    def test_otric_wid(self):
        self.assertEqual(ploshad(2, -1), "ширина не может быть отрицательной") # проверка на отрицательность ширины
    def test_null_wid(self):
        self.assertEqual(ploshad(2, 0), "ширина не может равняться нулю") # проверка на то, является ли ширина нулем
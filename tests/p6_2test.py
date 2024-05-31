import unittest
from p6_2 import sumMainDiagonal


class TestSum(unittest.TestCase):
    def testEmpty(self): # тест пустой матрицы
            self.assertEqual(sumMainDiagonal([]), 0)

    def testOneEl(self): # тест матрицы из одного элемента
        self.assertEqual(sumMainDiagonal([[1]]), 1)

    def testMatrix(self): # тест матрицы подхзодящей по условию
        self.assertEqual(sumMainDiagonal([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]), 15)

    def testNonSq(self): # тест неквадратной матрицы
        with self.assertRaises(ValueError):
            sumMainDiagonal([
                [1, 2, 3],
                [4, 5, 6],
            ])
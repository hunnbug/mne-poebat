import unittest
from papk.p6 import countWords

class TestsOfWordsCounter(unittest.TestCase): # создаем класс тестирования наследующий класс юнит тестов
    def testOneWord(self): # проверка на одно слово
        self.assertEqual("Hello", 1) 
    def testTwoWords(self): # проверка на два слова
        self.assertEqual("Hello, World!", 2)
    def testNoneWords(self): # проверка на отсутствие слов
        self.assertEqual("", 0)
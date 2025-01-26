#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
class TestMax(unittest.TestCase):

    def test_int_list(self):
        intList = [1, 2, 3, 4, 5]  # test with int
        self.assertEqual(max_integer(intList), 5)

    def test_float_list(self):
        floatList = [1.1, 2.22, 6.9, 42.0, -12.64]  # test with float
        self.assertEqual(max_integer(floatList), 42.0)

    def test_list_of_strings(self):
        stringList = ["i", "am", "Heinsenberg"]  # test with string
        self.assertEqual(max_integer(stringList), "Heinsenberg")

if __name__ == '__main__':
    unittest.main()

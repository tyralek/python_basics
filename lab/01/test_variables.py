import unittest
from .variables import *

class Test(unittest.TestCase):


    def test_exercisse_1(self):
        self.assertEqual(my_int, 10)

    def test_exercisse_2(self):
        self.assertEqual(my_string, 'team')

    def test_exercisse_3(self):
        self.assertEqual(a, True)
        self.assertEqual(b, False)

    def test_exercisse_4(self):
        self.assertEqual(my_float, 3.1415)

    def test_exercisse_5(self):
        self.assertEqual(first_func(), 1000)


if __name__ == "__main__":
    unittest.main()
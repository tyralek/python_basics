'''
@author: rozieblo

Lambda exercise
'''
import unittest

__mul__ = lambda

class Lambdas:
    add = lambda
    find_greater = lambda

class Test(unittest.TestCase):

    power = lambda
    cmp_int = lambda
    cmp_tuple = lambda

    def setUp(self):
        self.lmbd = Lambdas()
        pass

    def tearDown(self):
        pass

    def test_simple_lambdas(self):
        self.assertEqual(__mul__(7, 6), 42)
        self.assertEqual(self.power(5, 3), 125)
        self.assertEqual(self.lmbd.add(34, -28), 6)

    def test_compex_lambdas(self):
        # find first greater integer in list than given
        my_int_list = [ 2, 4, 7, 6, 8 ]
        self.assertEqual(self.lmbd.find_greater(7, my_int_list, self.cmp_int), 8)
        self.assertEqual(self.lmbd.find_greater(9, my_int_list, self.cmp_int), None)

        # find first tuple in list, where both elements are greater that in given tuple
        # order in tuple doesn't matter
        my_tuple_list = [ (3, 4), (3, 10), (45, 2), (28, 28), (-1, 192) ]
        self.assertEqual(self.lmbd.find_greater((1, 1), my_tuple_list, self.cmp_tuple), (3, 4))
        self.assertEqual(self.lmbd.find_greater((2, 34), my_tuple_list, self.cmp_tuple), None)
        self.assertEqual(self.lmbd.find_greater((9, 2), my_tuple_list, self.cmp_tuple), (3, 10))
        self.assertEqual(self.lmbd.find_greater((190, -3), my_tuple_list, self.cmp_tuple), (-1, 192))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

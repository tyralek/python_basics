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

        # find first tuple in list, where both elements are greater than in given tuple
        # order in tuple doesn't matter
        my_tuple_list = [ (3, 4), (3, 10), (45, 2), (28, 28), (-1, 192) ]
        self.assertEqual(self.lmbd.find_greater((1, 1), my_tuple_list, self.cmp_tuple), (3, 4))
        self.assertEqual(self.lmbd.find_greater((2, 34), my_tuple_list, self.cmp_tuple), None)
        self.assertEqual(self.lmbd.find_greater((9, 2), my_tuple_list, self.cmp_tuple), (3, 10))
        self.assertEqual(self.lmbd.find_greater((190, -3), my_tuple_list, self.cmp_tuple), (-1, 192))

    def test_smple_map(self):
        items = [2, 6, 18, -5]
        sqr_lmbd = lambda
        # sqr = items ** 2 using map and sqr_lmbd
        sqr = list
        self.assertEqual(sqr, [4, 36, 324, 25])

    def test_complex_map(self):
        items = [(2, 3), (3, 3), (4, -1), (-2, 0)]
        # using maps and
        # using lambdas mul and self.power
        # for each tuple in itmes
        # count multiplications and power and
        # prepare new list of tuples with results
        # ex.:
        # items = [ (a, b), (c, d) ]
        # result = [ ( a * b, a ** b), (c * d, c ** d) ]
        mul = lambda
        result = []
        for i in items:
            result.append(tuple(map))
        self.assertEqual(result, [(6, 8), (9, 27), (-4, 0.25), (0, 1)])

    def test_filter(self):
        items = range(-10, 20)
        # using filter and lmbd find numbers not divided by 2 and 3 in items
        lmbd = lambda
        result = list
        self.assertEqual(result, [-7, -5, -1, 1, 5, 7, 11, 13, 17, 19])

    def test_reduce(self):
        items = range(0, 100)
        # using lambdas and reduce find sum of odd and even numbers in items
        sum_even = lambda
        sum_odd = lambda
        result_even = 0
        result_odd = 0
        self.assertEqual(result_even, 2450)
        self.assertEqual(result_odd, 2500)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

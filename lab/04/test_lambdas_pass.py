'''
@author: rozieblo

Lambda exercise
'''
import unittest
from functools import reduce

__mul__ = lambda a, b: a * b

class Lambdas:
    add = lambda self, a, b: a + b
    find_greater = lambda self, a, list, cmp: self.greater(a, list, cmp)

    def greater(self, a, list, cmp):
        for i in list:
            if cmp(i, a) > 0:
                return i
        return None

class Test(unittest.TestCase):

    power = lambda self, a, b: a ** b
    cmp_int = lambda self, a, b: a > b
    cmp_tuple = lambda self, a, b: (a[0] > b[0] and a[1] > b[1]) or \
                                    (a[0] > b[1] and a[1] > b[0])

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
        sqr_lmbd = lambda a: a ** 2
        # sqr = items ** 2 using map and sqr_lmbd
        sqr = list(map(sqr_lmbd, items))
        self.assertEqual(sqr, [4, 36, 324, 25])

    def test_complex_map(self):
        items = [(2, 3), (3, 3), (4, -1), (-2, 0)]
        # using lambdas mul and self.power
        # for each tuple in itmes 
        # count multiplications and power and 
        # prepare new list of tuples with results
        # ex.:
        # items = [ (a, b), (c, d) ]
        # result = [ ( a * b, a ** b), (c * d, c ** d) ]
        mul = lambda a, b: a * b
        func = [mul, self.power]
        result = []
        for i in items:
            result.append(tuple(map(lambda x: x(i[0], i[1]), func)))
        self.assertEqual(result, [(6, 8), (9, 27), (-4, 0.25), (0, 1)])

    def test_filter(self):
        items = range(-10, 20)
        # using filter and lmbd find numbers not divided by 2 and 3 in items
        lmbd = lambda a: a % 2 and a % 3
        result = list(filter(lmbd, items))
        self.assertEqual(result, [-7, -5, -1, 1, 5, 7, 11, 13, 17, 19])

    def test_reduce(self):
        items = range(0, 100)
        # using lambdas and reduce find sum of odd and even numbers in items
        sum_even = lambda a, b: a + (b % 2 == 0) * b
        sum_odd = lambda a, b: a + (b % 2) * b
        result_even = reduce(sum_even, items)
        result_odd = reduce(sum_odd, items)
        self.assertEqual(result_even, 2450)
        self.assertEqual(result_odd, 2500)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

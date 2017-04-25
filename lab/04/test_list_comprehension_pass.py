'''
@author: rozieblo

List comprehension exercise
'''
import unittest
import time

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_list_comp_simple(self):
        items = [-2, 3, 0, 2.5, -1, 6]
        squared = [x ** 2 for x in items]
        even = [x for x in items if x % 2 == 0]
        doubled_odds = [x * 2 for x in items if x % 2 == 1]

        self.assertEqual(squared, [4, 9, 0, 6.25, 1, 36])
        self.assertEqual(even, [-2, 0, 6])
        self.assertEqual(doubled_odds, [6, -2])

    def test_list_comp_time(self):
        len = 5000000
        start = time.time()
        noprimes = []
        items = range(len)
        for i in range(2, int(len ** 0.5)):
            for j in range(i * 2, len, i):
                noprimes.append(j)
        time_loop = time.time() - start
        print('Time with loop: {}'.format(time_loop))
        start = time.time()
        noprimes_comp = [j for i in range(2,int(len ** 0.5)) for j in range(i * 2, len, i)]
        time_comp = time.time() - start
        print('Time with comprehension: {}'.format(time_comp))
        self.assertEqual(noprimes, noprimes_comp)
        self.assertGreater(time_loop, time_comp)

    def test_list_comp_string(self):
        words = "Litwo! Ojczyzno moja! Ty jesteś jak zdrowie".split()
        result = [[x.upper(), x.lower(), len(x)] for x in words]
        self.assertEqual(result, \
            [['LITWO!', 'litwo!', 6],
             ['OJCZYZNO', 'ojczyzno', 8],
             ['MOJA!', 'moja!', 5],
             ['TY', 'ty', 2],
             ['JESTEŚ', 'jesteś', 6],
             ['JAK', 'jak', 3],
             ['ZDROWIE', 'zdrowie', 7]])

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

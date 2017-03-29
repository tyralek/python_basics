'''
@author: ltyrala

Container exercise
'''
import unittest


class SomeMagic:

    def __init__(self, x):
        self.x = x


class Test(unittest.TestCase):

    def setUp(self):
        self.list = [1, 2, 3, 4]
        self.flight_rating = {'batman': 4,
                              'superman': 10,
                              'zorro': 0, }

    def tearDown(self):
        pass

    def test_list_multiply(self):
        self.list *= 3
        self.assertEqual([1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4], self.list)

    def test_list_remove_operation(self):
        # remove first 4 occurrence on list
        self.list.remove(4)
        self.assertEqual([1, 2, 3], self.list)

        # remove last element from list
        last = self.list.pop()
        self.assertEqual(2, len(self.list))
        self.assertEqual(last, 3)

        # remove first element from list
        first = self.list.pop(0)
        self.assertEqual(1, len(self.list))
        self.assertEqual(first, 1)

    def test_list_add_operration(self):
        # add 5 at end of list
        self.list.append(5)
        self.assertEqual([1, 2, 3, 4, 5], self.list)

        # add 0 at list beginning
        self.list.insert(0, 0)
        self.assertEqual([0, 1, 2, 3, 4, 5], self.list)

        # add new_list at the end
        new_list = [4, 4, 4]
        self.list.extend(new_list)
        self.assertEqual([0, 1, 2, 3, 4, 5, 4, 4, 4], self.list)

        # count "4" occurrence
        count_four = self.list.count(4)
        self.assertEqual(4, count_four)

    def test_list_comprehention(self):
        # Create list of SomeMagic objects, for all values form self.list
        sm_list = [SomeMagic(x) for x in self.list]
        self.assertTrue(isinstance(sm_list[0], SomeMagic))
        self.assertTrue(sm_list[0].x == 1)

    def test_tuple(self):
        # convert self.list to tuple
        test_tuple = tuple(self.list)
        self.assertTrue(isinstance(test_tuple, tuple))
        self.assertTrue(test_tuple == (1, 2, 3, 4))

    def test_dict_access(self):
        # add hero: spiderman with rating 7
        self.flight_rating['spiderman'] = 7
        self.assertTrue('spiderman' in self.flight_rating)

        # find best flight hero
        best_value = 0
        hero = 'cat'
        for (key, value) in self.flight_rating.items():
            if value > best_value:
                hero = key
                best_value = value
        self.assertEqual('superman', hero)
        self.assertEqual(10, best_value)

        # remove superman from list
        del self.flight_rating['superman']
        self.assertEqual(0, self.flight_rating.get('superman', 0))

        # get current hero list
        hero_list = list(self.flight_rating.keys())
        hero_list.sort()
        self.assertEqual(['batman', 'spiderman', 'zorro'], hero_list)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

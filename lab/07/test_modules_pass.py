'''
Created on May 15, 2017

@author: pgaj
'''
import unittest
from collections import Counter, defaultdict, OrderedDict, namedtuple

Person = namedtuple('PersonTuppleNameSpeciallyForRafal', 'name, age')

class Test(unittest.TestCase):

    def test_counter_sequence(self):
        '''
        1st type of initialization (sqeuence)
        '''
        counter = Counter(['a', 'b', 'c', 'a', 'b', 'b'])
        self.assertEqual({'a': 2, 'b': 3, 'c': 1}, dict(counter))
        
    def test_counter_dict(self):
        '''
        2nd type of initialization (dict)
        '''
        counter = Counter({'a': 2, 'b': 3, 'c': 1})
        self.assertEqual({'a': 2, 'b': 3, 'c': 1}, dict(counter))
        
    def test_counter_names(self):
        '''
        3rd type of initialization (named parameters)
        '''
        counter = Counter(a=2, b=3, c=1)
        self.assertEqual({'a': 2, 'b': 3, 'c': 1}, dict(counter))
        
    def test_remove_zero_and_negative(self):
        '''
        remove all negative and zero counts from counter
        '''
        counter = Counter(a=0, b=3, c=-1)
        counter += Counter()
        self.assertEqual({'b': 3}, dict(counter))
        
    def test_default_dict(self):
        '''
        try to meet this requirement without assignment
        '''
        def_dict = defaultdict(lambda: -1)
        
        def_dict[0]
        def_dict[1]
        def_dict[2]
        
        self.assertEqual({0: -1, 1: -1, 2: -1}, dict(def_dict))

    def test_ordereddict_sort_by_key(self):
        '''
        Sort ordereddict by key
        '''
        people = {2: Person('Przemek', 26), 1: Person(age=35, name='Rafal'), 3: Person('Marcin', 25)}
        
        sorted_people = OrderedDict(sorted(people.items(), key=lambda item: item[0]))
        
        self.assertEqual([1,2,3], list(sorted_people.keys()))

    def test_ordereddict_sort_by_value(self):
        '''
        Sort ordereddict by age
        '''
        people = {1: Person('Przemek', 26), 2: Person(age=35, name='Rafal'), 3: Person('Marcin', 25)}
        
        sorted_people = OrderedDict(sorted(people.items(), key=lambda item: item[1].age))
        
        self.assertEqual([3,1,2], list(sorted_people.keys()))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
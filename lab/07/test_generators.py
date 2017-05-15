'''
Created on May 12, 2017

@author: pgaj
'''
import unittest
from datetime import datetime, timedelta
from timeit import default_timer as timer
from _collections_abc import generator

class WorkingDayGenerator:
    '''
    This class generates working days (mon-fri) to the end of year
    '''
    def __init__(self, year, month, init_day = 1):
        self.actual_date = datetime(year, month, init_day)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        '''
        Overloaded method, should raise StopIteration at the end of generation
        '''
        raise StopIteration
        return self.actual_date
    
    def next(self):
        '''
        Python 2.x compatibility
        '''
        return self.__next__()
    
    def get_next(self):
        '''
        Returns next working day
        '''
        return self.actual_date
    
    def is_end(self):
        '''
        Checks if this is end of generation
        '''
        return True
        
def gen_dates(count = 1000):
    '''
    Generates 'count' dates from today
    '''
    date = datetime.now()
    dates = []
    for _ in range(count):
        date += timedelta(days=1)
        dates.append(date)
    return dates
    

class Test(unittest.TestCase):

    def test_begining(self):
        gen = WorkingDayGenerator(2017, 1, 1)
        self.assertEqual(datetime(2017, 1, 2), next(gen))
    
    def test_end(self):
        gen = WorkingDayGenerator(2017, 12, 31)
        with self.assertRaises(StopIteration):
            next(gen)
            
    def test_month(self):
        gen = WorkingDayGenerator(2017, 12)
        working_days = [day for day in gen]
        self.assertEqual(20, len(working_days))
        
    def test_no_working_days(self):
        gen = WorkingDayGenerator(2017, 12, 30)
        working_days = [day for day in gen]
        self.assertEqual([], working_days)
        
    
    def test_year(self):
        gen = WorkingDayGenerator(2017, 1)
        working_days = [day for day in gen]
        self.assertEqual(260, len(working_days))
        
    def test_using_timeit(self):
        start = timer()
        gen_dates(1000000)
        self.assertTrue(timer() - start < 1)
    
    def test_generator_element_type(self):
        self.assertTrue(isinstance(gen_dates(), generator))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
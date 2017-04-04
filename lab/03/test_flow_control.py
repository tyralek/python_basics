'''
Created on Apr 4, 2017
@author: ltyrala
flow control training
'''
import unittest
from enum import Enum


class PrimeGenerator:

    def __init__(self):
        pass

    @staticmethod
    def is_prime(number):
        '''
        Test if number is prime,
        use for else loop

        :param number: some numeric value, grater then 0
        :type number: int
        :returns: True if number is prime
        :rtype: bool
        '''
        pass

    def get_prime_larger_then(self, number):
        '''
        Find first prime larger then number
        use while loop

        :param number: some numeric value, grater then 0
        :type number: int
        :returns: prime number
        :rtype: int
        '''
        pass

    def get_prime_smaller_then(self, number):
        '''
        Find first prime smaller then number
        use while loop

        :param number: some numeric value, grater then 0
        :type number: int
        :returns: prime number
        :rtype: int
        '''
        pass

    def get_range(self, start, stop):
        '''
        Get prime numbers between start and stop values

        :param start: some numeric value, grater then 0
        :type start: int
        :param stop: some numeric value, grater then 0
        :type stop: int
        :returns: prime number list
        :rtype: list(int)
        '''
        pass


class PKOQueue:
    '''
    PKO client queue,
    ServiceType - type of available service
    _service_dict defines number of workers
    _queue - clients on queue
    '''
    class ServiceType(Enum):
        C = 'Cash register'
        B = 'Bonds'
        L = 'Loans'

    def __init__(self, init_count=0):
        self._service_dict = {self.ServiceType.C: 0,
                              self.ServiceType.B: 0,
                              self.ServiceType.L: 0}
        self._queue = []
        self._count = init_count

    def open_service(self, service_type):
        '''
        open service type
        '''
        if service_type in self._service_dict:
            self._service_dict[service_type] += 1

    def close_service(self, service_type):
        if service_type in self._service_dict \
           and self._service_dict > 0:
                self._service_dict[service_type] -= 1

    def queue_add(self, service_type):
        if service_type in self._service_dict \
           and self._service_dict[service_type] > 0:
                self._count += 1
                self._queue.append((service_type, self._count))

    def queue_release(self, service_type):
        return self._queue_release_fair(service_type)

    def _queue_release_fair(self, service_type):
        if service_type in self._service_dict \
           and self._service_dict[service_type] > 0:
                return self._queue.pop(0)
        else:
            return None

    def _queue_release_prime(self, service_type):
        pass


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_is_prime_negative(self):
        prime_generator = PrimeGenerator()
        self.assertFalse(prime_generator.is_prime(-1))
        self.assertFalse(prime_generator.is_prime(-10))

    def test_is_prime(self):
        prime_generator = PrimeGenerator()
        self.assertTrue(prime_generator.is_prime(2))
        self.assertTrue(prime_generator.is_prime(3))
        self.assertTrue(prime_generator.is_prime(5))
        self.assertTrue(prime_generator.is_prime(13))
        self.assertTrue(prime_generator.is_prime(751))
        self.assertTrue(prime_generator.is_prime(997))

        self.assertFalse(prime_generator.is_prime(1))
        self.assertFalse(prime_generator.is_prime(4))
        self.assertFalse(prime_generator.is_prime(8))
        self.assertFalse(prime_generator.is_prime(9))
        self.assertFalse(prime_generator.is_prime(100))
        self.assertFalse(prime_generator.is_prime(999))
        self.assertFalse(prime_generator.is_prime(1000))
        self.assertFalse(prime_generator.is_prime(11111))

    def test_prime_larger(self):
        prime_generator = PrimeGenerator()
        self.assertEqual(prime_generator.get_prime_larger_then(1000000),
                         1000003)

    def test_prime_smaller(self):
        prime_generator = PrimeGenerator()
        self.assertEqual(prime_generator.get_prime_smaller_then(-10), 2)
        self.assertEqual(prime_generator.get_prime_smaller_then(0), 2)
        self.assertEqual(prime_generator.get_prime_smaller_then(1), 2)
        self.assertEqual(prime_generator.get_prime_smaller_then(47), 43)

    def test_get_prime_range(self):
        prime_generator = PrimeGenerator()
        self.assertEqual([41, 43, 47],
                         prime_generator.get_range(40, 47))
        self.assertEqual([2, 3, 5, 7],
                         prime_generator.get_range(-40, 7))

    def test_pko_queue(self):
        pko_queue = PKOQueue()
        pko_queue.open_service(pko_queue.ServiceType.C)
        pko_queue.queue_add(pko_queue.ServiceType.C)
        pko_queue.queue_add(pko_queue.ServiceType.C)
        pko_queue.queue_add(pko_queue.ServiceType.B)
        self.assertEqual((pko_queue.ServiceType.C, 1),
                         pko_queue.queue_release(pko_queue.ServiceType.C))
        self.assertEqual((pko_queue.ServiceType.C, 2),
                         pko_queue.queue_release(pko_queue.ServiceType.C))
        self.assertEqual(None,
                         pko_queue.queue_release(pko_queue.ServiceType.B))

    def test_pko_prime_priority(self):
        pko_queue = PKOQueue(10)
        pko_queue.open_service(pko_queue.ServiceType.C)
        pko_queue.queue_add(pko_queue.ServiceType.C)
        pko_queue.queue_add(pko_queue.ServiceType.C)
        pko_queue.queue_add(pko_queue.ServiceType.C)
        self.assertEqual((pko_queue.ServiceType.C, 11),
                         pko_queue.queue_release(pko_queue.ServiceType.C))
        self.assertEqual((pko_queue.ServiceType.C, 13),
                         pko_queue.queue_release(pko_queue.ServiceType.C))
        self.assertEqual((pko_queue.ServiceType.C, 12),
                         pko_queue.queue_release(pko_queue.ServiceType.C))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

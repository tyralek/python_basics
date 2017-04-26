'''
Created on Apr 25, 2017

@author: ltyrala
'''
import unittest
from enum import Enum
import random


class Vehicle:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def run(self):
        raise NotImplementedError()

    def get_current_speed(self):
        raise NotImplementedError()


class Car(Vehicle):

    class Manufacturer(Enum):
        Toyota = 0
        Mercedes = 1
        BMW = 2

    instance_count = 0

    def __new__(cls, *args, **kwargs):
        cls.instance_count += 1
        return super().__new__(cls)

    def __init__(self, manufacturer, max_speed):
        if not isinstance(manufacturer, self.Manufacturer):
            raise ValueError("manufacturer type must be Cat.Manufacturer")
        Vehicle.__init__(self, max_speed)
        self.current_speed = 0
        self.manufacturer = manufacturer

    def __eq__(self, lhs):
        return self.manufacturer == lhs.manufacturer

    def run(self):
        self.current_speed += 10
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def get_current_speed(self):
        return self.current_speed


class Test(unittest.TestCase):

    def setUp(self):
        Car.instance_count = 0

    def tearDown(self):
        pass

    def test_new(self):
        '''
        Create class Vehicle.
            - define __init__ method,
              accept max_speed value in object construction
              make max_speed an attribute
            - define methods: run, get_current_speed.
              rise NotImplementedError exception in each of them.
        '''
        vehicle = Vehicle(120)
        with self.assertRaises(NotImplementedError):
            vehicle.run()
        with self.assertRaises(NotImplementedError):
            vehicle.get_current_speed()
        self.assertEqual(vehicle.max_speed, 120)

    def test_child_new(self):
        '''
        Create child class Car.
            - Car inherits from Vehicle
            - Car has class variable instance_count = 0
            - define __new__ method,
              make sure correct type is returned
              accept all arguments
              increment instance_count variable
              https://docs.python.org/3/reference/datamodel.html#object.__new__
        '''
        self.assertEqual(Car.instance_count, 0)

        car_1 = Car(Car.Manufacturer.BMW, 222)
        self.assertEqual(Car.instance_count, 1)
        self.assertEqual(car_1.instance_count, 1)

        car_2 = Car(Car.Manufacturer.Mercedes, 111)
        self.assertEqual(Car.instance_count, 2)
        self.assertEqual(car_1.instance_count, 2)
        self.assertEqual(car_2.instance_count, 2)

        self.assertTrue(isinstance(car_1, Vehicle))
        self.assertTrue(type(car_1) is Car)

        self.assertTrue(isinstance(Car.__new__(Car, "ala ma kota"), Vehicle))

    def test_child_init(self):
        '''
            - define __init__ method,
              add attributes: manufacturer, max_speed
              raise exception if manufacturer is not allowed type
              store max speed to attribute
        '''
        with self.assertRaises(ValueError):
            car = Car("Fiat", 120)

        car = Car(Car.Manufacturer.BMW, 120)
        self.assertEqual(car.max_speed, 120)
        self.assertEqual(car.manufacturer, Car.Manufacturer.BMW)

    def test_child_methods(self):
        '''
            - implement run method, each run call exceeds current speed by 10.
              but current speed cannot exceed max sped.
            - implement get_current_speed method
        '''
        car = Car(Car.Manufacturer.Toyota, 22)
        self.assertEqual(car.get_current_speed(), 0)
        car.run()
        self.assertEqual(car.get_current_speed(), 10)
        car.run()
        car.run()
        car.run()
        car.run()
        self.assertEqual(car.get_current_speed(), 22)

    def test_equal(self):
        '''
            - assume that cars of the same manufacturer are equal
        '''
        car_t1 = Car(Car.Manufacturer.Toyota, 100)
        car_t2 = Car(Car.Manufacturer.Toyota, 120)
        car_b1 = Car(Car.Manufacturer.BMW, 130)
        car_b2 = Car(Car.Manufacturer.BMW, 140)

        self.assertTrue(car_t1 == car_t2)
        self.assertTrue(car_b1 == car_b2)
        self.assertTrue(car_t1 != car_b1)

    def test_try_catch(self):
        '''
        having list of cars, fix remove method
            - you need to use try list.remove(x) catch
        '''
        def remove_manufacturer(car_list, manufacturer):
            while True:
                try:
                    car_list.remove(Car(manufacturer, 0))
                except ValueError:
                    break

        manufacturer_list = [Car.Manufacturer(i % 3) for i in range(300)]
        random.shuffle(manufacturer_list)
        car_list = [Car(m, 150) for m in manufacturer_list]

        self.assertEqual(car_list.count(Car(Car.Manufacturer.BMW, 100)), 100)
        remove_manufacturer(car_list, Car.Manufacturer.BMW)
        self.assertEqual(car_list.count(Car(Car.Manufacturer.BMW, 100)), 0)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
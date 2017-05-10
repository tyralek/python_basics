'''
Created on May 10, 2017

@author: ltyrala
'''
import unittest
from enum import Enum


class CarState:

    class State(Enum):
        STOP = 0
        RUN = 1

    class CarStateException(Exception):
        pass

    def __init__(self, max_speed, speed_up=10):
        pass

    def turn(self):
        pass

    def run(self):
        pass

    class Contex():
        def __init__(self):
            pass

        def __call__(self):
            pass

        def get(self):
            return CarState.State.STOP


class Car:
    @CarState.Contex()
    def __init__(self, max_speed):
        self.state = CarState(max_speed, speed_up=10)
        self.speed = 0
        self.direction_angle = 0

    @CarState.Contex()
    @CarState.turn
    def turn(self, angle):
        if self.speed:
            self.direction_angle += angle
            self.direction_angle %= 360

    @CarState.Contex()
    @CarState.run
    def run(self, speed_up):
        self.speed += speed_up

    @CarState.Contex()
    def stop(self):
        self.speed = 0


class Test(unittest.TestCase):

    def test_turn(self):
        car = Car(20)
        self.assertEqual(CarState.Contex().get(), CarState.State.STOP)
        car.turn(20)
        with self.assertRaises(CarState.CarStateException):
            car.turn(220)

    def test_run(self):
        car = Car(15)
        car.run()
        self.assertEqual(CarState.Contex().get(), CarState.State.RUN)
        with self.assertRaises(CarState.CarStateException):
            car.run()

    def test_stop(self):
        car = Car(15)
        car.run()
        self.assertEqual(CarState.Contex().get(), CarState.State.RUN)
        car.stop()
        self.assertEqual(CarState.Contex().get(), CarState.State.STOP)
        with self.assertRaises(CarState.CarStateException):
            car.stop()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

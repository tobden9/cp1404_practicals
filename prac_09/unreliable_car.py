from car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance based on its reliability."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0

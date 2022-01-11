"""
Define a property that must have the same value for every class instance (object)
Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

Use the following code for this exercise.
"""


class Vehicle:
    color = 'White'

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def show(self):
        print(f'Color: {self.color}, Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}')


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


b1 = Bus('School Volvo', 180, 12)
b1.show()
c1 = Car('Audi Q5', 240, 18)
c1.show()

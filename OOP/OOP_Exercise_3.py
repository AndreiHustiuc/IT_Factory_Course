"""
Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
"""


class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


b1 = Bus('School Bus', 160, 35000)
print(f'Vehicle name: {b1.name}, Speed: {b1.max_speed}, Mileage: {b1.mileage}')

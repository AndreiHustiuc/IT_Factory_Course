class Driver:
    def __init__(self, name):
        self._name = name

    def __add__(self, other):
        return self._name + other

    def __str__(self):
        return f'Driver to {self._name}'


driver = Driver('Chrome')
print(driver + 'Firefox')

# todo: de incercat si alte metode bilt-in

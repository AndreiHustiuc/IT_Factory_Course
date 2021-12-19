class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greeting(self):
        print(f"Hello {self.name}!")
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age
    

h = Human("Andrei", 31)

h.greeting()
print(h.get_name())
h.set_age(48)
print(h.get_age())




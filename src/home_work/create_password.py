import random


class CreatePassword:
    characters = list()

    def password_length(self):
        pass

    @classmethod
    def lower_case(cls):
        return cls.characters.extend('abcdefghijklmnopqrstuvwxyz')

    def upper_case(self):
        return self.characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def number(self):
        return self.characters.extend('1234567890')

    def special(self):
        return self.characters.extend('!@#$%^&*()_')

    pwd = ''

    def generate_weak_password(self):
        pass

    def generate_medium_password(self):
        pass

    def generate_strong_password(self):
        pass


p = CreatePassword
print(p.lower_case())

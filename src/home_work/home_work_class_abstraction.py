"""
Design the test model for a Test Case
It should contain 3 abstract methods (setup, tear down and a steps definition)

Design 3 classes modeled by the Test Case Abstract one
One class should simulate a login functionality
One class corresponds to home page
One class the about page

Each class should have a constructor with parameters.
"""

from abc import ABC, abstractmethod
from pwinput import pwinput


class TestCase(ABC):
    @abstractmethod
    def setup(self):
        raise NotImplemented

    @abstractmethod
    def steps_definition(self):
        raise NotImplemented

    @abstractmethod
    def tear_down(self):
        raise NotImplemented


class LogIn(TestCase):
    def __init__(self, admin_name, admin_pwd):
        self._admin_name = admin_name
        self._admin_pwd = admin_pwd

    def setup(self):
        print('Setting up test')

    def steps_definition(self):
        print('Definition of steps')

    def tear_down(self):
        print('Tear down test')

    def login(self):
        user_name = input('Enter your username: ')
        pwd = pwinput('Enter your password: ')
        if user_name == self._admin_name and pwd == self._admin_pwd:
            print('Welcome ADMIN')
        elif len(user_name) != 0 and len(pwd) != 0:
            print('Log in successfull')
        else:
            print('No credentials introduced')
        


class HomePage(TestCase):
    def __init__(self, home_page_name):
        self._home_page_name = home_page_name
        
    def setup(self):
        print('Setting up test')

    def steps_definition(self):
        print('Definition of steps')

    def tear_down(self):
        print('Tear down test')

    def home_page(self):
        print(f'Welcome to {self._home_page_name}')


class AboutPage(TestCase):
    def __init__(self, year):
        self._year = year
    
    def setup(self):
        print('Setting up test')

    def steps_definition(self):
        print('Definition of steps')

    def tear_down(self):
        print('Tear down test')
        
    def about_page(self):
        print(f'CopyRight {self._year}')
        
        


user = LogIn('X', 'Y')
user.login()
user = HomePage('Facebook')
user.home_page()
user = AboutPage(2022)
user.about_page()

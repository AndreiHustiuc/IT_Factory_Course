"""

"""
from abc import ABC, abstractmethod


class MainModule(ABC):

    @abstractmethod
    def test_definition(self):
        raise NotImplemented

    @abstractmethod
    def test_execution(self):
        raise NotImplemented

    @abstractmethod
    def test_report(self):
        raise NotImplemented


class SecondModule(MainModule):
    def test_definition(self):
        print('Test definition')

    def test_execution(self):
        print('Test execution')

    def test_report(self):
        print('Test report')

    def define_html_report(self):
        print('Second Module HTML report')


class ThirdModule(MainModule):

    def test_definition(self):
        print('Define test number 3')

    def test_execution(self):
        print('Execute test number 3')

    def test_report(self):
        print('Test report number 3')


obj = SecondModule()
obj2 = ThirdModule()

# obj1 = MainModule()
# obj1.test_report()

for i in (obj, obj2):
    i.test_definition()
    i.test_execution()
    i.test_report()

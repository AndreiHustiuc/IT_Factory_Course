class Encapsulation:
    def public(self):
        print('Everyone can see me')

    def _protected(self):
        print('Access provided only to my kids')

    def __private(self):
        print('No one should touch me')


class Child(Encapsulation):
    def test(self):
        self.public()
        self._protected()
        #self.__private()      ///copiii nu au acces la private


o = Child()
o.test()
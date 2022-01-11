import math


class Triunghi:
    def __init__(self, latura, baza):
        self._latura = latura
        self._baza = baza

    def perimetru(self):
        res = (self._latura * 2) + self._baza
        return f'Perimetrul triunghiului este: {res}'

    def aria(self):
        h = math.sqrt(self._latura ** 2 - (self._baza / 2) ** 2)
        res = (h * self._baza) / 2
        return f'Aria triunghiului este: {res}'


t1 = Triunghi(4, 2)
print(t1.perimetru())
print(t1.aria())


class Dreptunghi:
    def __init__(self, lat, lung):
        self._lat = lat
        self._lung = lung

    def perimetru(self):
        res = 2 * (self._lat + self._lung)
        return f'Perimetrul dreptunghiului este: {res}'

    def aria(self):
        res = self._lat * self._lung
        return f'Aria dreptunghiului este: {res}'


d = Dreptunghi(3, 4)
print(d.perimetru())
print(d.aria())


class PoligonRegulat:
    def __init__(self, nr_lat, raza):
        self._nr_lat = nr_lat
        self._raza = raza

    def perimetru(self):
        lat = self._raza * 2 * math.sin(180 / self._nr_lat)
        res = self._nr_lat * lat
        return f'Perimetrul poligonului cu {self._nr_lat} laturi este: {res}'

    def aria(self):
        res = self._raza ** 2 * (self._nr_lat / 2) * math.sin(360 / self._nr_lat)
        return f'Aria poligonului cu {self._nr_lat} laturi este: {res}'


p = PoligonRegulat(11, 5)
print(p.perimetru())
print(p.aria())

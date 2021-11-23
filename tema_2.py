# perimetrul si aria unui triunghi isoscel
import math

a = b = float(input('Introduceti valoarea laturei triunghiului: '))
c = float(input('Introduceti valoarea bazei triunghiului: '))

perimetru_triunghi = a + b + c
h = math.sqrt(b**2 - (c/2)**2)
aria_triunghi = (h * c)/2

print(f'Perimetrul triunghiului este: {perimetru_triunghi}')
print(f'Aria triunghiului este: {aria_triunghi}')

# perimetrul si aria unui dreptunghi

lung = float(input('Introduceti lungimea dreptunghiului: '))
lat = float(input('Introduceti latimea dreptunghiului: '))

perimetru_dreptunghi = 2 * (lung + lat)
aria_dreptunghi = lung * lat

print(f'Perimetrul dreptunghiului este: {perimetru_dreptunghi}')
print(f'Aria dreptunghiului este: {aria_dreptunghi}')

#perimetrul si aria unui poligon regulat cu n laturi

n = int(input('Introduceti numarul de laturi: '))
r = float(input('Introduceti raza cercului circumscris poligonului: '))

aria_poligon = r ** 2 * (n/2) * math.sin(360/n)
latura = r * 2 * math.sin(180/n)
perimetru_poligon = n * latura

print(f'Perimetrul poligonului cu {n} laturi este: {perimetru_poligon}')
print(f'Aria poligonului cu {n} laturi este: {aria_poligon}')

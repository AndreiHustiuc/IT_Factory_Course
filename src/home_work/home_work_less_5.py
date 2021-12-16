# perimetrul si aria unui triunghi isoscel
import math

def perimetru_triunghi(a, c):
    perimetru_triunghi = a + a + c
    return f'Perimetrul triunghiului este: {perimetru_triunghi}'

def aria_triunghi(a, c):
    h = math.sqrt(a ** 2 - (c / 2) ** 2)
    aria_triunghi = (h * c) / 2
    return f'Aria triunghiului este: {aria_triunghi}'

a = float(input('Introduceti valoarea laturei triunghiului: '))
c = float(input('Introduceti valoarea bazei triunghiului: '))

print(perimetru_triunghi(a, c))
print(aria_triunghi(a, c))

# perimetrul si aria unui dreptunghi

def perimetru_dreptunghi(a, b):
    perimetru_dreptunghi = 2 * (a + b)
    return f'Perimetrul dreptunghiului este: {perimetru_dreptunghi}'

def aria_dreptunghi(a, b):
    aria_dreptunghi = a * b
    return f'Aria dreptunghiului este: {aria_dreptunghi}'

lung = float(input('Introduceti lungimea dreptunghiului: '))
lat = float(input('Introduceti latimea dreptunghiului: '))

print(perimetru_dreptunghi(lung, lat))
print(aria_dreptunghi(lung, lat))



# perimetrul si aria unui poligon regulat cu n laturi
def perimetru_poligon_regulat(n, r):
    latura = r * 2 * math.sin(180 / n)
    perimetru_poligon = n * latura
    return f'Perimetrul poligonului cu {n} laturi este: {perimetru_poligon}'

def aria_poligon_regulat(n, r):
    aria_poligon = r ** 2 * (n / 2) * math.sin(360 / n)
    return f'Aria poligonului cu {n} laturi este: {aria_poligon}'

num_lat = int(input('Introduceti numarul de laturi: '))
raza = float(input('Introduceti raza cercului circumscris poligonului: '))

print(perimetru_poligon_regulat(num_lat, raza))
print(aria_poligon_regulat(num_lat, raza))



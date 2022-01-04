"""
Generate a password
"""
import random

characters = list('abcdefghijklmnopqrstuvwxyz')
upper_case = True
special = True
numbers = False

if upper_case:
    characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

if special:
    characters.extend('!@#$%^&*()_')

if numbers:
    characters.extend('1234567890')

length = 15
pwd = ''

for i in range(length):
    pwd += random.choice(characters)

print(pwd)

#todo: test pentru a verifica corectitudinea functiei (result: strong -> daca contine cifre, uppercase si caractere speciale)

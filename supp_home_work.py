'''
1. Define a variable which will contain the whole alphabet
    2. Count how many vowels and consonants there are
    3. Secondly define another variable which takes the input from the user (a name)
    4. Using string slicing, check first if the letters from the user are part of the alphabet
    5. Try to use also a special character e.g. ß and check how to handle this case
'''

import string

alphabet = list(string.ascii_lowercase)
alphabet_string = ''.join(alphabet)
vowels = ['a', 'e', 'i', 'o', 'u']

how_many_vowels = 0
for i in alphabet:
    for j in vowels:
        if i == j:
            how_many_vowels = how_many_vowels + 1

how_many_consonants = len(alphabet) - how_many_vowels

print(f'In the alphabet are {how_many_vowels} vowels')
print(f'In the alphabet are {how_many_consonants} consonants')

exist = 0
name = input('Enter your name: ').lower()

for i in name[0:]:
    for j in alphabet[0:]:
        if i == j:
            exist = exist + 1

if len(name) == exist:
    print('All letters are in the alphabet')
else:
    print(f'There are {len(name) - exist} letter(s) that are not in the alphabet, please use only latin letters')


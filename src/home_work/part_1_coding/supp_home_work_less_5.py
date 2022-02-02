from math import pi
import random
import string

# 1: Convert radians into degrees
"""
Write a function in Python that accepts one numeric parameter. 
This parameter will be the measure of an angle in radians. 
The function should convert the radians into degrees and then return that value.
"""


def rad_to_deg(val):
    return (val * 180) / pi


print(rad_to_deg(3))
print('\n')

# ========================================

# 2: Sort a list

"""
Create a function in Python that accepts two parameters. 
The first will be a list of numbers. 
The second parameter will be a string that can be one of the following values: asc, desc, and none.
"""

# create a list of random numbers
random_numbers = [random.randint(1, 50) for i in range(1, 10)]
print(random_numbers)


# string_values = ['asc', 'desc', 'none']

def sort_list(val1, val2):
    if val2 == 'asc':
        val1.sort()
        return val1
    elif val2 == 'desc':
        val1.sort(reverse=True)
        return val1
    elif val2 == 'none':
        return val1
    else:
        return 'Wrong type of sorting'


print(sort_list(random_numbers, 'asc'))
print('\n')

# ==========================================

# 3: Convert a decimal number into binary
"""
Write a function in Python that accepts a decimal number and returns the equivalent binary number. 
To make this simple, the decimal number will always be less than 1,024, so the binary number returned will always be less than ten digits long.
"""


def dec_to_bin(x):
    bin = []

    while x > 1:
        r = x % 2
        bin.append(r)
        x = int(x / 2)

    bin.append(x)
    bin.reverse()
    return bin


dec_num = 14
val_bin = ''

for i in dec_to_bin(dec_num):
    val_bin = val_bin + str(i)

print(f'The value of {dec_num} in binary is {val_bin}')
print('\n')

# 4: Count the vowels in a string
"""
Create a function in Python that accepts a single word and returns the number of vowels in that word. 
In this function, only a, e, i, o, and u will be counted as vowels — not y.
"""


def generate_random_word():
    alphabet = list(string.ascii_lowercase)
    word_length = random.randint(10, 15)
    word = ''
    num = 0

    while num < word_length:
        index = random.randint(1, len(alphabet) - 1)
        word += alphabet[index]
        num = num + 1

    return word


def count_vowels(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    num = 0
    for i in word:
        for j in vowels:
            if i == j:
                num = num + 1
    return num


random_word = generate_random_word()

print(f'In the word -> {random_word} are {count_vowels(random_word)} vowels')
print('\n')

# ==================================
# 5: Hide the credit card number

"""
Write a function in Python that accepts a credit card number. 
It should return a string where all the characters are hidden with an asterisk except the last four. 
For example, if the function gets sent "4444444444444444", then it should return "4444".
"""


def hide_card_number(num):
    my_list = list(num)

    for i in range(len(my_list)):
        if i <= len(my_list) - 5:
            my_list[i] = '*'

    for y in my_list:
        print(y, end='')


hide_card_number('4444444444444444')
print('\n')

# 6: Are the Xs equal to the Os?
"""
Create a Python function that accepts a string. 
This function should count the number of Xs and the number of Os in the string. 
It should then return a boolean value of either True or False
"""


def compare(word):
    num_x = 0
    num_o = 0

    for i in word.lower():
        if i == 'x':
            num_x = num_x + 1
        elif i == 'o':
            num_o = num_o + 1

    if num_x == 0 and num_o == 0:
        return 'There is no this letters X or O'
    elif num_x == num_o:
        return True
    else:
        return False


print(compare(random_word))
print('\n')

# =====================================
# 7: Create a calculator function
"""
Write a Python function that accepts three parameters. 
The first parameter is an integer. The second is one of the following mathematical operators: +, -, /, or . 
The third parameter will also be an integer.
"""


def calculator(num1, operator, num2):
    result = f'{num1} {operator} {num2}'
    return eval(result)


print(calculator(33, '*', 4))
print('\n')

# ====================================
# 8: Give me the discount
"""
Create a function in Python that accepts two parameters. 
The first should be the full price of an item as an integer. 
The second should be the discount percentage as an integer.
"""


def discount(full_price, discount):
    result = full_price - ((full_price * discount) / 100)
    return result


print(discount(100, 2))
print('\n')

# 9: Just the numbers
"""
Write a function in Python that accepts a list of any length that contains a mix of non-negative integers and strings. 
The function should return a list with only the integers in the original list in the same order.
"""


def filter_numbers(lst):
    num_lst = []
    for item in lst:
        if type(item) == int:
            num_lst.append(item)

    return num_lst


print(filter_numbers(['apple', 2, 5, 12, 3, 'orange', 'car', 2, 45, 'sun']))
print('\n')

# 10: Repeat the characters
"""
Create a Python function that accepts a string. The function should return a string, with each character in the original string doubled. 
If you send the function "now" as a parameter, it should return "nnooww," and if you send "123a!", it should return "112233aa!!".
"""


def double_word(str):
    result = ''
    for i in str:
        result = result + i * 2
    return result


print(double_word('123abc'))
print('\n')

# 11: 1. Define a variable containing a matrix with x rows, x columns
#     2. Swap the rows with the columns

"""
Example
input
1, 2, 3, 2, 5
4, 1, 7, 2, 9
13, 2, 3, 2, 5
11, 1, 5, 1, 2
3, 6, 10, 12, 11

output
1, 4, 13, 11, 3
2, 1, 2, 1, 6
3, 7, 3, 5, 10
2, 2, 2, 1, 12
5, 9, 5, 2, 11
"""

input_list = [
    [1, 2, 3, 2, 5],
    [4, 1, 7, 2, 9],
    [13, 2, 3, 2, 5],
    [11, 1, 5, 1, 2],
    [3, 6, 10, 12, 11]
]

for x in range(len(input_list)):
    for y in range(len(input_list[x])):
        print(input_list[y][x], end=' ')
    print(end='\n')

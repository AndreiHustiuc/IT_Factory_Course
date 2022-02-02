"""
Write a program that prints the numbers from 1 to 100. 
But for multiples of three print Fizz instead of the number and for the multiples of five print Buzz. 
For numbers which are multiples of both three and five print FizzBuzz.
"""

num_list = [i for i in range(1, 101)]

for item in range(len(num_list)):
    if num_list[item] % 15 == 0:
        num_list[item] = 'FizzBuzz'
    elif num_list[item] % 3 == 0:
        num_list[item] = 'Fizz'
    elif num_list[item] % 5 == 0:
        num_list[item] = 'Buzz'

print(num_list)

"""
Write a function that will take a given string and reverse the order of the words. 
“Hello world” becomes “world Hello” and “May the Fourth be with you” becomes “you with be Fourth the May”
"""


def reverse_string(str):
    str_list = str.split(' ')
    result = str_list[::-1]
    x = ' '.join(result)
    return x


print(reverse_string("May the Fourth be with you"))
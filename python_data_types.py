# Write a Python program to calculate the length of a string.
string = 'Write a Python program'
print(len(string))

#Write a Python program to sum all the items in a list.
lst = [1,2,3,4,5,6,7]
print(sum(lst))

#Write a Python program to multiplies all the items in a list.
import math

lst = [1,2,3,4,5,6,7]
result = math.prod(lst)
print(result)

#Write a Python program to get the largest number from a list.
lst = [1,2,3,4,5,6,7]
print(max(lst))

#Write a Python program to get the smallest number from a list.
lst = [1,2,3,4,5,6,7]
print(min(lst))

#Write a Python program to count the number of characters in a string.
string = 'google.com'
result = {}

for i in range(len(string)):
    result.update({string[i]: string.count(string[i])})

print(result)

#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
sample_list = ['abc', 'xyz', 'aba', '1221']
result = 0
for item in sample_list:
    if len(item) >= 2 and item[0] == item[-1]:
        result += 1
        
print(result)


#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
def my_funct(item):
    return item[1]

sample_list.sort(key=my_funct)
print(sample_list)

#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead the empty string
sample_string = 'w3resource'

def slice_fun(word):
    if len(word) >= 2:
        result = word[:3] + word[-2:]
    else:
        result = ''
    
    return result


print(slice_fun(sample_string))
sample_string = 'w3'
print(slice_fun(sample_string))
sample_string = 'w'
print(slice_fun(sample_string))

#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
sample_string = 'restart'

for item in sample_string:
    if sample_string.count(item) >= 2:
        res = sample_string[::-1].replace(item, '$', 1)

print(res[::-1])

#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string
sample_string = 'abc', 'xyz'

print(sample_string[1][0:2]+sample_string[0][2:]+' '+sample_string[0][0:2]+sample_string[1][2:])


#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string is already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

sample_string = 'string'

if len(sample_string) < 3:
    print(sample_string)
elif sample_string[-3:] == 'ing':
    print(sample_string + 'ly')
else:
    print(sample_string + 'ing')


#Write a Python function that takes a list of words and returns the length of the longest one.
lst=["CRV", "Outback", "XC90", "GL", "Cherokee", "Escalade"]
length=list()

for item in lst:
    length.append(len(item))
    
print(max(length))

#Write a Python program to test whether an input is an integer.
#num = input('Enter a number: ')
#print(num == int())

#Write a Python program to sort (ascending and descending) a dictionary by value
dict = {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

sorted_dict = sorted(dict.values())
sorted_dict_rev = sorted(dict.values(), reverse=True)
print(sorted_dict)
print(sorted_dict_rev)

#Write a Python program to sort (ascending and descending) a dictionary by key value
dict = {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

sorted_dict = sorted(dict)
sorted_dict_rev = sorted(dict, reverse=True)
print(sorted_dict)
print(sorted_dict_rev)

#Write a Python program to add key to a dictionary.
sample_dictionary = {0:10, 1:20}

sample_dictionary.update({2: 30})
print(sample_dictionary)

#Write a Python program to concatenate following dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

new_dict = {**dic1, **dic2, **dic3}
print(new_dict)

#Write a Python program to check if a given key already exists in a dictionary.
dict = {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

def exist_in(dictionary, new_key):
    for key in dictionary.keys():
        if new_key == key:
            return True
        else:
            return False

print(exist_in(dict, 'g'))
        
#Write a Python program to iterate over dictionaries using for loops
dict = {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

for key, values in dict.items():
    print(key, values)
    
#Write a Python program to remove duplicates from a list.
lst=[55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99, 54, 101]
print(set(lst))
    
#Write a Python program to check a list is empty or not.
lst = [1]

def is_empty(list):
    if len(list) == 0:
        return True
    else:
        return False

print(is_empty(lst))

#Write a Python program to clone or copy a list.
lst=[55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99, 54, 101]
new_lst = lst
print(new_lst)

#Write a Python program to remove the nth index character from a non empty string.
sample_string = 'occurrences'
n_index = 3
res = sample_string.replace(sample_string[n_index], '')
print(res)

#Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
sample_string = 'dictionaries'
res = sample_string[-1] + sample_string[1:len(sample_string)-1] + sample_string[0]
print(res)

#Write a Python program to remove the characters which have odd index values of a given string.
sample_string = 'pseudopseudohipoparatiroidism'
res = ''

for i in range(len(sample_string)):
    if i % 2 != 0:
        continue
    res = res + sample_string[i]
    
print(res)

#Write a Python program to find the list of words that are longer than n from a given list of words.
sample_list = ["CRV", "Outback", "XC90", "GL", "Cherokee", "Escalade"]
longer_than_n = []
n = 5

for item in sample_list:
    if len(item) > n:
        longer_than_n.append(item)
        
print(longer_than_n)

#Write a Python program to count the occurrences of each word in a given sentence.
sample_string = 'Write a Python program to change a given string to a new string where the first and last chars have been exchanged'

new_list = sample_string.split(' ')
new_dict = {}

for item in new_list:
    new_dict.update({item: new_list.count(item)})

for key, value in new_dict.items():
    print(f'Thw word [{key}] is present {value} many times.')
    
#Write a Python function that takes two lists and returns True if they have at least one common member.
first_list = ['CRV', 'Outback', 'XC90', 'GL', 'Cherokee', 'Escalade']
second_list = ['Supra', 'Passat', 'IS300', 'Impreza']

def common_member(list_1, list_2):
    for i in list_1:
        for j in list_2:
            if i == j:
                print(True)
            
common_member(first_list, second_list)
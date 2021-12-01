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
    print(sample_string.count(item))
    



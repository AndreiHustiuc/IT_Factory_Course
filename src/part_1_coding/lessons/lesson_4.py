my_variable = 'dreptunghi'
print(my_variable[3])
# my_variable[3] = 'z'
# print(my_variable)
# string are unmutable

# LIST
lst = [1, 2, 3, 4, 5, 6, 7]
lst_string = ['yellow', 'red', 'blue', 'pink']
lst_all = ['green', 230, True, 23.567, [2354, False, 'string', [1, 2]]]

print(lst, lst_string, lst_all)
print(lst[-1])
print(lst_string[0].count('l'))
lst_string[2] = 'red'  # list are mutable
print(lst_string)
print(len(lst_string))
print(lst_string[len(lst_string) - 1])
lst_string.clear()
print(lst_string)
lst_string.append('morcov')
print(lst_string)
print(lst_all[-1][-1][1])

# TUPLES
lst = [1, 2, 3, 4, 5, 6, 7]
print(type(lst))
tup = tuple(lst)
print(tup)
print(type(tup))
print(tup[2])
print(4 in tup)
x, y, z, *other = (1, 2, 3, 4, 5, 6, 7, 8)
print(other)
tup = 2, 3, 4
print(type(tup))

# SETS
my_set = {1, 2, 3, 4, 5, 5, 3, 6}
second_set = {2, 4, 6, 8, 10, 15}
print(my_set)
my_set.add(7)
print(my_set)
print(f' Difference {my_set.difference(second_set)}')

# DICTIONARY
my_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
print(my_dict['c'])
print(my_dict.get('b'))
my_dict.update({'d': 4})
print(my_dict)
print(my_dict.items())

second_dict = dict(name='Andrei',
                   age=31)
print(second_dict)

third_dict = dict(a=1,
                  b=3,
                  c='apple',
                  test_response=dict(user=1,
                                     details=dict(adress='Calea Sagului',
                                                  other=[1, 2, 3])))

print(third_dict['test_response']['details']['other'][1])
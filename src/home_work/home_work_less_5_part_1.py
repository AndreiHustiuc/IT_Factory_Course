"""
Display the image below to the right hand side where the 0 going to be ' ' and 1 '*'  
"""

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

picture_1 = []

for item in picture:
    for i in range(len(item)):
        if item[i] == 0:
            print(' ', end='')
        elif item[i] == 1:
            print('*', end='')
    print(end='\n')

"""
Find a duplicat in a list using set, not using set
"""

my_list = ['a', 'b', 'c', 'b', 'd', 'a', 'm', 'n', 'n']
my_dict = {}

for item in my_list:
    my_dict.update({item: my_list.count(item)})

for key, value in my_dict.items():
    if value > 1:
        print(f'Item in the list that are duplicated: {key}')

my_list_2 = list(set(my_list))

"""
Using this function find the highest even number in the list
"""


def highest_even(lst):
    lst_1 = []
    for it in lst:
        if it % 2 == 0:
            lst_1.append(it)
    return max(lst_1)


print(highest_even([10, 2, 3, 4, 8, 11, 102]))

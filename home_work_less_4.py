# LIST
print('LIST')

my_list_1 = [236, 45.68, 'New York', 'Canada', True]
my_list_2 = ['red', 'yellow', 'green', 'black']

# .append()
print('.append()')
print(f'Before: {my_list_1}')
my_list_1.append(False)
print(f'After: {my_list_1}')
print('\n')

# .copy()
print('.copy()')
my_list_3 = my_list_2.copy()
print(f'My List 3 = {my_list_3} and My List 2 = {my_list_2}')
print('\n')

# .count()
print('.count()')
item = True
print(f'How many [{item}] are in My List 1: {my_list_1.count(item)}')
print('\n')

# .extend()
print('.extend()')
print(f'Before: {my_list_1}')
my_list_1.extend(my_list_2)
print(f'After: {my_list_1}')
print('\n')

# .index()
print('.index()')
item = 'green'
print(f'Index of item [{item}] is: {my_list_2.index(item)}')
print('\n')

# .insert()
print('.insert()')
print(f'Before: {my_list_2}')
my_list_2.insert(1, 'white')
print(f'After: {my_list_2}')
print('\n')

# .pop()
print('.pop()')
print(f'Before: {my_list_1}')
pop_item = my_list_1.pop()
print(f'After: {my_list_1}')
print(f'Item that was removed: {pop_item}')
print('\n')

# .reverse()
print('.reverse()')
print(f'Before: {my_list_2}')
my_list_2.reverse()
print(f'After: {my_list_2}')
print('\n')

# .sort()
print('.sort()')
print(f'Before: {my_list_2}')
my_list_2.sort()
print(f'After: {my_list_2}')
my_list_2.sort(reverse=True)
print(f'Reversed sort: {my_list_2}')
print('\n')

# .clear()
print('.clear()')
print(f'Before: {my_list_2}')
my_list_2.clear()
print(f'After: {my_list_2}')
print('\n')



# TUPLES
print('TUPLE')

my_tup = ('red', 'yellow', 'green', 'black', 'green')

# .count()
print('.count()')
item = 'green'
print(f'How many [{item}] are in My Tuple: {my_list_1.count(item)}')
print('\n')

# .index()
print('.index()')
item = 'yellow'
print(f'Index of item [{item}] is: {my_tup.index(item)}')
print('\n')

# SET
print('SET')

my_set = {'red', 'yellow', 'green', 'black', 'green'}
my_set_1 = {236, 45.68, 'New York', 'Canada', True, 'green'}

# .add()
print('.add()')
print(f'Before: {my_set}')
my_set.add('blue')
print(f'After: {my_set}')
print('\n')

# .copy()
print('.copy()')
my_set_2 = my_set_1.copy()
print(f'Set 2 = {my_set_2} is a copy of Set 1 = {my_set_1}')
print('\n')

# .difference()
print('.difference()')
print(f'Difference between my_set and my_set_1 is: {my_set.difference(my_set_1)}')
print('\n')

# .difference_update()
print('.difference_update()')
print(f'Before: {my_set}')
my_set.difference_update(my_set_1)
print(f'After: {my_set}')
print('\n')

# .discard()
print('.discard()')
print(f'Before: {my_set_1}')
item = 'Canada'
my_set_1.discard(item)
print(f'The item [{item}] was removed from Set: {my_set_1}')
print('\n')

# .intersection()
my_set = {'red', 'yellow', 'green', 'black', 'green'}
my_set_1 = {236, 45.68, 'New York', 'Canada', True, 'green'}
print('.intersection()')
my_set_3 = my_set.intersection(my_set_1)
print(f'Set 3: {my_set_3} is an intersection of Set: {my_set} with Set 1: {my_set_1}')
print('\n')

# .intersection_update()
my_set = {'red', 'yellow', 'green', 'black', 'green'}
my_set_1 = {236, 45.68, 'New York', 'Canada', True, 'green'}
print('.intersection_update()')
my_set.intersection_update(my_set_1)
print(f'Item that is present on both sets: {my_set}')
print('\n')

# .isdisjoint()
my_set = {'red', 'yellow', 'green', 'black', 'green'}
my_set_1 = {236, 45.68, 'New York', 'Canada', True, 'green'}
print('.isdisjoint()')
my_set_3 = my_set.isdisjoint(my_set_1)
print(f'Return [True] if no items in set {my_set} is present in set {my_set_1}: {my_set_3}')
print('\n')

# .issubset()
print('.issubset()')
my_set = {'red', 'yellow', 'green', 'black', 'green'}
my_set_1 = {236, 45.68, 'New York', 'Canada', True, 'green'}
my_set_2 = my_set.issubset(my_set_1)
print(f'Return [True] if all items in set {my_set} are present in set {my_set_1}: {my_set_2}')
print('\n')

# .issuperset()
print('.issuperset()')
my_set_2 = my_set.issuperset(my_set_1)
print(f'Return [True] if all items set {my_set_1} are present in set {my_set}: {my_set_2}')
print('\n')

# .pop()
print('.pop()')
my_set = {'red', 'yellow', 'green', 'black', 'green'}
print(f'Before: {my_set}')
pop_item = my_set.pop()
print(f'Remove a random item -> [{pop_item}] from the set: {my_set}')
print('\n')

# .remove()
print('.remove()')
my_set = {'red', 'yellow', 'green', 'black', 'green'}
print(f'Before: {my_set}')
item = 'green'
my_set.remove(item)
print(f'Remove "{item}" from the set: {my_set}')
print('\n')

# .symmetric_difference()
print('.symmetric_difference()')
my_set = {'red', 'yellow', 'green', 'black', 'green'}
my_set_1 = {236, 45.68, 'New York', 'Canada', True, 'green'}
print(f'Before: {my_set}, {my_set_1}')
my_set_2 = my_set.symmetric_difference(my_set_1)
print(f'Return a set that contains all items from both sets, except items that are present in both sets: {my_set_2}')
print('\n')

# .symmetric_difference_update()
print('.symmetric_difference_update()')
my_set = {'red', 'yellow', 'green', 'black', 'green'}
my_set_1 = {236, 45.68, 'New York', 'Canada', True, 'green'}
print(f'Before: {my_set}, {my_set_1}')
my_set.symmetric_difference_update(my_set_1)
print(f'Remove the items that are present in both sets, AND insert the items that is not present in both sets: {my_set}')
print('\n')

# .union()
print('.union()')
my_set = {'red', 'yellow', 'green', 'black', 'green'}
my_set_1 = {236, 45.68, 'New York', 'Canada', True, 'green'}
print(f'Before: {my_set}, {my_set_1}')
my_set_2 = my_set.union(my_set_1)
print(f'Return a set that contains all items from both sets, duplicates are excluded: {my_set_2}')
print('\n')

# .update()
print('.update()')
my_set = {'red', 'yellow', 'green', 'black', 'green'}
my_set_1 = {236, 45.68, 'New York', 'Canada', True, 'green'}
print(f'Insert the items from set {my_set_1} into set {my_set}: ', end='')
my_set.update(my_set_1)
print(my_set)
print('\n')

# .clear()
print('.clear()')
print(f'Before: {my_set}')
my_set.clear()
print(f'After: {my_set}')
print('\n')

# DICTIONARY
print('DICTIONARY')

# .copy()
print('.copy()')
my_dict = {'grass': 'green', 'sun': 'yellow', 'sky': 'blue', 'blood': 'red'}
my_dict_1 = my_dict.copy()
print(f'Copy the {my_dict} dictionary: {my_dict_1}')
print('\n')

# .fromkeys()
print('.fromkeys()')
keys = ('key1', 'key2', 'key3')
value = 0
this_dict = dict.fromkeys(keys, value)
print(f'Create a dictionary with 3 keys, all with the value 0: {this_dict}')
print('\n')

# .get()
print('.get()')
my_dict = {'grass': 'green', 'sun': 'yellow', 'sky': 'blue', 'blood': 'red'}
key = 'sun'
result = my_dict.get(key)
print(f'Get the value of the "{key}" item: {result}')
print('\n')

# .items()
print('items()')
my_dict = {'grass': 'green', 'sun': 'yellow', 'sky': 'blue', 'blood': 'red'}
print(f'Return the dictionary\'s key-value pairs: {my_dict.items()}')
print('\n')

# .keys()
print('.keys()')
my_dict = {'grass': 'green', 'sun': 'yellow', 'sky': 'blue', 'blood': 'red'}
print(f'Return the keys: {my_dict.keys()}')
print('\n')

# .pop()
print('.pop()')
my_dict = {'grass': 'green', 'sun': 'yellow', 'sky': 'blue', 'blood': 'red'}
key = 'sky'
my_dict.pop(key)
print(f'Remove "{key}" from the dictionary: {my_dict}')
print('\n')

# .popitem()
print('.popitem()')
my_dict = {'grass': 'green', 'sun': 'yellow', 'sky': 'blue', 'blood': 'red'}
print(f'Before: {my_dict}')
my_dict.popitem()
print(f'Remove the last item from the dictionary: {my_dict}')
print('\n')

# .setdefault()
print('.setdefault()')
my_dict = {'grass': 'green', 'sun': 'yellow', 'sky': 'blue', 'blood': 'red'}
print(f'Before: {my_dict}')
result = my_dict.setdefault('wall', 'white')
print(f'Returns the value of the specified key. If the key does not exist: insert the key, with the specified value: {my_dict}')
print('\n')

# .update()
print('.update()')
my_dict = {'grass': 'green', 'sun': 'yellow', 'sky': 'blue', 'blood': 'red'}
item = {'coffe': 'brown'}
my_dict.update(item)
print(f'Insert an item -> [{item}] to the dictionary: {my_dict}')
print('\n')

# .values()
print('.values()')
my_dict = {'grass': 'green', 'sun': 'yellow', 'sky': 'blue', 'blood': 'red'}
print(f'Return the values: {my_dict.values()}')
print('\n')

# .clear()
print('.clear()')
my_dict = {'grass': 'green', 'sun': 'yellow', 'sky': 'blue', 'blood': 'red'}
print(f'Before: {my_dict}')
my_dict.clear()
print(f'Remove all element from dictionary. After: {my_dict}')
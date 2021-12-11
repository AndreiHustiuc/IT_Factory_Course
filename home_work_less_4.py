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
# .isdisjoint()
# .issubset()
# .issuperset()
# .pop()
# .remove()
# .symmetric_difference()
# .symmetric_difference_update()
# .union()
# .update()


# .clear()
print('.clear()')
print(f'Before: {my_set}')
my_set.clear()
print(f'After: {my_set}')
print('\n')

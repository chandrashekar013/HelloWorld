# Dictionary and set

# Dictionary
dict_1 = {'animal': 'Tiger',
          'bird': 'peacock',
          'fruit': 'mango'}

print(dict_1)
print(dict_1['animal'])  # Tiger
print(dict_1.get('animal'))  # Tiger

# iterate
for element in dict_1:
    print(dict_1[element])

# change value
dict_1['fruit'] = 'orange'
print(dict_1)

# add new element
dict_1['veg'] = 'cabbage'
print(dict_1)

# Printout only keys n values
print(dict_1.keys())
print(dict_1.values())

# Key values into list
list_1 = list(dict_1.keys())
print(list_1)

# into tuple
tuple_1 = dict_1.items()
print(tuple_1)

# combine 2 dictionaries
dict_2 = {'color': 'red', 'size': 'XL'}
dict_2.update(dict_1)
print(dict_2)
print('hey', dict_1)

dict_3 = dict_2.copy()
print(dict_3)

# Set
set_1 = {'dog', 'cat', 'mouse', 'dog'}
print(set_1)  # will remove duplicates

# Add elements
set_1.add('cow')
print(set_1)

# combine 2 sets
tuple_2 = ('horse', 'cow', 'sheep', 'hen')
set_2 = set(tuple_2)
print(set_2)

# set operations
print(len(set_1))  # Applicable for all sequences
print(sorted(set_1))  # will return sorted list

print(set_1.union(set_2))

print(set_1.intersection(set_2))  # cow
print(set_1 & set_2)  # cow

print(set_1.difference(set_2))  # {'dog', 'cat', 'mouse'}
print(set_1 - set_2)  # {'dog', 'cat', 'mouse'}

set_1.difference_update(set_2)  # will effect the set
print(set_1)

print(set_1.symmetric_difference(set_2))

set_1.discard('mouse')
print(set_1)
set_1.discard('mouse')  # will remove only if present
# set_1.remove('mouse')  # will throw error if element not present

print(set_1.issubset(set_2))
print(set_1.issuperset(set_2))

set_3 = frozenset(set_1)
# set_3.add('lion') will not accept any new elements

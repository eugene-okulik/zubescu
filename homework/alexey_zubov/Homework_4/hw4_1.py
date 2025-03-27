import pprint

my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [1, 2, 'three', 4, 'five'],
    'dict': {'one': 1, 'two': 2, 'three': 3, 4: 'four', 5: 'five'},
    'set': {1, 2, 3, 4, 5}
}

# tuple
print(my_dict['tuple'][-1])

# list
my_dict['list'].append('six')
print(my_dict['list'])
del my_dict['list'][1]
print(my_dict['list'])

# dict
my_dict['dict'][('i am a tuple'),] = 'value'
print(my_dict['dict'])
del my_dict['dict'][5]
print(my_dict['dict'])

# set
my_dict['set'].add(100)
print(my_dict['set'])
my_dict['set'].remove(1)
print(my_dict['set'])

pprint.pprint(my_dict)

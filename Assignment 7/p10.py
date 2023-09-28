
my_dict = {'a': 100, 'b': 200, 'c': 300}

key_to_remove = 'b'
if key_to_remove in my_dict:
    del my_dict[key_to_remove]


print(my_dict)
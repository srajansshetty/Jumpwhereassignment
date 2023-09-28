
my_dict = {'a': 100, 'b': 200, 'c': 300}

product = 1
for value in my_dict.values():
    product *= value


print("The product of all items in the dictionary is:", product)
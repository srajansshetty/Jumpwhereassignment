
sample_dict = {'apple': 10, 'banana': 5, 'orange': 20, 'grapes': 15}


print("Example 1:")
for key, value in sample_dict.items():
    print(key, value)


print("Example 2:")
for key in sample_dict:
    print(key, sample_dict[key])


print("Example 3:")
for key, value in sample_dict.iteritems():
    print(key, value)


print("Example 4:")
for key in sample_dict.keys():
    print(key)

for value in sample_dict.values():
    print(value)
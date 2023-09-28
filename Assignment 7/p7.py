
dict1 = {1: 'a', 2: 'b'}
dict2 = {2: 'c', 4: 'd'}


merged_dict = dict1.copy()
merged_dict.update(dict2)
print(merged_dict)
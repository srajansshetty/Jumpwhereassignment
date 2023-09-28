my_dict = {'x': 500, 'y': 5874, 'z': 560, 'a': 500}
new_dict = {}
for key, value in my_dict.items():
    if value not in new_dict.values():
        new_dict[key] = value
print("Original Dictionary: ", my_dict)
print("Dictionary after removing duplicates: ", new_dict)
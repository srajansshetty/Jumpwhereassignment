my_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
new_list = []
for sublist in my_list:
    if sublist not in new_list:
        new_list.append(sublist)
print("Original List:", my_list)
print("New List:", new_list)
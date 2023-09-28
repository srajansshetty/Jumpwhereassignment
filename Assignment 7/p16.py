from heapq import nlargest

my_dict = {'A': 67, 'B': 23, 'C': 45, 'D': 56, 'E': 12, 'F': 69}
three_highest = nlargest(3, my_dict, key=my_dict.get)
print("Dictionary with 3 highest values:")
print("Keys: Values")
for key in three_highest:
    print(key, ":", my_dict[key])
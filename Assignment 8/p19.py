def find_substring(str1, sub_str):
    result = list(filter(lambda x: sub_str in x, str1))
    return result

colors = ['red', 'black', 'white', 'green', 'orange']
print("Original list:")
print(colors)

sub_str = "ack"
print("\nSubstring to search:")
print(sub_str)
print("Elements of the said list that contain specific substring:")
print(find_substring(colors, sub_str))

sub_str = "abc"
print("\nSubstring to search:")
print(sub_str)
print("Elements of the said list that contain specific substring:")
print(find_substring(colors, sub_str))
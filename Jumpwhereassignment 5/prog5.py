
string1 = input("enter the string1:")
string2 = input("enter the string2:")

swapped_string1 = string2[:2] + string1[2:]
swapped_string2 = string1[:2] + string2[2:]

result = swapped_string1 + ' ' + swapped_string2

print(f"Sample Strings: '{string1}', '{string2}' -> Result: {result}")
p

def replace_substring(input_string):
    not_index = input_string.find('not')  
    poor_index = input_string.find('poor')  
    if not_index != -1 and poor_index != -1 and not_index < poor_index:
        return input_string[:not_index] + 'good' + input_string[poor_index + 4:]  
    else:
        return input_string  
sample_string1 = input("enter the string1:")
sample_string2 = input("enter the string2:")

result1 = replace_substring(sample_string1)
result2 = replace_substring(sample_string2)

print(f"Sample String 1: '{sample_string1}' -> Result: '{result1}'")
print(f"Sample String 2: '{sample_string2}' -> Result: '{result2}'")

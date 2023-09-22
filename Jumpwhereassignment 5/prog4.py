
def replace_occurrences(input_string):
    if len(input_string) < 2:
        return input_string  
    else:
        first_char = input_string[0] 
        modified_string = first_char + input_string[1:].replace(first_char, '$')  
        return modified_string

sample_string = input("enter the string:")

result = replace_occurrences(sample_string)

print(f"Sample String: '{sample_string}' -> Result: '{result}'")

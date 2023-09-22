def remove_nth_character(input_string, n):
    if n < 0 or n >= len(input_string):
        return "Invalid index"  

    
    new_string = input_string[:n] + input_string[n + 1:]

    return new_string

original_string = input("enter the string:")
index_to_remove = 2  

result = remove_nth_character(original_string, index_to_remove)
print(f"Original String: '{original_string}'")
print(f"String after removing character at index {index_to_remove}: '{result}'")

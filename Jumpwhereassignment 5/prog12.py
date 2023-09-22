def convert(input_string):
    
    uppercase_count = sum(1 for char in input_string[:4] if char.isupper())
    
    if uppercase_count >= 2:
        return input_string.upper()  
    else:
        return input_string  

input_string = input("enter the string:")
result = convert(input_string)
print(result)

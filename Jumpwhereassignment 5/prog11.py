def reverse_string_if_multiple_of_4(input_string):
    length = len(input_string)
    
    if length % 4 == 0:
        reversed_string = input_string[::-1]  
        return reversed_string
    else:
        return input_string
input_string = input("enter the string:")
result = reverse_string_if_multiple_of_4(input_string)
print(result)


input_string = input("Enter a string: ")

result_string = ""
for char in input_string:
    if char != result_string[-1:] or not result_string:
        result_string += char

print("Result:"+result_string)

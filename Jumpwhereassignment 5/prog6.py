
def modify_string(input_string):
    if len(input_string) < 3:
        return input_string 
    elif input_string.endswith('ing'):
        return input_string + 'ly'  
    else:
        return input_string + 'ing' 


sample_string1 = input("enter the string1:")
sample_string2 =input("enter the string2:")


result1 = modify_string(sample_string1)
result2 = modify_string(sample_string2)

print(f"Sample String 1: {sample_string1}-> Result: {result1}")
print(f"Sample String 2: {sample_string2} -> Result: {result2}")

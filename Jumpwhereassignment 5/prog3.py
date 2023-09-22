
def get_new_string(input_string):
    if len(input_string) < 2:
        return ""  
    else:
        first_two = input_string[:2]  
        last_two = input_string[-2:]  
        return first_two + last_two  

sample_string1 = 'thisisniceone'
sample_string2 = 'ab'
sample_string3 = 'f'

result1 = get_new_string(sample_string1)
result2 = get_new_string(sample_string2)
result3 = get_new_string(sample_string3)

print(f"Sample String 1: '{sample_string1}' -> Result: '{result1}'")
print(f"Sample String 2: '{sample_string2}' -> Result: '{result2}'")
print(f"Sample String 3: '{sample_string3}' -> Result: '{result3}'")

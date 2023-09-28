sum_numbers = 0
count = 0

while True:
    num = int(input("Enter an integer (enter 0 to finish): "))
    
    if num == 0:
        break
    
    sum_numbers += num  
    count += 1  


if count == 0:
    average = 0
else:
    average = sum_numbers / count
print(f"Sum: {sum_numbers}")
print(f"Average: {average}")
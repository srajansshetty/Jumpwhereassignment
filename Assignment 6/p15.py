total = 0
count = 0
product = 1

while True:
    user_input = input("Enter an integer (or 'q' to quit): ")
    if user_input == 'q':
        break
    
    try:
        num = int(user_input)
        total += num  
        product *= num  
        count += 1  
    except ValueError:
        print("Invalid input. Please enter an integer or 'q' to quit.")

if count == 0:
    average = 0
else:
    average = total / count

print(f"Average: {average}")
print(f"Product: {product}")
total = 0
count = 0
for i in range(10):
    num = int(input(f"Enter integer {i + 1}: "))
    total += num
    count += 1

if count == 0:
    average = 0
else:
    average = total / count

print("Average:",average)
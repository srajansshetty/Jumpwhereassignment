numbers = [24, 50, 29]

start = 1
end = 10
for number in numbers:
    print(f"Multiplication table for {number}:")
    for i in range(start, end + 1):
        result = number * i
        print(f"{number} x {i} = {result}")
    print()  
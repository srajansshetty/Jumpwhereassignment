x = float(input("Enter the length of side x: "))
y = float(input("Enter the length of side y: "))
z = float(input("Enter the length of side z: "))

if x + y > z and x + z > y and y + z > x:
    
    if x == y == z:
        print("Equilateral triangle")
    
    elif x == y or x == z or y == z:
        print("Isosceles triangle")
    
    else:
        print("Scalene triangle")
else:
    print("Not a valid triangle")
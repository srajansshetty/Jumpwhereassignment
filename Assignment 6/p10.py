salary = float(input("Enter the employee's salary: "))
years_of_service = int(input("Enter the years of service: "))


bonus = 0

if years_of_service > 5:
    bonus = 0.05 * salary

print("Net bonus amount:",bonus)
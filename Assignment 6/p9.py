cost_per_unit = 100
quantity = int(input("Enter the quantity to purchase: "))
total_cost = quantity * cost_per_unit

if total_cost > 1000:
    discount = 0.10 * total_cost
    total_cost -= discount


print("Total cost:",total_cost)
matrix = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print("Original Matrix:", matrix)

result = sorted(matrix, key=lambda row: sum(row))
print("\nSort the said matrix in ascending order according to the sum of its rows", result)
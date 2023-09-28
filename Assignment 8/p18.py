check_string = lambda s: all([any(map(str.isupper, s)), any(map(str.islower, s)), any(map(str.isdigit, s)), len(s) >= 10])

# Example usage
input_string = "PaceWisd0m"
if check_string(input_string):
    print("valid string")
else:
    print("invalid string")
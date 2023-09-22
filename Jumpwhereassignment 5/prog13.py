
input_string = input("Enter a string: ")

specified_characters = input("Enter the specified characters: ")

if input_string.startswith(specified_characters):
    print(f"The string '{input_string}' starts with '{specified_characters}'.")
else:
    print(f"The string '{input_string}' does not start with '{specified_characters}'.")

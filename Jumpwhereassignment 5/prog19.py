
input_string = input("Enter a string: ")
words = input_string.split()
smallest_word = largest_word = words[0]

for word in words:
    if len(word) < len(smallest_word):
        smallest_word = word
    elif len(word) > len(largest_word):
        largest_word = word

print(f"Smallest word: {smallest_word}")
print(f"Largest word: {largest_word}")

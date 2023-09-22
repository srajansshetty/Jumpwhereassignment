
input_string = input("Enter a comma-separated sequence of words: ")
words_list = input_string.split(',')
words_list = [word.strip().lower() for word in words_list]

unique_words = list(set(words_list))

sorted_unique_words = sorted(unique_words)

result_string = ', '.join(sorted_unique_words)
print(f"Unique words in sorted form: {result_string}")

def find_longest_word_length(word_list):
    if not word_list:
        return 0  

    max_length = len(word_list[0])  

    for word in word_list:
        current_length = len(word)
        if current_length > max_length:
            max_length = current_length

    return max_length

words = ["apple", "banana", "cherry", "date", "elderberry"]
longest_length = find_longest_word_length(words)
print(f"The length of the longest word is: {longest_length}")

class StringReverser:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))

# Example usage
reverser = StringReverser()
result = reverser.reverse_words('hello .py')
print(result)  # Output: .py hello
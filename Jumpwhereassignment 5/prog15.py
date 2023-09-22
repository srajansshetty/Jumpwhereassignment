sample_string = 'thequickbrownfoxjumpsoverthelazydog'
char_count = {}
for char in sample_string:
    
    if char.isalpha():
        
        char = char.lower()
        char_count[char] = char_count.get(char, 0) + 1

for char, count in char_count.items():
    if count > 1:
        print(f"{char} {count}")

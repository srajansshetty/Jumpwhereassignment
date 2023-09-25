def is_balanced(delimiters):
    stack = []
    opening_delimiters = "([{"
    closing_delimiters = ")]}"
    delimiter_pairs = {"(": ")", "{": "}", "[": "]"}
    
    for delimiter in delimiters:
        if delimiter in opening_delimiters:
            stack.append(delimiter)
        elif delimiter in closing_delimiters:
            if not stack or delimiter_pairs[stack.pop()] != delimiter:
                return False
    
    return len(stack) == 0


input_string = "([{}])"
print(is_balanced(input_string)) 
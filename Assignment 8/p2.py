class ParenthesesValidator:
    def __init__(self, parentheses_string):
        self.parentheses_string = parentheses_string

    def is_valid(self):
        stack = []
        opening_brackets = "([{"
        closing_brackets = ")]}"
        bracket_pairs = {"(": ")", "{": "}", "[": "]"}
        
        for bracket in self.parentheses_string:
            if bracket in opening_brackets:
                stack.append(bracket)
            elif bracket in closing_brackets:
                if not stack or bracket_pairs[stack.pop()] != bracket:
                    return False
        
        return len(stack) == 0
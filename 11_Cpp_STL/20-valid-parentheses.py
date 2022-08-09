def is_valid(s):
    stack = []
    for char in s:
        if char == '{' or char == '[' or char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            else:
                top = stack[-1]
                if (char == '}' and top == '{') or \
                   (char == ']' and top == '[') or \
                   (char == ')' and top == '('):
                    stack.pop()
                else:
                    return False
    
    return not stack


# Test
print(is_valid("()"))
# Output: True
print(is_valid("()[]{}"))
# Output: True
print(is_valid("(]"))
# Output: False

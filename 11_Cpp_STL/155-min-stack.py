class MinStack:
    stack = []
    min_stack = []

    def __init__(self):

    def push(self, val):
        stack.append(val)
        if not min_stack or min_stack[-1] >= val:
            min_stack.append(val)

    def pop(self):
        if min_stack and min_stack[-1] == stack[-1]:
            min_stack.pop()

        return stack.pop()

    def top(self):
        return stack[-1]

    def getMin(self):
        return min_stack[-1]

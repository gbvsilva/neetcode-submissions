class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in '([{':
                stack.append(c)
            elif stack and bracket_map[c] == stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack) == 0


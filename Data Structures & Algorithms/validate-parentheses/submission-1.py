from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:

        # thoughts
        # - to use stack to track the valid opening and closing parentheses

        stack = deque()

        # special case
        if len(s) == 1:
            return False
        
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if not stack:   # early return for right side imbalance
                    return False
                # check if it matches the top most on stack
                top = stack.pop()
                if char == ')' and top != '(':
                    return False
                if char == '}' and top != '{':
                    return False
                if char == ']' and top != '[':
                    return False
        
        if stack: # still have something in stack
            return False
        
        return True
        
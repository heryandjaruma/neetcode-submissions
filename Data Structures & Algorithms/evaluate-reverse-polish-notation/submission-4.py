from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # thought
        # - We use stack to first keep the 2 values then check if it's an operand

        # return early if it's less than 2 tokens
        if len(tokens) <= 2:
            return int(tokens[0])
        stack = deque()
        for i, token in enumerate(tokens):
            if token not in ['+','-','*','/']:
                stack.append(token)
            else:
                secondTok = int(stack.pop())
                firstTok = int(stack.pop())

                res = None
                if token == '+':
                    res = firstTok + secondTok
                elif token == '-':
                    res = firstTok - secondTok
                elif token == '*':
                    res = firstTok * secondTok
                elif token == '/':
                    res = int(firstTok / secondTok)
                
                # check if it's not the last item
                if i == len(tokens) - 1:
                    return res
                stack.append(res)

# Time Complexity
# O(n) : only looping through number
# Space Complexity
# O(n) : as many as the num as well
from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) < 2:
            return int(tokens[0])
        stack = deque()

        for i, token in enumerate(tokens):
            if token not in ['+','-','*','/']:
                stack.append(token)
            else:
                secondToken = int(stack.pop())
                firstToken = int(stack.pop())
                result = None
                if token == '+':
                    result = firstToken + secondToken
                if token == '-':
                    result = firstToken - secondToken
                if token == '*':
                    result = firstToken * secondToken
                if token == '/':
                    result = int(firstToken / secondToken)
                
                if i == len(tokens) - 1:
                    return result
                stack.append(result)

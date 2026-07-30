from collections import deque

class MinStack:
    # thoughs
    # - use py internal stack
    # - use 2 stacks one for real and the other is for most minimum

    def __init__(self):
        self.deque = deque()
        self.minq = deque()

    def push(self, val: int) -> None:
        self.deque.append(val)
        val = min(val, self.minq[-1] if self.minq else val)
        self.minq.append(val)
        
    def pop(self) -> None:
        val = self.deque.pop()
        self.minq.pop()
        

    def top(self) -> int:
        return self.deque[-1]
        

    def getMin(self) -> int:
        return self.minq[-1]

# TODO:
# Learn this approach
# class MinStack:
#     def __init__(self):
#         self.min = float('inf')
#         self.stack = []

#     def push(self, val: int) -> None:
#         if not self.stack:
#             self.stack.append(0)
#             self.min = val
#         else:
#             self.stack.append(val - self.min)
#             if val < self.min:
#                 self.min = val

#     def pop(self) -> None:
#         if not self.stack:
#             return

#         pop = self.stack.pop()

#         if pop < 0:
#             self.min = self.min - pop

#     def top(self) -> int:
#         top = self.stack[-1]
#         if top > 0:
#             return top + self.min
#         else:
#             return self.min

#     def getMin(self) -> int:
#         return self.min
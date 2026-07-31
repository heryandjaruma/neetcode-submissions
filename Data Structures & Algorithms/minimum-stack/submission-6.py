# from collections import deque

# class MinStack:
#     # thoughts
#     # - use py internal stack
#     # - use 2 stacks one for real and the other is for most minimum

#     def __init__(self):
#         self.deque = deque()
#         self.minq = deque()

#     def push(self, val: int) -> None:
#         self.deque.append(val)
#         val = min(val, self.minq[-1] if self.minq else val)
#         self.minq.append(val)
        
#     def pop(self) -> None:
#         val = self.deque.pop()
#         self.minq.pop()
        

#     def top(self) -> int:
#         return self.deque[-1]
        

#     def getMin(self) -> int:
#         return self.minq[-1]

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

# NOTE
# The intuition of using the 1st approach is to also
# push the current minimum to stack no matter the new
# number is.

# Now the second approach is, more about "store difference"
# to each current minimum as the value. This way to actually
# calculate the real value you will always need the minimum
# by the time it's pushed.

from collections import deque

class MinStack:
    # thoughts
    # - use py internal stack
    # - use 2 stacks one for real and the other is for most minimum

    def __init__(self):
        self.stack = deque()
        self.min = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0) # 0 because the first one is always has practically 0 diff to the current top min
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:  # just do regular check if we found new min
                self.min = val
        
    def pop(self) -> None:
        popped = self.stack.pop()
        if popped < 0: # if negative it means the curr min will change
            self.min = self.min - popped


    def top(self) -> int:
        return self.stack[-1] + self.min

    def getMin(self) -> int:
        return self.min
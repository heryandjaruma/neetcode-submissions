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
        if not self.minq:
            self.minq.append(val)
        if self.minq and self.minq[-1] > val:
            self.minq.append(val)
        

    def pop(self) -> None:
        val = self.deque.pop()
        if self.minq[-1] == val:
            self.minq.pop()
        

    def top(self) -> int:
        return self.deque[1]
        

    def getMin(self) -> int:
        return self.minq[-1]

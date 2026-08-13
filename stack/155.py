# https://leetcode.com/problems/min-stack/ 

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)

        if not self.min_stack:
            self.min_stack.append(value)
        elif value > self.min_stack[-1]:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(value)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Testing
s = MinStack()

s.push(5)
s.push(2)
s.push(7)
s.push(1)

print("Stack:", s.stack)
print("Min Stack:", s.min_stack)
print("Top:", s.top())
print("Minimum:", s.getMin())

s.pop()

print("\nAfter pop:")
print("Stack:", s.stack)
print("Min Stack:", s.min_stack)
print("Top:", s.top())
print("Minimum:", s.getMin())
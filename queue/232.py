from typing import Optional


class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        return self.stack_out.pop()

    def peek(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out


# Testing
queue = MyQueue()

queue.push(10)
queue.push(20)
queue.push(30)

print("Peek:", queue.peek())
print("Pop:", queue.pop())
print("Peek:", queue.peek())

queue.push(40)

print("Pop:", queue.pop())
print("Pop:", queue.pop())
print("Pop:", queue.pop())

print("Is empty:", queue.empty())
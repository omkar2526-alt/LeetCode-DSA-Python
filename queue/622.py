class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.capacity = k
        self.front = 0
        self.rear = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.count == self.capacity:
            return False

        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.count += 1

        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False

        self.queue[self.front] = 0
        self.front = (self.front + 1) % self.capacity
        self.count -= 1

        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1

        return self.queue[self.front]

    def Rear(self) -> int:
        if self.count == 0:
            return -1

        index = (self.rear - 1 + self.capacity) % self.capacity
        return self.queue[index]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity


# Testing

q = MyCircularQueue(3)

print(q.enQueue(10))   # True
print(q.enQueue(20))   # True
print(q.enQueue(30))   # True

print(q.Rear())        # 30
print(q.isFull())      # True

print(q.deQueue())     # True

print(q.enQueue(40))   # True

print(q.Front())       # 20
print(q.Rear())        # 40
print(q.isEmpty())     # False
print(q.isFull())      # True
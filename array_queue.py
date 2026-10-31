# array_queue.py
# Circular queue on a fixed-size list.
# A size counter is used so "empty" and "full" are never confused.

class ArrayQueue:
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.front = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == len(self.data)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue overflow: cannot enqueue, the queue is full")
        rear = (self.front + self.size) % len(self.data)   # wraps around
        self.data[rear] = value
        self.size = self.size + 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue from an empty queue")
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)     # wraps around
        self.size = self.size - 1
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty: nothing to peek")
        return self.data[self.front]

    def __str__(self):
        # shows the raw array (so wrap-around is visible) plus the logical order
        raw = ["_" if x is None else str(x) for x in self.data]
        order = [str(self.data[(self.front + i) % len(self.data)])
                 for i in range(self.size)]
        return ("array: [" + ", ".join(raw) + "]  front index=" + str(self.front)
                + "  size=" + str(self.size)
                + "\n  order (front -> rear): " + (" ".join(order) if order else "empty"))

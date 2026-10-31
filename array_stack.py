# array_stack.py
# Stack built on a fixed-size Python list.
# top = -1 means the stack is empty.

class ArrayStack:
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.data) - 1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack overflow: cannot push, the stack is full")
        self.top = self.top + 1        # move top up first
        self.data[self.top] = value    # then store the value

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from an empty stack")
        value = self.data[self.top]    # read the value first
        self.data[self.top] = None     # clear the slot
        self.top = self.top - 1        # then move top down
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: nothing to peek")
        return self.data[self.top]

    def __str__(self):
        if self.is_empty():
            return "[ empty ]"
        items = self.data[:self.top + 1]
        return "bottom -> " + " ".join(str(x) for x in items) + " <- top"

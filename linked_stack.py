# linked_stack.py
# Stack built on a singly linked list.
# Push and pop both happen at the head, so both are O(1).

from node import Node


class LinkedStack:
    def __init__(self):
        self.top = None   # head of the list = top of the stack

    def is_empty(self):
        return self.top is None

    def is_full(self):
        # No fixed capacity, so it is never full.
        return False

    def push(self, value):
        node = Node(value)
        node.next = self.top   # new node points to the old top
        self.top = node        # new node becomes the top

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from an empty stack")
        value = self.top.value
        self.top = self.top.next   # move top down the chain
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: nothing to peek")
        return self.top.value

    def __str__(self):
        if self.is_empty():
            return "[ empty ]"
        items = []
        current = self.top
        while current is not None:
            items.append(str(current.value))
            current = current.next
        return "top -> " + " -> ".join(items) + " -> None"

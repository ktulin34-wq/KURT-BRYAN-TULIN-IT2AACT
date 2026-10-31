# node.py
# A single node of a singly linked list.
# Shared by LinkedStack and LinkedQueue.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

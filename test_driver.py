# test_driver.py
# Non-interactive demo of all four classes, including error handling
# and circular wrap-around.

from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


def try_it(label, action):
    try:
        result = action()
        print(label, "->", result)
    except (IndexError, OverflowError) as err:
        print(label, "-> ERROR:", err)


def test_stack(name, s, overflow_test):
    print("\n===", name, "===")
    for x in ["A", "B", "C"]:
        s.push(x)
    print("After push A, B, C:", s)
    try_it("peek()", s.peek)
    try_it("pop()", s.pop)
    print("State:", s)
    if overflow_test:
        while not s.is_full():
            s.push("X")
        print("Stack is now full:", s)
        try_it("push('Y') on full stack", lambda: s.push("Y"))
    while not s.is_empty():
        s.pop()
    try_it("pop() on empty stack", s.pop)
    try_it("peek() on empty stack", s.peek)


def test_queue(name, q, overflow_test):
    print("\n===", name, "===")
    for x in ["A", "B", "C"]:
        q.enqueue(x)
    print("After enqueue A, B, C:\n ", q)
    try_it("dequeue()", q.dequeue)
    try_it("dequeue()", q.dequeue)
    print("After two dequeues:\n ", q)
    for x in ["D", "E", "F"]:
        q.enqueue(x)       # for the array queue these wrap past the end
    print("After enqueue D, E, F:\n ", q)
    if overflow_test:
        try_it("enqueue('G') on full queue", lambda: q.enqueue("G"))
    while not q.is_empty():
        q.dequeue()
    try_it("dequeue() on empty queue", q.dequeue)
    try_it("peek_front() on empty queue", q.peek_front)


test_stack("ArrayStack (capacity 4)", ArrayStack(4), True)
test_stack("LinkedStack", LinkedStack(), False)
test_queue("ArrayQueue (capacity 4, circular)", ArrayQueue(4), True)
test_queue("LinkedQueue", LinkedQueue(), False)

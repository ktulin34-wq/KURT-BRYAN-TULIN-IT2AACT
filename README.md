# Stacks and Queues: Array vs. Linked List

Module 5 laboratory activity. This project builds a stack (LIFO) and a queue
(FIFO), each one twice: once with an array (Python list) and once with a
singly linked list. Everything is built from scratch, with no `insert(0, x)`,
`pop(0)` or `collections.deque`.

Requires Python 3 only. No extra libraries.

## Files

| File | What it does |
|------|--------------|
| `node.py` | `Node` class (`value`, `next`) shared by the linked structures |
| `array_stack.py` | `ArrayStack` with fixed capacity, `top` starts at `-1` |
| `linked_stack.py` | `LinkedStack`, push/pop at the head, no capacity limit |
| `array_queue.py` | `ArrayQueue`, circular, uses `front` + `size` and modulo |
| `linked_queue.py` | `LinkedQueue` with `front` (head) and `rear` (tail) |
| `main.py` | Menu-driven program, prints the state after each operation |
| `balanced_parentheses.py` | Stack application: checks `()[]{}` balance |
| `print_queue.py` | Queue application: print job simulation in FIFO order |
| `test_driver.py` | Demo of all four classes, errors and wrap-around |
| `sample_runs.md` | Captured outputs (underflow and overflow included) |
| `analysis.md` | Written answer to the analysis question |

## How to run

Put all files in the same folder, then:

```
python main.py                   # interactive menu (choose any implementation)
python test_driver.py            # automatic demo with error handling
python balanced_parentheses.py   # parentheses checker
python print_queue.py            # print queue simulation
```

In `main.py`, pick 1 to 4 for the implementation. The array versions ask for a
capacity first. Errors (underflow/overflow) are shown as messages instead of
crashing the program.

## Operations

- Stacks: `push`, `pop`, `peek`, `is_empty`, `is_full`
- Queues: `enqueue`, `dequeue`, `peek_front`, `is_empty`, `is_full`

All operations are O(1). Underflow raises `IndexError` and overflow raises
`OverflowError`, each with a descriptive message.

# Sample Runs

Captured output showing normal use, underflow, overflow and circular wrap-around.

## 1. Test driver (`python test_driver.py`)
```text

=== ArrayStack (capacity 4) ===
After push A, B, C: bottom -> A B C <- top
peek() -> C
pop() -> C
State: bottom -> A B <- top
Stack is now full: bottom -> A B X X <- top
push('Y') on full stack -> ERROR: Stack overflow: cannot push, the stack is full
pop() on empty stack -> ERROR: Stack underflow: cannot pop from an empty stack
peek() on empty stack -> ERROR: Stack is empty: nothing to peek

=== LinkedStack ===
After push A, B, C: top -> C -> B -> A -> None
peek() -> C
pop() -> C
State: top -> B -> A -> None
pop() on empty stack -> ERROR: Stack underflow: cannot pop from an empty stack
peek() on empty stack -> ERROR: Stack is empty: nothing to peek

=== ArrayQueue (capacity 4, circular) ===
After enqueue A, B, C:
  array: [A, B, C, _]  front index=0  size=3
  order (front -> rear): A B C
dequeue() -> A
dequeue() -> B
After two dequeues:
  array: [_, _, C, _]  front index=2  size=1
  order (front -> rear): C
After enqueue D, E, F:
  array: [E, F, C, D]  front index=2  size=4
  order (front -> rear): C D E F
enqueue('G') on full queue -> ERROR: Queue overflow: cannot enqueue, the queue is full
dequeue() on empty queue -> ERROR: Queue underflow: cannot dequeue from an empty queue
peek_front() on empty queue -> ERROR: Queue is empty: nothing to peek

=== LinkedQueue ===
After enqueue A, B, C:
  front -> A -> B -> C -> None  (rear = C)
dequeue() -> A
dequeue() -> B
After two dequeues:
  front -> C -> None  (rear = C)
After enqueue D, E, F:
  front -> C -> D -> E -> F -> None  (rear = F)
dequeue() on empty queue -> ERROR: Queue underflow: cannot dequeue from an empty queue
peek_front() on empty queue -> ERROR: Queue is empty: nothing to peek
```

## 2. Balanced parentheses (`python balanced_parentheses.py`)
```text
'()'       -> balanced
'([]{})'   -> balanced
'(]'       -> NOT balanced
'((())'    -> NOT balanced
'{[()]}'   -> balanced
''         -> balanced
'())'      -> NOT balanced
'{[}]'     -> NOT balanced

```

## 3. Print queue (`python print_queue.py`)
```text
Submitted job J101 (5 pages)
Submitted job J102 (12 pages)
Submitted job J103 (3 pages)
Submitted job J104 (8 pages)

--- Printing in FIFO order ---
#1 Printing job J101 - 5 pages | waited for 0 pages before it
#2 Printing job J102 - 12 pages | waited for 5 pages before it
#3 Printing job J103 - 3 pages | waited for 17 pages before it
#4 Printing job J104 - 8 pages | waited for 20 pages before it

All jobs done. Total pages printed: 28
```

## 4. Menu program (`python main.py`), Array Stack of capacity 2
```text

=== Choose an implementation ===
1. Array Stack
2. Linked Stack
3. Array Queue (circular)
4. Linked Queue
5. Exit
Choice: Enter capacity (positive integer): 
--- Stack menu ---
1. push  2. pop  3. peek  4. is_empty  5. is_full  6. back
Choice: Value to push: Pushed A
State: bottom -> A <- top

--- Stack menu ---
1. push  2. pop  3. peek  4. is_empty  5. is_full  6. back
Choice: Value to push: Pushed B
State: bottom -> A B <- top

--- Stack menu ---
1. push  2. pop  3. peek  4. is_empty  5. is_full  6. back
Choice: Value to push: Error: Stack overflow: cannot push, the stack is full
State: bottom -> A B <- top

--- Stack menu ---
1. push  2. pop  3. peek  4. is_empty  5. is_full  6. back
Choice: Popped B
State: bottom -> A <- top

--- Stack menu ---
1. push  2. pop  3. peek  4. is_empty  5. is_full  6. back
Choice: Popped A
State: [ empty ]

--- Stack menu ---
1. push  2. pop  3. peek  4. is_empty  5. is_full  6. back
Choice: Error: Stack underflow: cannot pop from an empty stack
State: [ empty ]

--- Stack menu ---
1. push  2. pop  3. peek  4. is_empty  5. is_full  6. back
Choice: Error: Stack underflow: cannot pop from an empty stack
State: [ empty ]

--- Stack menu ---
1. push  2. pop  3. peek  4. is_empty  5. is_full  6. back
Choice: 
=== Choose an implementation ===
1. Array Stack
2. Linked Stack
3. Array Queue (circular)
4. Linked Queue
5. Exit
Choice: Goodbye!
```

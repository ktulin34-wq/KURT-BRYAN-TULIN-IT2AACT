# Analysis

The linked-list stack pushes and pops at the head because the head is the only
end we can reach in constant time. A singly linked list only has `next`
pointers, so removing the tail would mean walking the whole list to find the
node before it, which makes `pop` O(n). Working at the head keeps both `push`
and `pop` at O(1). The array queue has to be circular because a plain array
either wastes the slots at the front after each dequeue or forces us to shift
every element left, which makes `dequeue` O(n). Using the modulo operator
lets `front` and the rear position wrap back to index 0, so freed slots get
reused and both operations stay O(1).

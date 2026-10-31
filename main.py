# main.py
# Menu-driven program: pick an implementation, then run any operation.
# The state of the structure is printed after every operation.

from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


def ask_capacity():
    while True:
        text = input("Enter capacity (positive integer): ").strip()
        if text.isdigit() and int(text) > 0:
            return int(text)
        print("Please enter a number greater than 0.")


def choose_structure():
    print("\n=== Choose an implementation ===")
    print("1. Array Stack")
    print("2. Linked Stack")
    print("3. Array Queue (circular)")
    print("4. Linked Queue")
    print("5. Exit")
    choice = input("Choice: ").strip()
    if choice == "1":
        return ArrayStack(ask_capacity()), "stack"
    if choice == "2":
        return LinkedStack(), "stack"
    if choice == "3":
        return ArrayQueue(ask_capacity()), "queue"
    if choice == "4":
        return LinkedQueue(), "queue"
    if choice == "5":
        return None, None
    print("Invalid choice.")
    return choose_structure()


def run_stack(s):
    while True:
        print("\n--- Stack menu ---")
        print("1. push  2. pop  3. peek  4. is_empty  5. is_full  6. back")
        choice = input("Choice: ").strip()
        try:
            if choice == "1":
                value = input("Value to push: ")
                s.push(value)
                print("Pushed", value)
            elif choice == "2":
                print("Popped", s.pop())
            elif choice == "3":
                print("Top is", s.peek())
            elif choice == "4":
                print("is_empty:", s.is_empty())
            elif choice == "5":
                print("is_full:", s.is_full())
            elif choice == "6":
                return
            else:
                print("Invalid choice.")
        except (IndexError, OverflowError) as err:
            print("Error:", err)
        print("State:", s)


def run_queue(q):
    while True:
        print("\n--- Queue menu ---")
        print("1. enqueue  2. dequeue  3. peek_front  4. is_empty  5. is_full  6. back")
        choice = input("Choice: ").strip()
        try:
            if choice == "1":
                value = input("Value to enqueue: ")
                q.enqueue(value)
                print("Enqueued", value)
            elif choice == "2":
                print("Dequeued", q.dequeue())
            elif choice == "3":
                print("Front is", q.peek_front())
            elif choice == "4":
                print("is_empty:", q.is_empty())
            elif choice == "5":
                print("is_full:", q.is_full())
            elif choice == "6":
                return
            else:
                print("Invalid choice.")
        except (IndexError, OverflowError) as err:
            print("Error:", err)
        print("State:", q)


def main():
    while True:
        structure, kind = choose_structure()
        if structure is None:
            print("Goodbye!")
            break
        if kind == "stack":
            run_stack(structure)
        else:
            run_queue(structure)


if __name__ == "__main__":
    main()

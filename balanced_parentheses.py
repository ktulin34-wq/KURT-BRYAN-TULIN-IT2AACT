# balanced_parentheses.py
# Application exercise 6a: check ()[]{} balance using a stack.

from linked_stack import LinkedStack

PAIRS = {")": "(", "]": "[", "}": "{"}


def is_balanced(text):
    stack = LinkedStack()
    for ch in text:
        if ch in "([{":
            stack.push(ch)
        elif ch in PAIRS:
            if stack.is_empty():
                return False                 # closing bracket with nothing open
            if stack.pop() != PAIRS[ch]:
                return False                 # wrong type of bracket
    return stack.is_empty()                  # leftovers mean unbalanced


if __name__ == "__main__":
    tests = ["()", "([]{})", "(]", "((())", "{[()]}", "", "())", "{[}]"]
    for t in tests:
        result = "balanced" if is_balanced(t) else "NOT balanced"
        print(repr(t).ljust(10), "->", result)

    while True:
        text = input("\nEnter a string (or 'q' to quit): ")
        if text == "q":
            break
        print("balanced" if is_balanced(text) else "NOT balanced")

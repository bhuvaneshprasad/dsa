# Stack Data Structure


class Stack:
    """
    1) A stack is a linear data structure that follows the principle of Last In First Out (LIFO). This means the last element inserted inside the stack is removed first.

    2) You can think of the stack data structure as the pile of plates on top of another.

    3) There are some basic operations that allow us to perform different actions on a stack.

    Basic Operations of Stack:
        Push: Add an element to the top of a stack
        Pop: Remove an element from the top of a stack
        IsEmpty: Check if the stack is empty
        IsFull: Check if the stack is full
        Peek: Get the value of the top element without removing it

    Time complexity: O(1)
    Space complexity: O(1)
    """

    def __init__(self):
        """Initialize an empty stack."""
        self.stack = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.stack.append(item)

    def pop(self):
        """
        Remove and return the item at the top of the stack.

        Returns:
        - item: The item at the top of the stack.

        Raises:
        - IndexError: If the stack is empty.
        """
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        """
        Return the item at the top of the stack without removing it.

        Returns:
        - item: The item at the top of the stack.

        Raises:
        - IndexError: If the stack is empty.
        """
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from empty stack")

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
        - bool: True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0

    def size(self):
        """
        Return the number of items in the stack.

        Returns:
        - int: The number of items in the stack.
        """
        return len(self.stack)


# Example usage:
stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)

print("Stack size:", stack.size())
print("Peek top element:", stack.peek())

print("Pop:", stack.pop())
print("Stack size:", stack.size())
print("Stack: ", stack.stack)

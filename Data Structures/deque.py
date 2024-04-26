class Deque:
    """
    A double-ended queue (deque) implementation in Python.

    Attributes:
    - queue: A list to store elements in the deque.
    """

    def __init__(self) -> None:
        """
        Initializes an empty deque.
        """
        self.queue = []

    def isEmpty(self) -> bool:
        """
        Checks if the deque is empty.

        Returns:
        - True if the deque is empty, False otherwise.
        """
        return len(self.queue) == 0

    def addRear(self, data) -> None:
        """
        Adds an element to the rear end of the deque.

        Args:
        - data: The element to be added.
        """
        self.queue.append(data)

    def addFront(self, data) -> None:
        """
        Adds an element to the front end of the deque.

        Args:
        - data: The element to be added.
        """
        self.queue.insert(0, data)

    def removeRear(self):
        """
        Removes and returns the element from the rear end of the deque.

        Returns:
        - The element removed from the rear end of the deque.
        """
        return self.queue.pop()

    def removeFront(self):
        """
        Removes and returns the element from the front end of the deque.

        Returns:
        - The element removed from the front end of the deque.
        """
        return self.queue.pop(0)

    def size(self) -> int:
        """
        Returns the size of the deque.

        Returns:
        - The number of elements in the deque.
        """
        return len(self.queue)


# Example Usage

d = Deque()
print(d.isEmpty())
d.addRear(8)
d.addRear(5)
d.addFront(7)
d.addFront(10)
print(d.size())
print(d.isEmpty())
d.addRear(11)
print(d.removeRear())
print(d.removeFront())
d.addFront(55)
d.addRear(45)
print(d.queue)
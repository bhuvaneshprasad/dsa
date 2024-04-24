class CircularQueue:
    """
    A circular queue is the extended version of a regular queue where the last element is connected to the first element. Thus forming a circle-like structure.
    """

    def __init__(self, capacity: int) -> None:
        """
        Initialize CircularQueue with a specified capacity.

        Args:
            capacity (int): The maximum capacity of the circular queue.
        """
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = self.tail = -1

    def isEmpty(self) -> bool:
        """
        Check if the circular queue is empty.

        Returns:
            bool: True if the circular queue is empty, False otherwise.
        """
        return self.head == -1 and self.tail == -1

    def isFull(self) -> bool:
        """
        Check if the circular queue is full.

        Returns:
            bool: True if the circular queue is full, False otherwise.
        """
        return (self.tail + 1) % self.capacity == self.head

    def enqueue(self, data) -> None:
        """
        Add an element to the circular queue.

        Args:
            data: The data to be added to the circular queue.
        """
        if self.isFull():
            print("The queue is full")
        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.capacity
            self.queue[self.tail] = data

    def dequeue(self) -> None:
        """
        Remove an element from the front of the circular queue.
        """
        if self.isEmpty():
            print("The queue is empty")
        elif self.head == self.tail:
            self.queue[self.head] = None
            self.head = self.tail = -1
        else:
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.capacity

    def printQueue(self) -> None:
        """
        Print the elements of the circular queue.
        """
        if self.isEmpty():
            print("The queue is Empty")
        else:
            print(self.queue)

    def peek(self):
        """
        Peek at the element at the front of the circular queue.

        Returns:
            The element at the front of the circular queue, or None if the queue is empty.
        """
        if self.isEmpty():
            print("The queue is Empty")
            return None
        return self.queue[self.head]

    def clear(self):
        """
        Clear the circular queue, removing all elements from it.
        """
        if self.isEmpty():
            print("The queue is Empty")
            return None
        self.queue = [None] * self.capacity


# Example Usage
circular_queue = CircularQueue(10)
print("is queue empty: ", circular_queue.isEmpty())
print("is queue full? ", circular_queue.isFull())
circular_queue.enqueue(1)
circular_queue.enqueue(2)
circular_queue.enqueue(3)
circular_queue.printQueue()
print("is queue full? ", circular_queue.isFull())
circular_queue.dequeue()
circular_queue.printQueue()
print("is queue full? ", circular_queue.isFull())
circular_queue.enqueue(4)
circular_queue.printQueue()

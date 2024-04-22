# Queue Data Structure

class Queue:
    """
    1)A queue is a useful data structure in programming. It is similar to the ticket queue outside a cinema hall, where the first person entering the queue is the first person who gets the ticket.

    2) Queue follows the First In First Out (FIFO) rule - the item that goes in first is the item that comes out first.

    3) In programming terms, putting items in the queue is called enqueue, and removing items from the queue is called dequeue.

    Basic Operations of Queue:
    A queue is an object (an abstract data structure - ADT) that allows the following operations:

        Enqueue: Add an element to the end of the queue
        Dequeue: Remove an element from the front of the queue
        IsEmpty: Check if the queue is empty
        IsFull: Check if the queue is full
        Peek: Get the value of the front of the queue without removing it

    Time complexity: O(1)
    Space complexity: O(n)
    """
    
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the item at the front of the queue.
        
        Returns:
        - item: The item at the front of the queue.
        
        Raises:
        - IndexError: If the queue is empty.
        """
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def peek(self):
        """
        Return the item at the front of the queue without removing it.
        
        Returns:
        - item: The item at the front of the queue, or None if the queue is empty.
        """
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
        - bool: True if the queue is empty, False otherwise.
        """
        return len(self.items) == 0

    def size(self):
        """
        Return the number of items in the queue.
        
        Returns:
        - int: The number of items in the queue.
        """
        return len(self.items)

    def __str__(self):
        """
        Return a string representation of the queue.
        
        Returns:
        - str: A string representation of the queue.
        """
        return str(self.items)


# Example usage:
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Queue:", q)
    print("Size:", q.size())
    print("Dequeue:", q.dequeue())
    print("Queue after dequeue:", q)
    print("Peek:", q.peek())

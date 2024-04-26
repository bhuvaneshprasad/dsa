class MinHeap:
    """
    A class representing a Min Heap data structure.
    """

    def __init__(self, size) -> None:
        """
        Initialize a MinHeap instance with a given size.

        Parameters:
            size (int): The initial size of the heap.
        """
        self.size = size
        self.heapArr = [None] * size
        self.count = 0
        self.original_size = size

    def getParentIndex(self, index):
        """
        Get the index of the parent node of the node at the given index.

        Parameters:
            index (int): The index of the node.

        Returns:
            int: The index of the parent node.
        """
        return (index - 1) // 2

    def getLeftChildIndex(self, index):
        """
        Get the index of the left child node of the node at the given index.

        Parameters:
            index (int): The index of the node.

        Returns:
            int: The index of the left child node.
        """
        return 2 * index + 1

    def getRightChildIndex(self, index):
        """
        Get the index of the right child node of the node at the given index.

        Parameters:
            index (int): The index of the node.

        Returns:
            int: The index of the right child node.
        """
        return 2 * index + 2

    def hasParent(self, index):
        """
        Check if the node at the given index has a parent node.

        Parameters:
            index (int): The index of the node.

        Returns:
            bool: True if the node has a parent, False otherwise.
        """
        return self.getParentIndex(index) >= 0

    def hasLeftChild(self, index):
        """
        Check if the node at the given index has a left child node.

        Parameters:
            index (int): The index of the node.

        Returns:
            bool: True if the node has a left child, False otherwise.
        """
        return self.getLeftChildIndex(index) < self.count

    def hasRightChild(self, index):
        """
        Check if the node at the given index has a right child node.

        Parameters:
            index (int): The index of the node.

        Returns:
            bool: True if the node has a right child, False otherwise.
        """
        return self.getRightChildIndex(index) < self.count

    def parent(self, index):
        """
        Get the value of the parent node of the node at the given index.

        Parameters:
            index (int): The index of the node.

        Returns:
            int: The value of the parent node.
        """
        return self.heapArr[self.getParentIndex(index)]

    def leftChild(self, index):
        """
        Get the value of the left child node of the node at the given index.

        Parameters:
            index (int): The index of the node.

        Returns:
            int: The value of the left child node.
        """
        return self.heapArr[self.getLeftChildIndex(index)]

    def rightChild(self, index):
        """
        Get the value of the right child node of the node at the given index.

        Parameters:
            index (int): The index of the node.

        Returns:
            int: The value of the right child node.
        """
        return self.heapArr[self.getRightChildIndex(index)]

    def isFull(self):
        """
        Check if the heap is full.

        Returns:
            bool: True if the heap is full, False otherwise.
        """
        return self.count == self.size

    def swap(self, index1, index2):
        """
        Swap the values of nodes at the given indices.

        Parameters:
            index1 (int): The index of the first node.
            index2 (int): The index of the second node.
        """
        temp = self.heapArr[index1]
        self.heapArr[index1] = self.heapArr[index2]
        self.heapArr[index2] = temp

    def heapifyUp(self, index):
        """
        Restore the heap property by moving the node at the given index upwards.

        Parameters:
            index (int): The index of the node.
        """
        if self.hasParent(index) and self.heapArr[index] < self.parent(index):
            self.swap(self.getParentIndex(index), index)
            self.heapifyUp(self.getParentIndex(index))

    def insert(self, data):
        """
        Insert a new element into the heap.

        Parameters:
            data (int): The value of the element to be inserted.
        """
        if self.isFull():
            raise MemoryError("Heap is Full")
        self.heapArr[self.count] = data
        self.count += 1
        self.heapifyUp(self.count - 1)

    def heapifyDown(self, index):
        """
        Restore the heap property by moving the node at the given index downwards.

        Parameters:
            index (int): The index of the node.
        """
        smallest = index
        if self.hasLeftChild(index) and self.heapArr[smallest] > self.leftChild(index):
            smallest = self.getLeftChildIndex(index)
        if self.hasRightChild(index) and self.heapArr[smallest] > self.rightChild(
            index
        ):
            smallest = self.getRightChildIndex(index)
        if smallest != index:
            self.swap(index, smallest)
            self.heapifyDown(smallest)

    def removeMin(self):
        """
        Remove and return the minimum element from the heap.

        Returns:
            int: The minimum element in the heap.
        """
        if self.count == 0:
            raise IndexError("Heap is empty")
        data = self.heapArr[0]
        self.heapArr[0] = self.heapArr[self.count - 1]
        self.heapArr[self.count - 1] = None
        self.count -= 1
        self.heapifyDown(0)
        return data

    def peek(self):
        """
        Return the minimum element in the heap without removing it.

        Returns:
            int: The minimum element in the heap.
        """
        return self.heapArr[0]

    def clear(self):
        """
        Clear the heap by resetting its size and count.
        """
        self.size = self.original_size
        self.heapArr = [0] * self.size
        self.count = 0


# Example Usage
heap = MinHeap(10)

heap.insert(5)
heap.insert(10)
heap.insert(3)
heap.insert(8)

min_element = heap.peek()
print("Minimum element in the heap:", min_element)

print(heap.heapArr)

removed_element = heap.removeMin()
print("Removed minimum element from the heap:", removed_element)

print(heap.heapArr)

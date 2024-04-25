class Node:
    """
    A class representing a node in a linked list.

    Attributes:
        data: The data stored in the node.
        next: A reference to the next node in the linked list.
    """

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    """
    A class representing a singly linked list.

    Attributes:
        header: A reference to the first node in the linked list.
        tail: A reference to the last node in the linked list.
        size: The number of nodes in the linked list.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the LinkedList class.
        """
        self.header = None
        self.tail = None
        self.size = 0

    def prepend(self, data):
        """
        Inserts a new node with the given data at the beginning of the linked list.

        Args:
            data: The data to be stored in the new node.
        """
        n = Node(data)
        if self.size == 0:
            self.header = n
            self.tail = n
        else:
            n.next = self.header
            self.header = n
        self.size += 1

    def append(self, data):
        """
        Inserts a new node with the given data at the end of the linked list.

        Args:
            data: The data to be stored in the new node.
        """
        n = Node(data)
        if self.size == 0:
            self.header = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n
        self.size += 1

    def printList(self):
        """
        Returns a string representation of the linked list.

        Returns:
            A string containing the data of each node in the linked list, separated by commas.
        """
        data = ""
        current = self.header
        while current != None:
            data = data + str(current.data) + ","
            current = current.next
        return data

    def removeFirst(self):
        """
        Removes and returns the data of the first node in the linked list.

        Returns:
            The data of the first node, or None if the list is empty.
        """
        if self.size == 0:
            return None
        data = self.header.data
        if self.size == 1:
            self.header = None
            self.tail = None
        else:
            self.header = self.header.next
        self.size -= 1
        return data

    def removeLast(self):
        """
        Removes and returns the data of the last node in the linked list.

        Returns:
            The data of the last node, or None if the list is empty.
        """
        if self.size == 0:
            return None
        data = self.tail.data
        if self.size == 1:
            self.header = None
            self.tail = None
        else:
            current = self.header
            while current.next.next != None:
                current = current.next
            current.next = None
            self.tail = current
        self.size -= 1
        return data

    def insertAt(self, pos, data):
        """
        Inserts a new node with the given data at the specified position in the linked list.

        Args:
            pos: The position at which to insert the new node.
            data: The data to be stored in the new node.

        Returns:
            None if the position is invalid, otherwise returns the data of the inserted node.
        """
        if pos < 0 or pos > self.size:
            return None
        elif pos == 0:
            self.prepend(data)
        elif pos == self.size:
            self.append(data)
        else:
            n = Node(data)
            prev = None
            current = self.header
            counter = 0
            while counter < pos:
                prev = current
                current = current.next
                counter += 1
            n.next = current
            prev.next = n
        self.size += 1

    def removeAt(self, pos):
        """
        Removes and returns the data of the node at the specified position in the linked list.

        Args:
            pos: The position of the node to remove.

        Returns:
            The data of the removed node, or None if the position is invalid.
        """
        if pos < 0 or pos >= self.size:
            return None
        elif pos == 0:
            return self.removeFirst()
        elif pos == self.size - 1:
            return self.removeLast()
        else:
            prev = None
            current = self.header
            counter = 0
            while counter < pos:
                prev = current
                current = current.next
                counter += 1
            prev.next = current.next
            self.size -= 1
            return current.data


# Example Usage
list = LinkedList()
list.append(2)
list.prepend(1)
list.append(4)
list.insertAt(2, 3)
list.removeFirst()
list.removeLast()
list.append(6)
list.removeAt(0)
print(list.printList())
print(list.size)

class Queue:
    """
    This class represents a queue using a double-linked list.

    Attributes:
        front: The front node of the queue.
        rear: The rear node of the queue.
        size: The number of elements in the queue.
    """

    class Node:
        """
        Created class Node that I will use later.

        Attributes:
            data: The data stored in the node.
            next: Reference to the next node.
            prev: Reference to the previous node.
        """

        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def printQueue(self):
        """
        Prints the elements of the queue, this method was made just for mine clarification.
        """
        current = self.front
        while current:
            print(current.data, end="")
            current = current.next
            if current is not None:
                print(", ", end="")
        print()

    def add(self, item):
        """
        Adds element to the end of the queue.
        """
        new_node = self.Node(item)
        if self.size == 0:
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def pop(self):
        """
        Removes and returns the item from the front of the queue.

        Raises:
            Exception: If the queue is empty.
        """
        if self.size == 0:
            raise Exception("Queue is empty, so you can't use pop")
        data = self.front.data
        if self.size == 1:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.size -= 1
        return data

    def count(self):
        """
        Returns the number of elements in the queue.
        """
        return self.size

    def clear(self):
        """
        Clears the queue, removing all elements.
        """
        self.front = self.rear = None
        self.size = 0

    def popAll(self):
        """
        Removes and returns all elements from the queue as a list.
        """
        items = []
        while self.size > 0:
            items.append(self.pop())
        return items

    def __len__(self):
        """
        Returns the number of elements in the stack.
        """
        return self.size

    def __getitem__(self, key):
        """
        Returns the item at the specified index in the stack.
        """
        if not (0 <= key < self.size):
            raise IndexError("Index out of range")

        current = self.front
        for _ in range(key):
            current = current.next
        return current.data

    def __setitem__(self, key, value):
        """
        Sets the item at the specified index in the stack to the given value.
        """
        if not (0 <= key < self.size):
            raise IndexError("Index out of range")

        current = self.front
        for _ in range(key):
            current = current.next
        current.data = value

    def __len__(self):
        """
        Returns the number of elements in the queue using len() function.
        """
        return self.count()

    def __getitem__(self, key):
        """
        Returns the element at the given index using the [] operator.
        """
        if not (0 <= key < self.size):
            raise IndexError("Index out of range")
        current = self.front
        for i in range(key):
            current = current.next
        return current.data

    def __setitem__(self, key, value):
        """
        Sets the element at the given index using the [] operator.
        """
        if not (0 <= key < self.size):
            raise IndexError("Index out of range")
        current = self.front
        for i in range(key):
            current = current.next
        current.data = value

queue = Queue()
queue.add(5)
queue.add(1)
queue.add(2)
queue.add(3)


print(len(queue))  # Should print the number of elements in the stack
print(queue[3])    # Should print the 4th element (3rd index)
queue[0] = "Pepa"  # Should set the 1st element to "Pepa"
queue.printQueue()

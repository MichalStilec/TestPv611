class Stack:
    """
    This class represents a stack using a double-linked list.

    Attributes:
        top: The top node of the stack.
        size: The number of elements in the stack.
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
        self.top = None
        self.size = 0

    def printStack(self):
        """
        Prints the elements of the stack.
        """
        current = self.top
        while current:
            print(current.data, end="")
            current = current.prev
            if current is not None:
                print(", ", end="")
        print()

    def push(self, item):
        """
        Pushes an element onto the stack.
        """
        new_node = self.Node(item)
        if self.size == 0:
            self.top = new_node
        else:
            new_node.prev = self.top
            self.top.next = new_node
            self.top = new_node
        self.size += 1

    def pop(self):
        """
        Pops and returns the item from the top of the stack.

        Raises:
            Exception: If the stack is empty.
        """
        if self.size == 0:
            raise Exception("Stack is empty, so you can't use pop")
        data = self.top.data
        if self.size == 1:
            self.top = None
        else:
            self.top = self.top.prev
        self.size -= 1
        return data

    def count(self):
        """
        Returns the number of elements in the stack.
        """
        return self.size

    def clear(self):
        """
        Clears the stack, removing all elements.
        """
        self.top = None
        self.size = 0

    def popAll(self):
        """
        Pops and returns all elements from the stack as a list.
        """
        items = []
        while self.size > 0:
            items.append(self.pop())
        return items

    def __iter__(self):
        self.current = self.top  # Initialize the current pointer when creating an iterator
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.prev  # Move to the previous node
        return data


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

for element in stack:
    print(element)
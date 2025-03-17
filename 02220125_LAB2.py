class Node:
    def __init__(self, data):
        self.data = data  # Data field to store the element
        self.next = None  # Next field to reference the next node


class LinkedList:
    def __init__(self):
        self.head = None  # Head reference to the first node
        self.tail = None  # Tail reference to the last node (optional)
        self.size = 0     # Size counter to track the number of elements
        print("Created new LinkedList")
        print(f"Current size: {self.size}")
        print(f"Head: {self.head}")

    def append(self, element):
        """Add an element to the end of the list."""
        new_node = Node(element)
        if self.head is None:  # If the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Link the new node to the last node
            self.tail = new_node        # Update the tail reference
        self.size += 1  # Increment the size counter
        print(f"Appended {element} to the list")

    def get(self, index):
        """Retrieve an element at a specific index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def set(self, index, element):
        """Replace an element at a specific index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = element
        print(f"Set element at index {index} to {element}")

    def get_size(self):
        """Return the current number of elements."""
        return self.size

    def prepend(self, element):
        """Add an element at the beginning of the list."""
        new_node = Node(element)
        if self.head is None:  # If the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head  # Link the new node to the current head
            self.head = new_node        # Update the head reference
        self.size += 1  # Increment the size counter
        print(f"Prepended {element} to the list")

    def __str__(self):
        """Return a string representation of the list."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return "[" + " ".join(map(str, elements)) + "]"


# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    
    linked_list.append(5)  # List: [5]
    print(f"Element at index 0: {linked_list.get(0)}")  # Output: Element at index 0: 5
    
    linked_list.set(0, 10)  # List: [10]
    print(f"Element at index 0: {linked_list.get(0)}")  # Output: Element at index 0: 10
    
    print(f"Current size: {linked_list.get_size()}")  # Output: Current size: 1
    linked_list.prepend(10)  # List: [10, 10]
    linked_list.append(5)     # List: [10, 10, 5]
    
    print(f"Print Linked list: {linked_list}")  # Output: Print Linked list: [10 10 5]
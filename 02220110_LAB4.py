#Part 1: Queue Implementation using Array: Sonam Tobgay
#Part 2: Queue implementation using Linked List: Chesung Dorji

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        print("Created new LinkedQueue")
    
    def is_empty(self):
        return self.size == 0
    
    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        print(f"Enqueued {element} to the queue")
        self.display()
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot dequeue.")
            return None
        removed_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        print(f"Dequeued element: {removed_data}")
        self.display()
        self.print_queue()
        return removed_data
    
    def peek(self):
        if self.is_empty():
            print("Queue is empty, no front element.")
            return None
        print(f"Front element: {self.front.data}")
        return self.front.data
    
    def display(self):
        if self.is_empty():
            print("Display queue: []")
            return
        current = self.front
        queue_elements = []
        while current:
            queue_elements.append(str(current.data))
            current = current.next
        print("Display queue:[" + ",".join(queue_elements) + "]")
    
    def get_size(self):
        print(f"Queue size: {self.size}")
        return self.size
    
    def print_queue(self):
        current = self.front
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Current queue: " + " -> ".join(elements) + " -> null")

# Example usage
queue = LinkedQueue()
print("Queue is empty:", queue.is_empty())
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.peek()
queue.dequeue()
queue.get_size()

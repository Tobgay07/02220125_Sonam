#Part 1: Queue Implementation using Array By Sonam Tobgay
#Part 2: Queue implementation using Linked List By Choesung Dorji


# Task 1: Implement the ArrayQueue Class Structure
class ArrayQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.size = 0
        print(f"Created new Queue with capacity: {capacity}")
        print(f"Queue is empty: {self.is_empty()}")

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity
    
 # Task 2: Implement Array-based Queue Operations
    def enqueue(self, element):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = element
        self.size += 1
        print(f"Enqueued {element} to the queue")
        self.display()

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        element = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        if self.is_empty():
            self.front = -1
            self.rear = -1
        print(f"Dequeued element: {element}")
        self.display()
        return element

    def peek(self):
        if self.is_empty():
            print("Queue is empty. Nothing to peek.")
            return None
        print(f"Front element: {self.queue[self.front]}")
        return self.queue[self.front]

    def get_size(self):
        print(f"Queue size: {self.size}")
        return self.size

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        elements = []
        index = self.front
        for _ in range(self.size):
            elements.append(self.queue[index])
            index = (index + 1) % self.capacity
        print(f"Display queue: {elements}")

# Example usage
queue = ArrayQueue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.peek()
queue.dequeue()
queue.get_size()

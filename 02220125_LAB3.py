
#Part 1: Stack Implementation using Array :Sonam Tobgay
#Part 2: Stack Implementation using Linked List: Chesung Dorji

#Part 1
# Task 1: Implement the ArrayStack Class Structure
class ArrayStack:
    def __init__(self, capacity=10):
        self._capacity = capacity  
        self._stack = [None] * capacity  
        self._top = -1  
        print(f"Created new ArrayStack with capacity: {capacity}")
        print("Stack is empty:", self.is_empty())  

    def is_empty(self):
        return self._top == -1
    
    # Task 2: Implement Array-based Stack Operations
    def push(self, element):
        if self._top + 1 == self._capacity:
            print("Stack is full! Cannot push element.")
            return
        self._top += 1
        self._stack[self._top] = element
        print(f"Pushed {element} to the stack")
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop element.")
            return None
        element = self._stack[self._top]
        self._stack[self._top] = None
        self._top -= 1
        print(f"Popped element: {element}")
        return element
    
    def peek(self):
        if self.is_empty():
            print("Stack is empty! No top element.")
            return None
        return self._stack[self._top]
    
    def size(self):
        return self._top + 1
    
    def display(self):
        print("Display stack:", [self._stack[i] for i in range(self._top + 1)])

# Example usage
stack = ArrayStack()
stack.push(10)
stack.display()
stack.push(20)
stack.display()
stack.push(30)
stack.display()
print("Top element:", stack.peek())
stack.pop()
print("Stack size:", stack.size())
stack.display()


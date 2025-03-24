  
#Part 1: Stack Implementation using Array :Sonam Tobgay
#Part 2: Stack Implementation using Linked List: Chesung Dorji

class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  


class LinkedStack:
    def __init__(self):
        self.top = None  
        self.size = 0    
        print("Created new LinkedStack")

    def push(self, element):
        new_node = Node(element)  
        new_node.next = self.top  
        self.top = new_node       
        self.size += 1             
        print(f"Pushed {element} to the stack")
        self.display()

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_node = self.top      
        self.top = self.top.next     
        self.size -= 1              
        print(f"Popped element: {popped_node.data}")
        self.display()
        return popped_node.data

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        print(f"Top element: {self.top.data}")
        return self.top.data

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size

    def display(self):
        current = self.top
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Display stack:", elements)

if __name__ == "__main__":
    stack = LinkedStack()
    print("Stack is empty:", stack.is_empty())
    
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    stack.peek()
    stack.pop()
    
    print("Current stack:", end=' ')
    stack.display()
    print("Stack size:", stack.size)
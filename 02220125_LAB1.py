class CustomList:
    def __init__(self, capacity=10):

        self._array = [None] * capacity  
        self.capacity = capacity  
        self.size = 0  
        print(f"Created new CustomList with capacity: {self.capacity}")
        print(f"Current size: {self.size}")

    def append(self, element):
        
        if self.size == self.capacity:
            self._resize()  
        
        self._array[self.size] = element
        self.size += 1
        print(f"Appended {element} to the list")

    def get(self, index):
        
        if 0 <= index < self.size:
            return self._array[index]
        else:
            raise IndexError("Index out of range")
    
    def set(self, index, element):
        
        if 0 <= index < self.size:
            self._array[index] = element
            print(f"Set element at index {index} to {element}")
        else:
            raise IndexError("Index out of range")

    def size(self):
       
        return self.size

    def _resize(self):
        
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self._array[i]  
        self._array = new_array
        print(f"Resized array to new capacity: {self.capacity}")
    
my_list = CustomList()  

my_list.append(5)  
print(f"Element at index 0: {my_list.get(0)}")  
my_list.set(0, 10)  
print(f"Element at index 0: {my_list.get(0)}")
print(f"Current size: {my_list.size}")  

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
##LINKED LIST IMPLEMENTATION
#ARRAY AS UNDERLYING STORAGE STRUCTURE
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []
#length of the array (dunder)
    def __len__(self):
        #loopin through the elements in the stack.
        return len(self.storage)

#add to the front of the array
    def push(self, value):
        self.size += 1
        self.storage.insert(0, value)
        
#pop the last item
    def pop(self):
        #check if empty
        if len(self.storage) == 0:
            return None
        #remove the first element in storage
        self.size -= 1
        node = self.storage.pop(0)
        return node

new_stack = Stack()
print(len(new_stack))
new_stack.push(2)
new_stack.push(3)
new_stack.push(5)
print(len(new_stack))
print(new_stack.storage)
print(f'Removed value is: {new_stack.pop()}')
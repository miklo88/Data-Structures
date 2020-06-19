
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
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []
#length of the array? 
    def __len__(self):
        #loopin through the elements in the stack.
        return len(self.storage)
        
#add to the end of the array
    def push(self, value):
        self.storage.append(value)
        
#pop the last item
    def pop(self):
        if len(self.storage)>0:
            return self.storage.pop()
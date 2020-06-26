from bst_linked_list import LinkedList
##LINKED LIST IMPLEMENTATION
'''
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
'''
#adding to the head of the stack. should look just like other array stack class.
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def push(self,value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        node = self.storage.remove_head()
        return node

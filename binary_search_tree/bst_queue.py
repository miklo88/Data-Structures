from bst_linked_list import LinkedList
'''
1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.

'''

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.insert(0, value)

    def dequeue(self):
        if len(self.storage) == 0:
            return None
        self.size -= 1
        #this is removing the LAST element in storage
        node = self.storage.pop(-1)
        return node
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
  
class LinkedList:
    def __init__(self):
        self.head = None # Stores a node, that corresponds to our first node in the list 
        self.tail = None # stores a node that is the end of the list
    
    # # return all the values in the list
    # def __str__(self):
    #     output = ''
    #     current_node = self.head
    #     #while current node HAS something
    #     while current_node is not None: #loop until its none
    #         output += f'{current_node.value} -> '
    #     #set current node to the next value or you'll be printing 0 over and over.
    #         current_node = current_node.next_node #update the tracker node to the next node.

    #     return output
    def add_to_head(self, value):
    # create a node to add
        new_node = Node(value)
    # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
      # new_node should point to current head
            new_node.next_node = self.head
      # move head to new node
            self.head = new_node

    def add_to_tail(self, value):
    # create a node to add
        new_node = Node(value)
    # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
      # point the node at the current tail, to the new node
            self.tail.next_node = new_node
            self.tail = new_node

  # remove the head and return its value
    def remove_head(self):
    # if list is empty, do nothing
        if not self.head:
            return None
    # if list only has one element, set head and tail to None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
    # otherwise we have more elements in the list
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value 

    def contains(self, value):
        if self.head is None:
            return False
    # Loop through each node, until we see the value, or we cannot go further
        current_node = self.head
        while current_node is not None:
      # check if this is the node we are looking for
            if current_node.value == value:
                return True
      # otherwise, go to the next node
            current_node = current_node.next_node
        return False

    def get_max(self):
        #if nothing, do nothing
        if not self.head:
            return None
        #if list only has one element, return that value
        if self.head.next_node is None:
            return self.head.value
        #loopin through the nodes comparing values its linked to
        current_node = self.head
        max_node = 0
        while current_node is not None:
            #if current node is bigger than the max node set max node to that value and carry on
            if current_node.value > max_node:
                max_node = current_node.value
            current_node = current_node.next_node
        return max_node
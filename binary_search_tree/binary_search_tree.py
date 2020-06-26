#importing stack from bst_stack.py
from bst_stack import Stack
from bst_queue import Queue
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
# recursion https://www.youtube.com/watch?v=8lhxIOAfDss
# def hanoi(n,f,h,t):
#     if n==0:
#         pass
#     else:
#         hanoi(n-1,f,t,h)
#         move(f,t)
#         hanoi(n-1,h,f,t)
# print(hanoi(4,"A","B","C"))

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    #another base case
    def insert(self, value):
        new_node = BSTNode(value)
#if empty
        if self.value is None:
            self.value = value
        # take the current value of our node (self.value)
        #compare to the new value we want to insert
        if value < self.value:
            #set the left to the new node with the new value if left is empty
            if self.left is None:
                self.left = new_node
            else:
                self.left.insert(value)
#set the right child to the new node with the new value
        if value >= self.value:
            if self.right is None:
                self.right = new_node
            else:
                self.right.insert(value)
    
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #if the target is equal to the base node or root node
        if self.value == target:
            return True
        #compar the target to the current value
        # if current value < target
        found = False
        if self.value >= target:
            #check the left subtree self.left.contains(target)
            if self.left is None:
                return False
            found = self.left.contains(target)
#if current value >= target
        if self.value < target:
        #check if right subtree contains target
        #if you cannot go right, return false
            if self.right is None:
                return False
            found = self.right.contains(target)
        return found
    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        
        max_val = self.right.get_max()
        
        return max_val

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        #calling fn on current node
        fn(self.value)
        #if a left node calling for each
        if self.left is not None:
            self.left.for_each(fn)
            #if a right node calling for each
        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self.left)
        print(self.value)
        if self.right:
            self.right.in_order_print(self.right)
        # print(self.value)
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    #bft uses a queue and queues up its children
    def bft_print(self, node):
        #create a queue for nodes
        # add the first node to the queue
        #utilizing a queue
        queue = Queue()
        #initializing queue with root node
        queue.enqueue(node)
        #while loopin to check size of the queue
        while queue.size > 0:
            current_node = queue.dequeue()
            print(current_node.value)
#get all the queue kids in the pool on the left
            if current_node.left is not None:
                queue.enqueue(current_node.left)
                #then on the right
            if current_node.right is not None:
                queue.enqueue(current_node.right)

        #while queue is not empty
            # remove the first node from the queue
            # print the removed node
            # add all the children into the queue
        

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    #first in last out FIFO data structure 
    #uses a stack and queues up its children up onto its stack.
    def dft_print(self, node):
        #create a stack for nodes
        stack = Stack()
        #add the fist node to the stack
        stack.push(node)
        #while the stack is not empty
        #get the current node form the top of th stack
        # print that node
        # then add all the children to the stack
        while len(stack) > 0:
            current_node = stack.pop()
            print(current_node.value)
            
            if current_node.left is not None:
                stack.push(current_node.left)

            if current_node.right is not None:
                stack.push(current_node.right)


    # # Stretch Goals -------------------------
    # # Note: Research may be required

    # # Print Pre-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass

# # const print_node = (x) => { console.log(x) }
# print_node = lambda x: print(f'current_node is : {x}')

# example_node = BSTNode(8)
# example_node.insert(3)
# example_node.insert(4)
# example_node.insert(2)
# example_node.insert(10)
# example_node.insert(9)
# example_node.insert(12)
# example_node.dft_print(example_node)
# example_node.bft_print(example_node)

# example_node.for_each(print_node)
# example_node.in_order_print(example_node)
# example_node.dft_print(example_node)


# # #you have to decide either or
# # root_node.bft_print(root_node)

# # #if you print like this then bft is NOT apart of the class.
# # # bft_print(root_node)
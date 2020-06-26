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
        # take the current value of our node (self.value)
        #compare to the new value we want to insert
        # if self.value is None:
        #     self.value = value
        if value < self.value:
            #set the left to the new node with the new value
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
#set the right child to the new node with the new value
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        #compar the target to the current value
        # if current value < target
        found = False
        if self.value > target:
            #check the left subtree self.left.contains(target)
            if self.left is None:
                return False
            found = self.left.contains(target)
#if current value >= target
        if self.value <= target:
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
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        #create a queue for nodes
        # add the first node to the queue
        #while queue is not empty
            # remove the first node from the queue
            # print the removed node
            # add all the children into the queue

        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        #create a stack for nodes
        #add the fist node to the stack
        #while the stack is not empty
        #get the current node form the top of th stack
        # print that node
        # add all the children to the stack
        pass

    # # Stretch Goals -------------------------
    # # Note: Research may be required

    # # Print Pre-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass

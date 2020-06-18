# Given an (array)list of integers, 1 ≤ a[i] ≤ n (n = size of list), some elements appear twice and others appear once.
# Find all the elements that appear twice in this list.
# Could you do it without extra space and in O(n) runtime?
donslist = [4,3,2,7,8,2,3,1,1,1]
# print(list(set([doubleItem for doubleItem in donslist if donslist.count(doubleItem)>1])))

for doubleItems in donslist:
    if donslist.count(list(set(doubleItems)))>1:
        continue
    elif len(doubleItems)>2:
        print(list(set(doubleItems)))
    # elif donslist.count(doubleItems)>2:
    #     continue
print(list(set(doubleItems)))
# 
# for i in range(6):
#     print(i, end=', ')
# 
# for i in range(6):
#     print(i)

#returns [2,3]
# Input:
# [4,3,2,7,8,2,3,1]
# Output:
# [2,3]

'''
Big O notation.
'''
# Structured way a computer scientist understands if an algo is efficent or not.
#what efficient really means
#when to appropriately apply datastructures to situations

#####VERY IMPORTANT
# Not how long some algorythm takes, the important part is how does the algorythm keep performing with more input that
# keeps getting put into it.

# if you see a loop, just look inside of it an analyze everything that is running inside of it.

#Data Structures
# - Access data: data.read()
# - Insertion arr.append(), dict['new_key1'] = val
# - Delete
# - Search

# Linked Lists- a bunch of values that are linked to each other

#home project
# implement a stack 
# and implement a queue.

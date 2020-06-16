# Given an (array)list of integers, 1 ≤ a[i] ≤ n (n = size of list), some elements appear twice and others appear once.
# Find all the elements that appear twice in this list.
# Could you do it without extra space and in O(n) runtime?
# donslist = [4,3,2,7,8,2,3,1,1,1]
# print(list(set([doubleItem for doubleItem in donslist if donslist.count(doubleItem)>1])))

# doubleItems = []
# for doubleItems in donslist:
#     if donslist.count(doubleItems)>1:
#         print(list(set(doubleItems)))
#     # elif donslist.count(doubleItems)>2:
#     #     continue
# for i in range(6):
#     print(i, end=', ')
for i in range(6):
    print(i)

#returns [2,3]
# Input:
# [4,3,2,7,8,2,3,1]
# Output:
# [2,3]
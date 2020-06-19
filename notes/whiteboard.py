# x = 'test'
# print(x)
'''
Print out all of the numbers in the following array that are divisible by 3:
[85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
The expected output for the above input is:
27
81
9
27
99
63
42
You may use whatever programming language you wish.
Verbalize your thought process as much as possible before writing any code. 
Run through the UPER problem solving framework while going through your thought process.
'''
#thoughts - no need to return an array or list. first sign for a loop
# divisible by 3 so i'll need the / operator 
# use python

#what i need to do. iterate through the list. declare a variable for my list that I can apply my logic to. 
x = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
#so check each item and see which items are divisible by three.
#only need to return what is divisible by three. new list of items. or new items. 
for y in x:
    if y%3==0:
    #return new variable for items divisible by three
        print(y)
    else:
        continue
# return x

# coding=utf-8
# put the above at the start of a file to use special characters in the comments
l = []

# check if a list is empty
if not l:
  print("List is empty")

# check if list is sorted
# for a list named l
all(l[j] <= l[j+1] for j in range(len(l)-1))

# check if all elements of a list is in another list
all(x in ['b', 'a', 'foo', 'bar'] for x in ['a', 'b'])

# select all elements of a list except the last one
# works aussi for differents indexes and values
mylist = [0, 1, 2, 3, 4, 5]
x = mylist[-1]
mylist[:x] + mylist[x+1:]
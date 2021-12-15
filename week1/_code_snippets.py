# coding=utf-8
# put the above at the start of a file to use special characters in the comments
l = []

# check if a list is empty
if not l:
  print("List is empty")

# check if list is sorted
# for a list named l
all(l[j] <= l[j+1] for j in range(len(l)-1))

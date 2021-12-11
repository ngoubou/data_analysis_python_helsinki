
l = []

# check if a list is empty
if not l:
  print("List is empty")

# check if list is sorted
# for a list named l
all(l[j] <= l[j+1] for j in range(len(l)-1))

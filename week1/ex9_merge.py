# test list
l = [1, 5, 9, 12, 2, 6, 10]

# the loop should continue as long as the list is unsorted
while(not all(l[j] <= l[j+1] for j in range(len(l)-1))): # found on stackoverflow
#while (l[0] != min(l)) or (l[-1] != max(l)): # should check here if list is sorted
    for i in range(0, 1 + len(l)):
    
        while i+1 < len(l):
            #print(i)
            temp = l[i]
            #if i+1 > len(l):
            #   break
            if l[i] > l[i+1]:
                l[i] = l[i+1]
                l[i+1] = temp
            i += 2
print(l)

# my code wasn't working cause the while condition was not correctly specified
# try to improve my code using the wiki article illustration of merge sort
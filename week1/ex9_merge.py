# 1e étape de l'algorithme marche, on compare 1 nombre sur deux au nombre adjacent
#i = 0
#l = [40, 2, 34, 3, 18, 7] # works only for this example
l = [1, 5, 9, 12, 2, 6, 10]
while (l[0] != min(l)) or (l[-1] != max(l)):
    for i in range(0, 1 + len(l)):
    
        #while i+1 < len(l):
            #print(i)
        temp = l[i]
        if i+1 > len(l):
            break

        if l[i] > l[i+1]:

            l[i] = l[i+1]
            l[i+1] = temp
        i += 2
print(l)

# the code works for a list of 6 elements (nope)
# but i'm getting close i feel it 

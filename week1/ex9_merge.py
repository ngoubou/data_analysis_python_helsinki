# 1e étape de l'algorithme marche, on compare 1 nombre sur deux au nombre adjacent
i = 0
#l = [40, 2, 34, 3, 18, 7] # works only for this example
l = [89,56,98,32]
#while (l[0] != min(l)) and (l[-1] != max(l)):
for i in range(len(l)):
    
    while (i+1 < len(l)) and (l[0] != min(l)):
        #print(i)
        temp = l[i]
        #if i+1 > len(l):
         #   break
        if l[i] > l[i+1]:
            l[i] = l[i+1]
            l[i+1] = temp
        i += 2
print(l)

# the code works for a list of 6 elements (nope)
# but i'm getting close i feel it 

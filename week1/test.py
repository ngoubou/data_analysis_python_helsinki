ls = [2, 4, 5, 6, 7, 8, 10, 12, 13]
ll = ls.copy()
del ll[0]

for j in ll:
    for i in ls:
        if j not in list(range(i,j)):
            print(i)
        #print(list(range(i,j)))
        #print(range(j,i))
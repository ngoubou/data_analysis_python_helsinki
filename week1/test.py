ls = [2, 4, 5, 6, 7, 8, 10, 12, 13]
ll = ls.copy()
del ll[0]

for j in ll:
    for i in range(len(ls)):
        # s'il y a un élément du résultat qui n'est pas dans la liste imprime i
        for k in list(range(i,j)):
            if k == ls[i]:
                print(k)
        #if j not in list(range(i,j)):
        #if (list(range(i,j))) and (j not in list(range(i,j))):
         #   print(i)
        #print(list(range(i,j)))
        #print(range(j,i))
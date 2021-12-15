ls = [2, 4, 5, 6, 7, 8, 10, 12, 13]
ll = ls.copy()
del ll[0]

for j in ll:
    for i in ls:
        # s'il y a un élément du résultat qui n'est pas dans la liste imprime i
        for k in list(range(i,j)):
            if k in ls: # dois vérifier ici que k est dans ls
                print(k)
            else:
                print(j)
        #if j not in list(range(i,j)):
        #if (list(range(i,j))) and (j not in list(range(i,j))):
         #   print(i)
        #print(list(range(i,j)))
        #print(range(j,i))

# je dois garder les deux loupes suivantes
# for j in ll:
    # for i in ls:
# peut être en modifier l'ordre
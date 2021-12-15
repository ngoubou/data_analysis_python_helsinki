# coding=utf-8

ls = [2, 4, 5, 6, 7, 8, 10, 12, 13]
ll = list(ls)
del ll[0]



# faire range des 2 1ers éléments et les mettre dans une liste
for i in range(len(ls)): 
    while i+1 < len(ls):
# for i in ls:
    #new_list =  list(range(i, i+1)) # donne un résultat différent
    
        new_list = list(range(ls[i], ls[i+1])) # attention au dernier élément de la liste



# vérifier si tous les éléments de cette liste sont dans LA LISTE:
#print(all(x in ls for x in new_list))
    # s'ils le sont tous, étendre le range à l'élément suivant.
        if all(x in ls for x in new_list):
            print(range(ls[i], ls[i+1]))

    # s'arrêter dès qu'il y a un élément non présent dans THE LIST
    # et print range(élément[0], élément[-1])
    # prends 2e nombre du range
    # si 2e nombre pas dans LISTE, alors dernier élément à imprimer

    # s'il y a un élément non présent dans LA LISTE:
        else:
            print(ls[i])
        i += 1
    
    # print le 1er nombre, et sors
    # update une variable ici
    # prends le 2e nombre avec qui tu étais et fais ce qui est au dessus
    #range(ls[1], ls[2])



# je dois garder les deux loupes suivantes
# for j in ll:
    # for i in ls:
# peut être en modifier l'ordre
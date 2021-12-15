# coding=utf-8

#L = [12, 8, 5, 6, 7, 4, 10, 2, 13]
L = [88, 89, 90, 92, 93, 94, 95, 96, 97]
ls = sorted(L)
ll = list(ls)
del ll[0]



# faire range des 2 1ers éléments et les mettre dans une liste
j = 0
for i in range(2): # je veux uniquement que i soit égal à 0 et 1. Pourquoi? Aucune idée
    #for j in range(len(ll)):
    
    ## PROBLÈME ICI
    new_list = list(range(ls[i], ll[j])) # attention au dernier élément de la liste
    #while i+1 < len(ls):
# for i in ls:
    #new_list =  list(range(i, i+1)) # donne un résultat différent
    
       
    # s'il y a un élément non présent dans LA LISTE:
    ## PROBLÈME ICI
    if not all(x in ls for x in new_list): # juste pour les 2 premiers éléments (rentre ici 1 seule fois)
        #print(ls[i])
        a = ls[i]
        j += 1
        #i += 1 si j loop uncomment
    else: # rentre ici une seule fois (?)
        a = ls[i]
        #j += 1    
    # peut-être update new_list ici

# vérifier si tous les éléments de cette liste sont dans LA LISTE:
#print(all(x in ls for x in new_list))
    # s'ils le sont tous, étendre le range à l'élément suivant.
    while all(x in ls for x in new_list): # ne pas revenir ici lorsqu'on est à l'avant dernier élément
        #print(range(ls[i], ll[j+1]))
        new_list = list(range(ls[i], ll[j+1])) # après ici revenir checker directement
        j += 1 

        # ne le faire qu'après être entré dans la while loop   
        ## PROBLÈME ICI
        if new_list[-1] not in ls:
            #print(new_list[0], new_list[-1]) 
            b = new_list[0]
            c = new_list[-1]
            #print(ll[j])
            d = ll[j]
            new_list = list(range(ll[j+1], ll[j+2]))  # pour le dernier élément
            # le + 1 et + 2 sont trop spécifiques à mon exemple
        # imprimer successivement les éléments désirés
        ## PROBLÈME ICI
        if (ll[j+2] == ls[-1]) and (ll[j+2] not in new_list): # ne faire que pour dernier élément
                #print(list([ll[j+1], ll[j+2] + 1]))
            e = ll[j+1]
            f = ll[j+2] + 1
                #print(f"The area is {c:6f}")
            print("[{},({},{}),{},({},{})]".format(a, b, c, d, e, f)) 
                # ne pas toujours print a tout seul
            break
            # si ll[j+2] pas présent dans new_list
            # alors print(list(ll[j+1], ll[j+2] + 1))
            # on arrête tout après ça
        
        #print(list(range(ll[j+1], ll[j+2])))
    
    # s'arrêter dès qu'il y a un élément non présent dans THE LIST
    # et print range(élément[0], élément[-1])
    # prends 2e nombre du range
    # si 2e nombre pas dans LISTE, alors dernier élément à imprimer

    
    # print le 1er nombre, et sors
    # update une variable ici
    # prends le 2e nombre avec qui tu étais et fais ce qui est au dessus
    #range(ls[1], ls[2])



# je dois garder les deux loupes suivantes
# for j in ll:
    # for i in ls:
# peut être en modifier l'ordre
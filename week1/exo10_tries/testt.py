# coding=utf-8

#ls = [88, 89, 90, 92, 93, 94, 95, 96, 97]
ls = sorted([2, 5, 4, 8, 12, 6, 7, 10, 13])
#j = 1
#for i in range(len(ls)):
   # new_list = list(range(ls[i], ls[j])) 

#new_list = [ls[0], ls[1]] # mettre le range ici
new_list = list(range(ls[0], ls[1]))
j = 1
i = 0
# y aura une loop ici pour revenir checker (doit commencer à 0)
while j + 1 < len(ls): # évidemment mettre autre condition comme i < len(ls) ou plutôt j
# 1e loop pour le cas où tous les éléments de new_list(range) sont dans ls
    while (all(x in ls for x in new_list)) and (ls[-1] != new_list[-1] + 1): #j + 1 < len(ls): 
        #i = 0 # ne doit pas être ici
        
        new_list = list(range(ls[i], ls[j+1]))
        #print(range(ls[i], ls[j]))
        j += 1 

        # CONSERVER CE CODE POUR DERNIER ÉLÉMENT
        if ls[-1] == new_list[-1] + 1:
            print(range(new_list[0], ls[-1] + 1)) # remplacer 0 par autre chose
        # une fois qu'il est rentré ici tout arrêter
            #break
            
    #print(new_list) # voir combien de fois et quand l'imprimer
    if (j + 1 < len(ls)) and (all(x in ls for x in new_list)): # ls[0] == new_list[0] ?
        print(range(new_list[0], new_list[-1]))
    else:
        print(new_list[0])
        new_list = list(range(ls[i+1], ls[j+1])) # exclure l'élément non présent et débuter avec chiffre suivant
# 2e loop pour l'autre cas
    i = j 
    while not all(x in ls for x in new_list):
        #del new_list[-1] ça ne change rien car le range va toujours inclure l'élément
        # qui n'est pas dans ls
        #print(range(ls[i], ls[j+1]))
        new_list = list(range(ls[i], ls[j])) # mettre juste j ici je pense
        # i should delete element not in the range and never include it again
        j += 1
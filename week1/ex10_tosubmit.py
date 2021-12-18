# coding=utf-8

#ls = [88, 89, 90, 92, 93, 94, 95, 96, 97]
#ls = sorted([2, 5, 4, 8, 12, 6, 7, 10, 13])
ls = [2, 4, 5, 6, 7, 8, 10, 12, 13]
#ls = [1, 2, 4]
#ls = [-2, 0, 1, 2, 3]
#ls = sorted([4, 2, 0, -2, -4])
#print(list(reversed(ls)))
new_list = list(range(ls[0], ls[1]))
j = 1
#for i in range(len(ls)):
print("[", end = "")
while j < len(ls): # mettre égalité pour ls3 et dans les 2 autres while loops
    #singleton = []
    #for j in range(1,len(ls)): # mettre while loop ici
   
    while (not all(x in ls for x in new_list)) and (j < len(ls)): #  mettre condition pour dernier élément
        if len(new_list) == 2:
            print(new_list[0], end = ",") # créer une liste pour toutes les valeurs
                #new_list = list(range(ls[i+1], ls[1]))
            #print()
            new_list = list(range(ls[j], ls[j+1])) # problème ici pour ls4 avec dernier élément#
            # mettre la même if condition que dans l'autre loop avant d'arriver là
            j += 1
        else: # PROBLÈME ICI pour ls3
            print("(" + str(new_list[0])+ "," + str(new_list[-1]) + ")", end = ",") # créer une liste pour toutes les valeurs
            new_list = list(range(ls[j-1], ls[j]))
        
    while (all(x in ls for x in new_list)) and (j < len(ls)): # mettre condition pour dernier élément
        new_list = list(range(new_list[0], ls[j]))
        j += 1
            # pour dernier élément
        if ls[-1] == new_list[-1] + 1: # PROBLÈME ICI pour ls3
            print("(" + str(new_list[0]) + "," + str(ls[-1] + 1), end = ")]") # créer une liste pour toutes les valeurs
                #print(range(new_list[0], ls[-1] + 1)) 

    #while all(x in ls for x in new_list):
        # 1+1
# return "[{},({},{}),{},({},{})]".format(a, b, c, d, e, f)

# TESTER SUR LES AUTRES LISTES DU FICHIER À CÔTÉ
# 
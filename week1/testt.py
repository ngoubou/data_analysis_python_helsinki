# coding=utf-8

ls = [88, 89, 90, 92, 93, 94, 95, 96, 97]

#j = 1
#for i in range(len(ls)):
   # new_list = list(range(ls[i], ls[j])) 

new_list = [ls[0], ls[1]]
j = 1
i = 0
# y aura une loop ici pour revenir checker (doit commencer à 0)
while True: # évidemment mettre autre condition comme i < len(ls)
# 1e loop pour le cas où tous les éléments de new_list(range) sont dans ls
    while (all(x in ls for x in new_list)) and j + 1 < len(ls): 
        #i = 0 # ne doit pas être ici
        print(range(ls[i], ls[j]))
        new_list = list(range(ls[i], ls[j+1]))
        j += 1 

        if ls[-1] == new_list[-1] + 1:
            print(range(new_list[0], ls[-1] + 1))
            
    #print(new_list) # ou range(new_list)
    print(range(new_list))

# 2e loop pour l'autre cas
    i = j
    while not all(x in ls for x in new_list):
    
        print(range(ls[i], ls[j+1]))
        new_list = list(range(ls[i], ls[j+1]))
        j += 1
# coding=utf-8
# write a function that detect ranges between numbers
# i think i've understood what is asked (after many hours)
# but don't know how to explain it in plain english

# Create a function named detect_ranges that gets a list of integers as a parameter. 
# The function should then sort this list, and transform the list into another list 
# where pairs are used for all the detected intervals. So 3,4,5,6 is replaced by the pair (3,7). 
# Numbers that are not part of any interval result just single numbers. 
# The resulting list consists of these numbers and pairs, separated by commas.

# what i have
l = [2,5,4,8,12,6,7,10,13]
# what i want
[2,(4,9),10,(12,14)]

# work with the sorted list
ls = [2, 4, 5, 6, 7, 8, 10, 12, 13]
ll = ls.copy()
del ll[0]

n = [10, 20, 30, 40]
m = [1, 20, 21, 30]
#print(type(m))

for j in ll:
    for i in ls:
        
        print(range(j,i))
#print([any(x in range(r) for r in m) for x in n])

for i in range(len(ls)):
    for j in range(1, len(ls)):
    # écrire une condition pour ne pas prendre dernier élément
    # car i + 1 out of range (while loop)
        if ls[i+1] not in range(ls[i], ls[i+1]): # normalement une boucle pour ça (while?) nope
            print(ls[i])
            # prends i+1
        if len(range(ls[j],ls[j+1])) == 1:
            k = j + 2
        #if (ls[j] and ls[k]) in range(ls[j], ls[k]):
            #continue
        print(list(range(ls[j], ls[k])))
        if list(range(ls[j], ls[k])) in ls:
            print('oui')
        # continue jusqu'à ce que le range print un chiffre pas dans ls
            #print(range(ls[j], ls[k]))
            # prends j + 2

            # range(ls[i+1], ls[i+1])
            # break
            # continue

        
    #if len(range(ls[i], ls[i+1])) == 2: 
     #   "oui"
    #print(range(ls[i], ls[i+1]))
    #print(i)



# prends 2 nombres adjacents (i et i + 1)
# calcule range(i, i+1)
# s'il y a 2 chiffres et le dernier chiffre de range(i, i + 1) n'est pas égal à i + 1
# prends i et mets le de côté dans une nouvelle liste

# s'il y a un seul chiffre fais range(i, i + 2)
# si le dernier chiffre est égal à i + 1 fais range(i, i + 3)

# recommence la boucle

# penser à écrire une seconde boucle


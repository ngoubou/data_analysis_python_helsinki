# write a function that detect ranges between numbers
# i think i've understood what is asked (after many hours)
# but don't know how to explain it in plain english

# what i have
l = [2,5,4,8,12,6,7,10,13]
# what i want
[2,(4,9),10,(12,14)]

# work with the sorted list
ls = [2, 4, 5, 6, 7, 8, 10, 12, 13]


for i in range(4,7):
    print(i)

# prends 2 nombres adjacents (i et i + 1)

# s'il y a 2 chiffres et le dernier chiffre de range(i, i + 1) n'est pas égal à i + 1
# prends i et mets le de côté dans une nouvelle liste

# s'il y a un seul chiffre fais range(i, i + 2)
# si le dernier chiffre est égal à i + 1 fais range(i, i + 3)

# recommence la boucle

# penser à écrire une seconde boucle
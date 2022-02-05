#!/usr/bin/env python3

def sum_equation(L):
    # L = [1, 5, 7]
    # 1 - écrire un programme qui additionne tous les éléments de la liste, convertir résultat en string"
    
    from functools import reduce   # import the reduce function from the functools module
    add = reduce(lambda x,y:x+y, L, 0)
    add = str(add)

    # 2 - convertir la liste en string (ou boxer mouhahahaha)
    #s1 = str([1,5,7]) # not correct
    # i want to convert each element of the list as a string, so i use the following method
    s1 = [str(x) for x in L]

    # 3 - ajouter signe "+" à la liste convertie et signe "="
    s2 = " + ".join(s1)

    # 4 - concatener liste au résultat de l'addition
    if len(L) > 0:
        a = s2 + " = " + add
    else: # handle empty lists
        a = "0 = 0"

    return a

def main():
    pass

if __name__ == "__main__":
    main()



## Course Solution ----

#def sum_equation(L):
    
    #if not L:

     #   return "0 = 0"

    #result = list(map(str, L))

    #return " + ".join(result) + f" = {sum(L)}"
#!/usr/bin/env python3

def sum_equation(L):
    return ""

def main():
    pass

if __name__ == "__main__":
    main()

# Write a function sum_equation which takes a list of positive integers as parameters and returns a string
# with an equation of the sum of the elements.

# Example: sum_equation([1,5,7]) returns "1 + 5 + 7 = 13" Observe, the spaces should be exactly as shown above.
# For an empty list the function should return the string "0 = 0".




#print(list(map(lambda x: x+x, s1)))

# 1 - écrire un programme qui additionne tous les éléments de la liste, convertir résultat en string"
s = [1,5,7]
from functools import reduce   # import the reduce function from the functools module
add = reduce(lambda x,y:x+y, s, 0)

add = str(add)

# 2 - convertir la liste en string (ou boxer mouhahahaha)
#s1 = str([1,5,7]) # not correct
# i want to convert each element of the list as a string, so i use the following method
s1 = [str(x) for x in s]


# 3 - ajouter signe "+" à la liste convertie et signe "="
s2 = " + ".join(s1)
print(s2)

print(s2 + " = " + add)

# 4 - concatener liste au résultat de l'addition


# print(str(s))
# print(" ".join(s))
#a = " + ".join(s1)
# print(len(a))
# print(a.strip("+"))
# print(a)

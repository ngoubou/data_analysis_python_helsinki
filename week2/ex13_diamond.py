#!/usr/bin/env python3

import numpy as np

def diamond(n):
    return np.array([])

def main():
    pass

if __name__ == "__main__":
    main()

## 1 - Create a identity matrix with shape(n,n) where n = diamond size length
n = 3 # we start with a length of 3 as in the example
mat_id = np.eye(2 * n - 1, dtype = int)

## 2 - Create a matrix of zeros with the same shape as above
shape = (2 * n - 1,) * 2
mat_ze = np.zeros(shape, dtype = int)
#print(mat_ze)

##  3 - Take the line of the zeros matrix and replace it in the identity matrix
# For how this is done, see my paper shit
s = 2 * n - 1
a = s//2

for j in range(5): 
    mat_ze[j] = mat_id[a]
    print(mat_ze)
    if j >= 2: # mouvements de remplissage en fonction des lignes (voir feuille papier)
        a += 1
    else:
        a -= 1
    
# Faire exactement la même loop mais dans l'autre sens (du bas vers la droite)
# Look how to incorporate concatenate
    
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

##  3 - Take the line of the identity matrix and replace it in the zeros matrix
# For how this is done, see my paper shit
s = 2 * n - 1 # the shape of the matrix
a = s//2 # to get the middle array of the identity matrix

for i in range(s): 
    mat_ze[i] = mat_id[a] # start with the middle array of he identity matrix
    #print(mat_ze)
    if i >= n - 1: # mouvements de remplissage en fonction des lignes (voir feuille papier)
        a += 1
    else:
        a -= 1
print(mat_ze)

for j in reversed(range(s)): # range(s-1, 0, -1) is an alternative
    # pour les modificatiosn j'aurai besoin des indices des "1" de mat_id
    # créer liste qui va les stocker
    # puis plutôt que remplacer la ligne, remplacer le chiffre
    # donc utiliser mat_ze[i,j] = mat_id[i,j]
    mat_ze[j] = mat_id[a]
1
# Faire exactement la même loop mais dans l'autre sens (du bas vers la droite)
# Look how to incorporate concatenate
    
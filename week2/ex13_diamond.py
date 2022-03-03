#!/usr/bin/env python3

import numpy as np

def diamond(n):
    return np.array([])

def main():
    pass

if __name__ == "__main__":
    main()

# Create a function diamond that returns a two dimensional integer array where 
# the 1s form a diamond shape. Rest of the numbers are 0. 
# The function should get a parameter that tells the length of a side of the diamond. 
# Do this using the eye and concatenate functions of NumPy and array slicing.

#a = np.eye(5, dtype = int)
#b = np.array([0, 1, 0, 0, 0])
#c = np.array([0, 0, 0, 1, 0])
#d = np.array([0, 0, 1, 0, 0])
#print(a)
#print(a.reshape(5,1))
#print(np.concatenate((b, c), axis = 0))
#print(5//2 + 5%2)
#i,j = a.shape
#print(a)
#print(i//2 + i%2)
#print(a[i//2]) # lui je l'utilise comme début et fin de la matrice finale
#for r in range(i):
    #print(i)
 #   print(a[r])
#print(a)
#print((4*2-5,)*2)
# Example of usage:

#for n in range(3,4): # the diamond l-side length goes from 1 to 10
    #print(np.eye(2 * n - 1, dtype = int))
  #  shape = (2 * n - 1,) * 2 # the matrice shape
    #print(shape)
# print(diamond(3))
# [[0 0 1 0 0]
# [0 1 0 1 0]
# [1 0 0 0 1]
# [0 1 0 1 0]
# [0 0 1 0 0]]
# print(diamond(1))
# [[1]]

## 1 - Create a identity matrix with shape(n,n) where n = diamond size length
n = 3 # we start with a length of 3 as in the example
mat_id = np.eye(2 * n - 1, dtype = int)

## 2 - Create a matrix of zeros with the same shape as above
shape = (2 * n - 1,) * 2
mat_ze = np.zeros(shape, dtype = int)
#print(mat_ze)

##  3 - Take the indexes of the ones in the identity matrix
#print(mat_id)
ls = [] # store the indexes of each ones, one per array
for i in mat_id:
    ls.append(np.where(i == 1)[0][0])
    #print(np.where(i == 1)[0][0])
#for i in mat_ze:
#print(mat_ze.shape)
s, ss = mat_ze.shape
a = s//2
for j in range(len(ls)): # j c'est l'indice et k la valeur
    # As with lists, modification through indexing is possible
        # m_z[1] m_i[3]
        #print(mat_id[0,k])
    
    mat_ze[j] = mat_id[a]
    print(mat_ze)
    
    if j >= 2:
        a += 1
    else:
        a -= 1
    
# Faire exactement la même loop mais dans l'autre sens
        #mat_ze[j,k] = mat_id[2,k] # doit le faire une foisà chaque itération de k et non 5 fois
    
    #print(a//2)
        #mat_ze[1,k] = mat_id[1,k]
        #print(mat_ze)
        #mat_ze[2,k] = mat_id[0,k]
        #print(mat_ze)
        #mat_ze[3,k] = mat_id[1,k]
        #print(mat_ze)
        #mat_ze[4,k] = mat_id[2,k]
        #print(mat_ze)
print(ls)
    
    #counter = 0
    #for j in i: # go through each array in the matrix
     #   if j == 1:
      #      counter += 1
       #     print(counter)
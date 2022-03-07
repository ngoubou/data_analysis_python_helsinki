#!/usr/bin/env python3

import numpy as np
from scipy.linalg import norm
from math import pi

def vector_angles(X, Y):

    np.array([])

def main():
    np.array([])

if __name__ == "__main__":
    main()

# print(np.cos(1))
a = np.array([[0,0,1], [-1,1,0]]) # compute the angle between these 2 vectors in degress
b = np.array([[0,1,0], [1,1,0]])
#print(a.shape, b.shape)
#x = np.random.randn(2,3)
#print("X1")
#print(x)
#print("X2")
#print(x)
#print("INNER PRODUCT")
#print(np.vdot(a,b))

#print(sum(a[:] * b[:]))
#print(np.inner(a,b))
#print(np.inner(x,x))
#print(np.vdot(np.array([-1,1,0]), np.array([0,1,0])))
## 1 - Compute the inner product between the vectors of X and Y
prod_in = np.inner(a, b)[0]
#print(prod_in)
## 2 - Compute the product of the l1 norms of X and Y
prod_norms = norm(a, 1) * norm(b, 1)
#print(prod_norms)
## 3 - Compute the arccos of the ratio between 1 et 2 and returns the dvalue in degree rather than radian

# NOT IN THE CORRECT FORMAT
#angle =  np.array([np.arccos(np.clip(prod_in / prod_norms, -1, 1)) * 180 / pi, np.arccos(np.clip(prod_in / prod_norms, -1, 1)) * 180 / pi]) # forces the input to be between -1 and 1 with np.clip
angle = np.arccos(np.clip(prod_in / prod_norms, -1, 1)) * 180 / pi
print(angle)
#print(angle.shape)

## ERROR FROM TMC
# # (shapes (2,), (10,) mismatch)
#x: array([68.566261, 68.566261])
#y: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

## TO DO ----
# revoir implémentation de np.inner

# Revisit if angle is in the right format
# my implementation outputs a scaler
# should it be a vector of different values ofjust the same values repeated multiple times
# the shape of input is (n,m) and angle should be (n,)
# il doit y avoir autant de valeurs qu'il y a de vecteurs dans les input array
# donc les calculs doivent être faits pour chaque vecteur

# le problème vient de l'étape 1; je devrais juste retourner le 1er array

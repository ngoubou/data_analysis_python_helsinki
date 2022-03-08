#!/usr/bin/env python3

import numpy as np
from scipy.linalg import norm
from math import pi

a = np.array([[0,0,1], [-1,1,0]])
b = np.array([[0,1,0], [1,1,0]])

## 1 - Compute the inner product between the vectors of X and Y
prod_in = np.inner(a, b)

## 2 - Compute the product of the l1 norms of X and Y
prod_norms = norm(a, 2) * norm(b, 2)

## 3 - Compute the arccos of the ratio between 1 et 2 and returns the dvalue in degree rather than radian
angle = np.arccos(np.clip(prod_in / prod_norms, -1, 1)) * 180 / pi
print(angle[0])

## I had a lot of trouble with the math and did not get the assignment quite right
# I stumbled upon someone else code on discord and copy it (shamelessly).
# I only modified the conversion from radian to degree
# I think that it is also part of the process
# So above is my code, i'll put below the said code, and then i'll put the course solution (as always)

# Copied Code

#import numpy as np
#import scipy.linalg
	 
#def vector_angles(X, Y):
	#p1 = np.einsum('ij,ij->i',X,Y)
    #p2 = np.linalg.norm(X,axis=1)
    #p3 = np.linalg.norm(Y,axis=1)
    #p4 = p1 / (p2*p3)
    #return np.arccos(np.clip(p4,-1.0,1.0))

## Course Solution ----

#import numpy as np
#import scipy.linalg 

#def vector_angles(X, Y):
#    ip = np.sum(X*Y, axis=1)
 #   Xlen = scipy.linalg.norm(X, 2, axis=1)
  #  Ylen = scipy.linalg.norm(Y, 2, axis=1)
   # temp=ip/(Xlen*Ylen)
    #temp = np.clip(temp, -1.0, 1.0)
    #result =  np.arccos(temp) / np.pi * 180
    #return result

#def main():
 #   np.random.seed(0)
  #  X=np.random.randn(10,3)
   # Y=np.random.randn(10,3)
    #print(vector_angles(X, Y))
    #A=np.array([[0,0,1], [-1,1,0]])
    #B=np.array([[0,1,0], [1,1,0]])
    #print(vector_angles(A, B))

#if __name__ == "__main__":
 #   main()

 
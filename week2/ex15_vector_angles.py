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
s = np.array([-1,1,0])
f = np.array([0,1,0])
#print(np.inner(s,f))

## 1 - Compute the inner product between the vectors of X and Y
prod_in = np.vdot(a, b)
#print(prod_in)
## 2 - Compute the product of the l1 norms of X and Y
prod_norms = norm(a, 1) * norm(b, 1)
#print(prod_norms)
## 4 - Compute the arccos of the ratio between 1 et 2 and returns the dvalue in degree rather than radian
angle =  np.arccos(np.clip(prod_in / prod_norms, -1, 1)) * 180 / pi # forces the input to be between -1 and 1 with np.clip
print(angle)

#print(np.arccos(0)*180/pi)
#np.arc
## 5 - Profit
# np.cos()
# dénominateur = 2 ie, scipy.linalg.norm(a, 1) * scipy.linalg.norm(b, 1)

# Let x and y be m-dimensional vectors. 
# The angle α between two vectors is defined by the equation cos⁡xy(α) = ..., 
# where the angle brackets denote the inner product, and ∣∣x∣∣ = ...

# Write function vector_angles that gets two arrays X and Y with same shape (n,m) as parameters. 
# Each row in the arrays corresponds to a vector. The function should return vector of shape (n,) 
# with the corresponding angles between vectors of X and Y in degrees, not in radians. 
# Again, don't use loops, but use vectorized operations.

# Note: function np.arccos is only defined on the domain [-1.0,1.0]. 
# If you try to compute np.arccos(1.000000001), it will fail.
# These kind of errors can occur due to use of finite precision in numerical computations. 
# Force the argument to be in the correct range (clip method).

#Test your solution in the main program.
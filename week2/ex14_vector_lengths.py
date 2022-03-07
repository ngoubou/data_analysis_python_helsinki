#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    return np.array([])

def main():
    pass

if __name__ == "__main__":
    main()

# Exercise 14 (vector lengths)

# Write function vector_lengths that gets a two dimensional array of shape (n,m) as a parameter. 
# Each row in this array corresponds to a vector. 
a = np.array([[2,5], [3,0], [4,6]]) # my input
b = np.array([1,2,3]) 
c = a.sum(axis = 1) 
d = a.sum(axis = 0) # my output
#d = np.sum(a)
#n, m = a.shape
#print(a)
#print(a.shape)
#print(len(a))
print(c)
print(c.shape)
#print(len(d))
#print(d.shape)

#print(a.T.sum(axis = 1))
#print(a.T.shape)
#print(a.T.sum(axis = 1).shape)
#print([2,5]+ [3,0]+ [4,6])
#print(f"n = ({n},)")
#print(np.sqrt(a).shape)

# What i'm actually trying to implement is a matrix norm:
## TO DO :
# EUCLIDIAN NORM YT (check mon historique aussi)
# Matrix norm YT MIT Strang

# Look up matrix norm definition
# Look up scipy.linalg.norm implementation

# The function should return an array of shape (n,), that has the length of each vector in the input. 
# The length is defined by the usual Euclidean norm. Don't use loops at all in your solution.
# Instead use vectorized operations. You must use at least the np.sum and the np.sqrt functions. 
# You can't use the function scipy.linalg.norm. Test your function in the main function.

# scipy.linalg.norm implementation
#from scipy.linalg import norm
#d = np.arange(9) - 4.0
#print(d.shape)
#e = d.reshape((3, 3))
#print(e.shape)
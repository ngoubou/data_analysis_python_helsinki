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
a = np.array([[1,2,5], [3,4,0], [9,4,6]])
b = np.array([7,5,1,8])
d = np.array([[7], [5], [4]])
c = np.array([[[7,5,1], [4,6,9], [4,6,7], [4,22,1]]])
print(a.shape)
print(d.shape)
#print(c.shape)
#print(np.shape(np.array([[1,2,2]])))
# Each row in this array corresponds to a vector. 
# The function should return an array of shape (n,), that has the length of each vector in the input. 
# The length is defined by the usual Euclidean norm. Don't use loops at all in your solution.
# Instead use vectorized operations. You must use at least the np.sum and the np.sqrt functions. 
# You can't use the function scipy.linalg.norm. Test your function in the main function.
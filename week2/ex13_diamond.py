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

a = np.eye(5, dtype = int)
for i in a:
    print(i)
#print(a)
#print((4*2-5,)*2)
# Example of usage:

for n in range(3,4): # the diamond l-side length goes from 1 to 10
    #print(np.eye(2 * n - 1, dtype = int))
    shape = (2 * n - 1,) * 2 # the matrice shape
    #print(shape)
# print(diamond(3))
# [[0 0 1 0 0]
# [0 1 0 1 0]
# [1 0 0 0 1]
# [0 1 0 1 0]
# [0 0 1 0 0]]
# print(diamond(1))
# [[1]]

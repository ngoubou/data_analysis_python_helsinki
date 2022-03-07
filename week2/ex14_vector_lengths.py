#!/usr/bin/env python3

import numpy as np
#from scipy.linalg import norm

def vector_lengths(a):
    return np.sqrt((a**2).sum(axis = 1))

def main():
    a = np.array([[2,5], [3,0], [4,6]])
    print(vector_lengths(a))
   
if __name__ == "__main__":
    main()

# We did the following things : 
# 1 - We take the array, we square each element in all vectors
# 2 - We sum all elements in each vector; each vector(array) then becomes a number
# 3 - We compute the square root of each number

# What we did is known as the Euclidian norm or l2 norm
# We used scipy.linalg.norm to assess our results

## Course Solution ----
# For the second time, my solution equals exactly the course one
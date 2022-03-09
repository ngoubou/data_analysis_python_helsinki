#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    return np.array([])

def main():
    pass

if __name__ == "__main__":
    main()

# Write function first_half_second_half that gets a two dimensional array of shape (n,2*m) as a parameter. 
# The input array has 2*m columns. The output from the function should be a matrix with those rows from 
# the input that have the sum of the first m elements larger than the sum of the last m elements 
# on the row. Your solution should call the np.sum function or the corresponding method exactly twice.

# Example of usage:

#a = np.array([[1, 3, 4, 2], [2, 2, 1, 2]])
#first_half_second_half(a)
#array([[2, 2, 1, 2]])

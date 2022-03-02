#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    result = []
    for rows in a:
        result.append(rows)
    return result

def get_columns(a):
    result = []
    for cols in a.T:
        result.append(cols)
    return result
    

def main():
    np.random.seed(0)
    a = np.random.randint(0,10, (4,4))
    #print(a.ndim)
    print("a:", a)
    #print("cols:", a[])
    #ls = []
    #for i in a.T :
        #ls.append(i)
     #   print(i)
    #print(ls)
    #b = np.array([[1,2,3], [4,5,6]])
    #print(b, type(b))
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()

# Write two functions, get_rows and get_columns, that get a two dimensional array as parameter. 
# They should return the list of rows and columns of the array, respectively. 
# The rows and columns should be one dimensional arrays. 
# You may use the transpose operation, which flips rows to columns, in your solution. 
# The transpose is done by the T method:
# a = np.random.randint(0, 10, (4,4))
# print(a)
# print(a.T)

# Test your solution in the main function. Example of usage:

# a = np.array([[5, 0, 3, 3], [7, 9, 3, 5], [2, 4, 7, 6], [8, 8, 1, 6]])
# get_rows(a)
# [array([5, 0, 3, 3]), array([7, 9, 3, 5]), array([2, 4, 7, 6]), array([8, 8, 1, 6])]
# get_columns(a)
# [array([5, 7, 2, 8]), array([0, 9, 4, 8]), array([3, 3, 7, 1]), array([3, 5, 6, 6])
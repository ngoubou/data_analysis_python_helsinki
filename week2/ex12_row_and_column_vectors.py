#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
    return []

def get_column_vectors(a):
    return []

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()

# Create function get_row_vectors that returns a list of rows from the input array of shape (n,m), 
# but this time the rows must have shape (1,m). Similarly, create function get_columns_vectors 
# that returns a list of columns (each having shape (n,1)) of the input matrix .

# Example: for a 2x3 input matrix

# [[5 0 3]
# [3 7 9]]

# the result should be

# Row vectors: 
# [array([[5, 0, 3]]), array([[3, 7, 9]])]
# Column vectors: 
# [array([[5],[3]]), array([[0],[7]]), array([[3],[9]])]

# The above output is basically just the returned lists printed with print. 
# Only some whitespace is adjusted to make it look nicer. Output is not tested.
#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
    result = []
    for rows in a:
        result.append(np.array([rows]))
    return result

def get_column_vectors(a):
    result = []
    #i, j = np.shape(a)
    for cols in a.T:
        # use a for loop instead
        i = 0
        result.append(np.concatenate(([[cols[i]]], [[cols[i+1]]], [[cols[i+2]]], [[cols[i+3]]])))
        #for i in np.array([cols]):
         #   result.append(np.array([i]))

        #result.append(np.array([cols]))
    return result

def main():
    np.random.seed(0)
    a = np.random.randint(0,10, (4,4))
    print("a:", a)
    #b = np.array([[5, 0, 3], [3, 7, 9]])
   # print("b:", b)
    #c = np.array([[50, 10, 33], [23, 17, 94]])
    #print(np.concatenate(([[1]], [[2]])))
    #print("b transposed:", b.T)
    #ls = []
    #print(np.shape(a))
    #i, j = np.shape(a)
    #z = np.shape(a)
    #print(z)
    #print(range(i))
    #print(i)
    #print(j)
    #for i in np.shape(a):
     #   print(i)
    #for i in b.T:
        #print(np.array([i])) # go from here
     #   k = 0
       # print(np.concatenate(([[i[k]]], [[i[k+1]]])))
        #print(np.concatenate(([[i[k]]], [[i[k+1]]])))
        #for k in range(len(i)):
         #   print(k)
        #print([i[k]])
        #print([i[k+1]]) 
        #print(i)

        #print(range(len(i)))
      #  for j in i:
            #print([j])
       #     ls.append([j])
            #print(j)
    #print(ls)
        #print(np.concatenate())
        #for j in np.array([i]):
         #   print(np.array([j]))
        #print(np.array([i]))
    #for i in a:
     #   print(np.array(i).reshape(2,2))
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
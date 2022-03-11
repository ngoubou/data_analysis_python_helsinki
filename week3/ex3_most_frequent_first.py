#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    return np.array([])

def main():
    pass

if __name__ == "__main__":
    main()

# Note: This exercise is fairly difficult. Feel free to skip if you get stuck.

# Write function most_frequent_first that gets a two dimensional array and an index c of a column as parameters. 
# The function should then return the array whose rows are sorted based on column c, in the following way. 
# Rows are ordered so that those rows with the most frequent element in column c come first, 
# then come the rows with the second most frequent element in column c, and so on. 
# Therefore, the values outside column c don't affect the ordering in any way.

# Example of usage:

# a:
# [[5 0 3 3 7 9 3 5 2 4]
# [7 6 8 8 1 6 7 7 8 1]
# [5 9 8 9 4 3 0 3 5 0]
# [2 3 8 1 3 3 3 7 0 1]
# [9 9 0 4 7 3 2 7 2 0]
# [0 4 5 5 6 8 4 1 4 9]
# [8 1 1 7 9 9 3 6 7 2]
# [0 3 5 9 4 4 6 4 4 3]
# [4 4 8 4 3 7 5 5 0 1]
# [5 9 3 0 5 0 1 2 4 2]]
# print(most_frequent_first(a, -1))
# [[4 4 8 4 3 7 5 5 0 1]
# [2 3 8 1 3 3 3 7 0 1]
# [7 6 8 8 1 6 7 7 8 1]
# [5 9 3 0 5 0 1 2 4 2]
# [8 1 1 7 9 9 3 6 7 2]
# [9 9 0 4 7 3 2 7 2 0]
# [5 9 8 9 4 3 0 3 5 0]
# [0 3 5 9 4 4 6 4 4 3]
# [0 4 5 5 6 8 4 1 4 9]
# [5 0 3 3 7 9 3 5 2 4]]

# If we look at the last column, we see that the number 1 appears three times, then both numbers 2 and 0 appear twice, 
# and lastly numbers 3, 9, and 4 appear only once. 
# Note that, for example, among those rows that contain in column c a number that appear twice in column c the order can be arbitrary.

# Hint: the function np.unique may be useful.
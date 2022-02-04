#!/usr/bin/env python3

def transform(s1, s2):
    return []

def main():
    pass

if __name__ == "__main__":
    main()


# Write a function transform that gets two strings as parameters and returns a list of integers. 
# The function should split the strings into words, and convert these words to integers.
# This should give two lists of integers. Then the function should return a list 
# whose elements are multiplication of two integers in the respective positions in the lists. 
# For example transform("1 5 3", "2 6 -1") should return the list of integers [2, 30, -3].

# You have to use split, map, and zip functions/methods. 
# You may assume that the two input strings are in correct format.

# 1 - split the strings into words, and convert these words to integers.
s1 = "12 43 64 6"
s2 = "21 34 46 9"
L1 = s1.split() 
L2 = s2.split()
print(L1, L2)
print(list(map(int, L1)), list(map(int, L2)))  

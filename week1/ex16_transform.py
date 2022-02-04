#!/usr/bin/env python3

def transform(s1, s2):
    # 1 - split the strings into words, and convert these words to integers.

    # split the strings into words
    L1 = s1.split() 
    L2 = s2.split()
    # convert these words to integers
    L1 = list(map(int, L1)) 
    L2 = list(map(int, L2)) 

    # 2 - return a list whose elements are multiplication of two integers in the respective positions in the lists

    L = list(zip(L1,L2))
    result = [(x * y) for x, y in L]
    
    return result

def main():
    pass

if __name__ == "__main__":
    main()

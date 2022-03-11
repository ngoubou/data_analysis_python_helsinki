#!/usr/bin/env python3

import pandas as pd

def create_series(L1, L2):
    s1 = pd.Series(L1, index = ["a", "b", "c"])
    s2 = pd.Series(L2, index = ["a", "b", "c"])
    return (s1, s2)
    
def modify_series(s1, s2):
    s1["d"] = s2["b"]
    del s2["b"]
    return (s1, s2)
    
def main():
    L1 = [1, 2, 3]
    L2 = [4, 5, 6]
    s1 = pd.Series(L1, index = ["a", "b", "c"])
    s2 = pd.Series(L2, index = ["a", "b", "c"])
    #print(create_series(L1, L2))
    print(modify_series(s1, s2))
    #return
    
if __name__ == "__main__":
    main()

L1 = [1, 2, 3]
L2 = [4, 5, 6]
s1 = pd.Series(L1, index = ["a", "b", "c"])
s2 = pd.Series(L2, index = ["a", "b", "c"])
s1["d"] = s2["b"]
del s2["b"]
#print(s1)
#print(s2)


# Test these functions from the main function. 
# Try adding together the Series returned by the modify_series function. 
# The operations on Series use the indices to keep the element-wise operations aligned. 
# If for some index the operation could not be performed, the resulting value will be NaN (Not A Number).
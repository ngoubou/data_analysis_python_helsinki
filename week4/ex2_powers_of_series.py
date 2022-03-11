#!/usr/bin/env python3

import pandas as pd
import numpy as np

def powers_of_series(s, k):
    return None
    
def main():
    return
    
if __name__ == "__main__":
    main()

# Make function powers_of_series that takes a Series and a positive integer k as parameters and returns a DataFrame. 
# The resulting DataFrame should have the same index as the input Series. 
# The first column of the dataFrame should be the input Series, the second column should contain the Series raised to power of two. 
# The third column should contain the Series raised to the power of three, and so on until (and including) power of k. 
# The columns should have indices from 1 to k.

# The values should be numbers, but the index can have any type. Test your function from the main function. 
# Example of usage:

ind = list("abcd")
s = pd.Series([1,2,3,4], index = ind)
s2 = s**2
s3 = s**3
#print(s3.values)
columns = []
for i in s:
    columns.append(i)
#print(np.array(columns))
#df = pd.DataFrame(s, index = ind)
#print(df)
#print(powers_of_series(s, 3))
k = 3
d = {}
for i in range(1, k + 1):
    #print(i)
    d.update({i: s.values**i})
print(d)
df = pd.DataFrame(d, index = ind)
print(df)
# Should print:

#    1   2   3
# a  1   1   1
# b  2   4   8
# c  3   9  27
# d  4  16  64

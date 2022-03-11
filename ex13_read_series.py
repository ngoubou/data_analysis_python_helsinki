#!/usr/bin/env python3

import pandas as pd    # This is the standard way of importing the Pandas library
import numpy as np
import re
def read_series():
    return pd.Series()

def main():
    pass

if __name__ == "__main__":
    main()

# Write function read_series that reads input lines from the user and return a Series. 
# Each line should contain first the index and then the corresponding value, separated by whitespace. 
# The index and values are strings (in this case dtype is object). An empty line signals the end of Series. 
# Malformed input should cause an exception. 
# An input line is malformed, if it is non-empty and, when split at whitespace, does not result in two parts.

# Test your function from the main function.
input = "a Lionel"#\n1 Ralph\n2 Me\n"
input1 = "b Ralph"
input2 = "c Me"
a = [input, input1, input2]
ind = [] # the series indexes
val = []
for i in a:
    ind.append(re.findall(r'^(.*?)\s', i)[0]) # don't convert it to int cause they can be characters too
    val.append(re.findall(r'\s(.*?)$', i)[0]) # everything after the space

result = pd.Series(val, index = ind)
#pd.Se

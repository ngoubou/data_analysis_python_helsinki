#!/usr/bin/env python3

import contextlib
import pandas as pd
import numpy as np
import re

def read_series():
    contents = []
    ind = []
    val = []

    while True: 
        line = input()
        contents.append(line)
        if line: # As long as the input is not empty, continue prompting the user
            continue
        else:
            break

    for i in contents: 
        if i and len(i.split()) != 2: # if the input does not have two parts separated by a space
            raise Exception("The line is malformed")
        with contextlib.suppress(IndexError):
            ind.append(i.split()[0])
            val.append(i.split()[-1])
    return pd.Series(val, index = ind)

def main():
    print(read_series())

if __name__ == "__main__":
    main()

## Course Solution ----
# My code is very similar to the course solution, but i'll paste it nonetheless

#def read_series():    
#    values=[]
#    indices=[]
#    while True:
#        line = input("")
#        if not line:
#            break
#        i, v = line.split()
#        values.append(v)
#        indices.append(i)
#    s = pd.Series(values, index=indices)
#    return s
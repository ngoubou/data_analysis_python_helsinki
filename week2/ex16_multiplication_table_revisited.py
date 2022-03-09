#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    return np.arange(n) * np.arange(n).reshape((n,1))

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()

## Course Solution ---- 
# 2nd time i think my solution is better (i should actually time both functions and see the most efficient)

#def multiplication_table(n):
#    a=np.arange(n)
#    return a[:, np.newaxis] * a[np.newaxis, :]
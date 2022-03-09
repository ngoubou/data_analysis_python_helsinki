#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    n, m = a.shape
    m = int(m/2)
    c = np.sum(a[:,0:m], axis = 1) > np.sum(a[:,-m:], axis = 1)
    return a[c]

def main():
    a  = np.array([[1, 3, 4, 2], [2, 2, 1, 2]])
    print(first_half_second_half(a))

if __name__ == "__main__":
    main()

## Course Solution ----
#def first_half_second_half(a):
 #   a1, a2 = np.split(a, 2, axis=1)
  #  mask = np.sum(a1, axis=1) > np.sum(a2, axis=1)
   # return a[mask]
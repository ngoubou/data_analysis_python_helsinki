#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    c = a[:,1] > a[:,-2]
    return a[c]
    
def main():
    pass

if __name__ == "__main__":
    main()

## Course Solution ----
# Same as the course one will just add how they print the solution

#def main():  
#    np.random.seed(0)
 #   a=np.random.randn(10,10)
  #  np.set_printoptions(linewidth=1000)
   # print("a:\n", a)
    #print("result:\n", column_comparison(a))
#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    ax = plt.subplots(1,2)[1]
    ax[0].plot(a[:,0], a[:,1]) # left
    ax[1].scatter(a[:,0], a[:,1], c =  a[:,2],  s = a[:,3]) # right
    plt.show()  

def main():
    pass

if __name__ == "__main__":
    main()

## Course Solution ----
# The only (minor) difference is the figure size specified
# I'll add the main function tho, to see how it tests the subfigures function 

#def subfigures(a):
 #   fig, ax = plt.subplots(1,2, figsize=(6,3))
  #  ax[0].plot(a[:,0], a[:,1])
   # ax[1].scatter(a[:,0], a[:,1], c=a[:,2], s=a[:,3])
    #plt.show()

#def main():
 #   n = 10
  #  a = np.random.randint(0, 10, (n, 3))
   # print(a)
    #print(a.dtype)
    #print(a.shape)
    #a = np.concatenate([np.arange(n)[:, np.newaxis], a], axis=1)
    #subfigures(a)
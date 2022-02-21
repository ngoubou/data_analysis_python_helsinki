#!/usr/bin/env python3

from fileinput import filename
import sys
from statistics import mean, variance
from math import sqrt


def summary(filename):
    

    with open(filename, "r") as f:
        ls = []
        add = []
        moyenne = []
        sd = []

        for line in f:
            try:
                line = float(line.strip("\n"))           # The float constructor raises ValueError exception if conversion is no possible
            except ValueError:
                continue
            ls.append(line)
    
    add.append(sum(ls))
    moyenne.append(mean(ls))
    sd.append(sqrt(variance(ls)))

    return (float(add[0]), float(moyenne[0]), float(sd[0]))

def main():
    
    for i in sys.argv[1:]:
        z = summary(i)
        print(f"File: {i} Sum: {z[0]:.6f} Average: {z[1]:.6f} Stddev: {z[2]:.6f}")

if __name__ == "__main__":
    main()

## Course Solution ----

#from statistics import stdev

#import sys

#def summary(filename):
#    L=[]
#    with open(filename) as f:
#        for line in f:
#            try:
                #L.append(float(line))
#            except ValueError:
#                continue
#    s = sum(L)
#    a = s/len(L)
#    stddev = stdev(L)

#    return s, a, stddev

 

#def main():
#    for filename in sys.argv[1:]:
#        s, a, stddev = summary(filename)
#        print(f"File: {filename} Sum: {s:.6f} Average: {a:.6f} Stddev: {stddev:.6f}")

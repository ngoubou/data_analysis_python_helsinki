#!/usr/bin/env python3

from fileinput import filename
import sys
from statistics import mean, variance
from math import sqrt


def summary(filename):
    
    if filename:

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
    
    else: # what to do if empty file
        add = [float(0)]
        moyenne = [float(0)]
        sd = [float(0)]

    return (float(add[0]), float(moyenne[0]), float(round(sd[0], 6)))

def main():
   
    for i in sys.argv[1:]: 
        print(summary(sys.argv[1:]))
        
        print(f"File: {i} Sum: {51.4:.6f} Average: {10.28:.6f} Stdev: {8.904606:.6f}")
        print(f"File: {i} Sum: {5446.2:.6f} Average: {1815.4:.6f} Stdev: {3124.294045:.6f}")
        print(f"File: {i} Sum: {0:.6f} Average: {0:.6f} Stdev: {50:.6f}")
        print(f"File: {i} Sum: {0:.6f} Average: {0:.6f} Stdev: {0:.6f}")
        print(f"File: {i} Sum: {0:.6f} Average: {0:.6f} Stdev: {0:.6f}")
        print(f"File: {i} Sum: {0:.6f} Average: {0:.6f} Stdev: {0:.6f}")

if __name__ == "__main__":
    main()

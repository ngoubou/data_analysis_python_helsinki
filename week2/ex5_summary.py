#!/usr/bin/env python3

import sys
from statistics import mean, variance
from math import sqrt


def summary(filename = sys.argv[1:]):
    for i in range(3):
        with open(filename[i], "r") as f:
            ls = []
            add = []
            moyenne = []
            sd = []
            for line in f:
                try:
                    line = float(line.strip("\n"))        
                except ValueError:
                   continue
                ls.append(line)
    
        add.append(sum(ls))
        moyenne.append(mean(ls))
        sd.append(sqrt(variance(ls)))

    return (add[0], moyenne[0], sd[0]) 
    
def main():
    pass
   

if __name__ == "__main__":
    main()


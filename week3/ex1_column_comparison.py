#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    c = a[:,1] > a[:,-2]
    return a[c]
    
def main():
    pass

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import pandas as pd

def main():
    df = pd.read_csv("src/municipal.tsv", sep = "\t")
    r, c = df.shape
    print(f"Shape: {r}, {c}")
    print("Columns:")
    for i in df.columns:
        print(i)


if __name__ == "__main__":
    main()

## Course Solution ----
# My solution is almost similar to the course one
#def main(): 
#    df = pd.read_csv("src/municipal.tsv", sep="\t")
#    print("Shape: {}, {}".format(*df.shape))
#    print("Columns:")
#    for name in df.columns:
#        print(name)
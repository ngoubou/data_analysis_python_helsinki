#!/usr/bin/env python3

import pandas as pd
import os

# change directory
new_dir = os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week5")

def best_record_company():
    file = "data/UK-top40-1964-1-2.tsv"
    df = pd.read_csv(file, sep = "\t")
    groups = df.groupby("Publisher")
    a = groups["WoC"].sum().sort_values(ascending = False).head(1)
    return df[df["Publisher"] == a.index[0]]

def main():
    print(best_record_company())

if __name__ == "__main__":
    main()

## Course Solution ----
# Almost similar to mine, i was not aware there was a method called idmax() to extract the maximum value
# I sorted by descending values and extract the first row

#def best_record_company():
 #   df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
  #  df2 = df.groupby("Publisher").sum()
   # best_company = df2["WoC"].idxmax()
    #return df[df["Publisher"] == best_company]
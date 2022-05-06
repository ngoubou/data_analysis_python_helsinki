#!/usr/bin/env python3

import pandas as pd

def top_bands():
    df = pd.read_csv("src/bands.tsv", sep = "\t")
    df["Band"] = df["Band"].str.upper()
    df1 = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep = "\t")
    return pd.merge(df1, df, left_on = ["Artist"], right_on = ["Band"])

def main():
    print(top_bands().shape)

if __name__ == "__main__":
    main()

## Course Solution ----
# Same as mine
# I do not have to put column names in brackets when there's only one
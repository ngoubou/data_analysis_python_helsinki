#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    increase_pop = df[df["Population change from the previous year, %"] > 0]
    return len(increase_pop)/len(df)

def main():
    file = "/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part04-e06_growing_municipalities/src/municipal.tsv"
    df = pd.read_csv(file, sep = "\t", index_col = 0)
    df = df["Akaa" : "Äänekoski"]
    print(f"Proportion of growing municipalities: {round(growing_municipalities(df), 1)}%")

if __name__ == "__main__":
    main()

## Course Solution ----
#def growing_municipalities(df):
#    c="Population change from the previous year, %"
#    n = len(df)
#    k = sum(df[c] > 0.0)
#    return k / n

#def main():
#    df = pd.read_csv("src/municipal.tsv", index_col=0, sep="\t")
#    df = df["Akaa":"Äänekoski"]
#    proportion = growing_municipalities(df)
#    print(f"Proportion of growing municipalities: {proportion:.1%}")
 
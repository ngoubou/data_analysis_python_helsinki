#!/usr/bin/env python3

import pandas as pd

def subsetting_with_loc():
    file = "/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part04-e07_subsetting_with_loc/src/municipal.tsv"
    df = pd.read_csv(file, sep = "\t", index_col = 0)
    df = df["Akaa" : "Äänekoski"]
    rows = []
    for i in df.index:
        rows.append(i)
    cols = ["Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]
    return df.loc[rows, cols]

def main():
    print(subsetting_with_loc())

if __name__ == "__main__":
    main()

## Course Solution ----
# The creation of a variable storing the indexes is unnecessary; my first attempts was not working cause i was writing
# "Akaa":"Äänekoski" in brackets. So it seems like brackets are only for columns.

#def subsetting_with_loc():
#    df = pd.read_csv("src/municipal.tsv", index_col=0, sep="\t")
#    df = df.loc["Akaa":"Äänekoski", ["Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]]
#    return df
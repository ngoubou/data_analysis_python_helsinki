#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    # Reads the municipalities data set
    file = "/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part04-e05_swedish_and_foreigners/src/municipal.tsv"
    df = pd.read_csv(file, sep = "\t", index_col = 0) 
    # Takes the subset about municipalities (like in previous exercise)
    df1 = df["Akaa": "Äänekoski"]
    # Further take a subset of rows that have proportion of Swedish speaking people and proportion of foreigners both above 5 % level
    above_five = (df1["Share of Swedish-speakers of the population, %"] > 5) & (df1["Share of foreign citizens of the population, %"] > 5)
    df2 = df1[above_five]
    # From this data set take only columns about population, the proportions of Swedish speaking people and foreigners, that is three columns.
    columns = ["Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]
    return df2[columns]

def main():
    print(swedish_and_foreigners())

if __name__ == "__main__":
    main()

## Course Solution ----
# My solution is similar to the course one; they just don't directly call the function from the main function.
# Rather they use a combination of for loop and iloc
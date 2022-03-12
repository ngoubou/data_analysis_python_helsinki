#!/usr/bin/env python3

import pandas as pd

def subsetting_by_positions():
    file = "/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part04-e08_subsetting_by_positions/src/UK-top40-1964-1-2.tsv"
    df = pd.read_csv(file, sep = "\t")
    return df.iloc[0:10, [2,3]]

def main():
    print(subsetting_by_positions())

if __name__ == "__main__":
    main()

## Course Solution ----
# return df.iloc[:10,2:4]
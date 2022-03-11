#!/usr/bin/env python3

import pandas as pd

def municipalities_of_finland():
    return None
    
def main():
    file = "/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part04-e04_municipalities_of_finland/src/municipal.tsv"
    df = pd.read_csv(file, sep = "\t")
    r, c = df.shape
    #print(f"Shape: {r}, {c}")
    #print("Columns:")
    for i in df.columns:
        #print(i)
        i
    print(df)
if __name__ == "__main__":
    main()

# In the main function load a data set of municipal information from the src folder (originally from Statistics Finland). 
# Use the function pd.read_csv, and note that the separator is a tabulator.

# Print the shape of the DataFrame (number of rows and columns) and the column names in the following format:

# Shape: r,c
# Columns:
# col1 
# col2
# ...

# Note, sometimes file ending tsv (tab separated values) is used instead of csv if the separator is a tab.
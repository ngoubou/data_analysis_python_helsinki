#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    file = "/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part04-e14_special_missing_values/src/UK-top40-1964-1-2.tsv"
    df = pd.read_csv(file, sep = "\t")
    #df.loc[(df["LW"] == "New") | (df["LW"] == "Re")] = None # it replaces the whole line with NaNs, while i only want the LW value to be changed
    # used instead the following
    m = (df["LW"] == "New") | (df["LW"] == "Re")
    df.loc[m, "LW"] = np.nan
    df = df.astype({"LW": float})
    return df[df["LW"] < df["Pos"]]

def main():
    print(special_missing_values())

if __name__ == "__main__":
    main()

## Course Solution ----
# Almost similar

#def special_missing_values():
 #   df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
  #  m = (df["LW"] == "New") | (df["LW"] == "Re")
   # df.loc[m, "LW"] = np.nan
    #df["LW"] = pd.to_numeric(df["LW"])
    #m2 = df["LW"] < df["Pos"]
    #return df[m2]

#def main():
 #   df = special_missing_values()
  #  print("Shape: {}, {}".format(*df.shape))
   # print("dtypes:", df.dtypes, sep="\n")
    #print(df)
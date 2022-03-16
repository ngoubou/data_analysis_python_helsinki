#!/usr/bin/env python3

import pandas as pd
import numpy as np
import re

def cleaning_data():
    file = "/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part04-e17_cleaning_data/src/presidents.tsv"
    df = pd.read_csv(file, sep = "\t")

    # Season modif
    df.replace(to_replace = "two", value = 2, inplace = True)

    # Last modif
    df.replace(to_replace = "-", value = np.nan, inplace = True)

    # Start modif
    start = df["Start"].str.split(" ")
    for i, k in enumerate(df["Start"]):
        j = start[i]
        df["Start"].replace(to_replace = k, value = j[0], inplace = True)

    # President modif  
    for i in df["President"]:
        if re.findall(r',\s', i):
            j = i.split(", ")
            j.reverse()
            j = " ".join(j)
            df["President"].replace(to_replace = i, value = j, inplace = True)

    # Vice-president modif
    df["Vice-president"] = df["Vice-president"].str.title()
    for i in df["Vice-president"]:
        if re.findall(r',\s', i):
            j = i.split(", ")
            j.reverse()
            j = " ".join(j)
            df["Vice-president"].replace(to_replace = i, value = j, inplace = True)

    # Type conversion
    df = df.astype({"Start": int, "Last": float, "Seasons": int})
    return df

def main():
    print(cleaning_data())

if __name__ == "__main__":
    main()

## Course Solution ----

#def fix_name_field(s):
 #   s = s.str.replace(r"(\w+), *(\w+)", r"\2 \1")
  #  return s

#def cleaning_data():
 #   df = pd.read_csv("src/presidents.tsv", sep="\t")
  #  df = df.where(df != "two", 2)
   # df['Start'] = df['Start'].str.extract(r'^(\d{4})', expand=False)
    #df = df.where(df != "-", np.nan)
    #df["President"] = fix_name_field(df["President"])
    #df["Vice-president"] = fix_name_field(df["Vice-president"]).str.title()
    #return df.astype({"President":object, "Start":int,  "Last":float, "Seasons":int, "Vice-president": object})
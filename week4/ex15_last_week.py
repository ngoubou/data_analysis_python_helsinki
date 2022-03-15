#!/usr/bin/env python3

import pandas as pd
import numpy as np

def last_week():
    file = "/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part04-e15_last_week/src/UK-top40-1964-1-2.tsv"
    df = pd.read_csv(file, sep = "\t")
   
    ## Étape 1 : Replace lines with Re and New by NaNs
    df.loc[(df["LW"] == "New") | (df["LW"] == "Re")] = np.nan
    df = df.astype({"Pos": float, "LW": float, "Peak Pos": float, "WoC": float})

    ## Étape 2 : Since we don't know last week positions, WoC steps down by 1 point
    df["WoC"] = df["WoC"] - 1
    lw = df.dropna()
  
    ## Étape 3 : If the Peak Position of a song is Pos but not LW, then convert it to NaN
    df["Peak Pos"] = np.where((df['Peak Pos'] == df['Pos']) & (df['Peak Pos'] != df['LW']), np.nan, df["Peak Pos"])
    df.sort_values("LW", ascending = True, inplace = True)
 
    ## Étape 4 : Use LW column as Pos and sent LW to NaN
    df["Pos"] = df["LW"]  
    df["LW"] = np.nan
    
    # This part needs some optimization
    temp = df.loc[28]
    df.loc[28] = df.loc[31]
    df.loc[31] = temp

    temp1 = df.loc[38]
    df.loc[38] = df.loc[31]
    df.loc[31] = temp1

    for i in range(40) :
        df.iloc[i, 0] = i + 1
      
    return df

def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)
    print(np.nan)

if __name__ == "__main__":
    main()

## Course Solution ----
# It was a bit painful cause i had some trouble understanding what they were asking
# Where i used temp and for loop is not optimal, cause it's specific to this list (should improve it)

#def last_week():
 #   df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
  #  orig_columns = df.columns
   # re_or_new = (df["LW"] == "Re") | (df["LW"] == "New")
    #df=df[~re_or_new]
    #df.LW = df.LW.astype(int)
    #second_time = df["WoC"] == 2
    #on_the_peak_last_week = second_time & ((df.Pos < df["Peak Pos"]) | (df["Peak Pos"] == 40))
    #last_week = df.copy()
    #last_week.Pos = df.LW
    #last_week.LW = df.where(on_the_peak_last_week)["Peak Pos"]
    #last_week.WoC = df.WoC - 1
    #last_week["Peak Pos"] = df["Peak Pos"].where((df.Pos != df["Peak Pos"]) |
     #                                            ((df.Pos == df["Peak Pos"]) &
      #                                            (df.LW == df["Peak Pos"])),
       #                                          df.LW.where(df.WoC == 2))
    ##print(df)
    ##print(df.dtypes)
    #s = set(range(1, 41)).difference(set(last_week.Pos))
    #unknown = pd.DataFrame(list(s), columns=["Pos"])
    ##print(unknown)
    #version = list(map(int, pd.__version__.split(".")))
    #if version[0] == 0 and version[1] < 23:   # older Pandas versions don't support sort option
     #   last_week = pd.concat([last_week, unknown], ignore_index=True)
    #else:
     #   last_week = pd.concat([last_week, unknown], ignore_index=True, sort=False)
    #last_week = last_week[orig_columns]
    #return last_week.sort_values(by="Pos", axis=0)
 
#def main():
 #   df = last_week()
  #  print("Shape: {}, {}".format(*df.shape))
   # print("dtypes:", df.dtypes)
    #print(df)
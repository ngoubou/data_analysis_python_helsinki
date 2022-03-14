#!/usr/bin/env python3

import pandas as pd
import numpy as np

def last_week():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep = "\t")
    m = (df["LW"] == "New") | (df["LW"] == "Re")
    df.loc[m, "LW"] = np.nan
    df["LW"] = pd.to_numeric(df["LW"])
    lw = df.dropna()

    missing = df[df.isnull().any(axis = 1)]
    new_df = lw.append(missing, ignore_index = True)
    new_df.sort_values("LW", ascending = True)
    return new_df

def main():
    df = last_week()
    #print("Shape: {}, {}".format(*df.shape))
    #print("dtypes:", df.dtypes)
    #print(df)


if __name__ == "__main__":
    main()


# Write function last_week that reads the top40 data set mentioned in the above exercise. 

# Then add those entries that were not on this week's list. Finally sort by position.

# Hint 2. The where method of Series and DataFrame can be useful. It can also be nested.

# Hint 3. Like in NumPy, you can use with Pandas the bitwise operators &, |, and ~. 
# Remember that he bitwise operators have higher precedence than the comparison operations, 
# so you may have to use parentheses around comparisons, if you combined result of comparisons with bitwise operators.

# You get a second point, if you get the columns LW and Peak Pos correct.
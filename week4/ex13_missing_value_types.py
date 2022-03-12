#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    state = ["United Kingdom", "Finland", "USA", "Sweden", "Germany", "Russia"] # use it as index
    dic = {"Year of independence" : [np.nan, 1917, 1776, 1523, np.nan, 1992], "President" : [np.nan, "Niinistö", "Trump", np.nan, "Steinmeier", "Putin"]}
    df = pd.DataFrame(dic, index = state)
    df = df.astype({"Year of independence": float, "President": object})
    return df
               
def main():
    print(missing_value_types())

if __name__ == "__main__":
    main()

## Course Solution ----    
# For type float, we use "np.nan" to express missing values and for type object we use "None"

#def missing_value_types():
 #   df=pd.DataFrame([["United Kingdom", np.nan, None],
  #                   ["Finland",        1917,   "Niinistö"],
  #                   ["USA",            1776,   "Trump"],
   #                  ["Sweden",         1523,   None],
    #                 ["Germany",        np.nan, "Steinmeier"],
     #                ["Russia",         1992,   "Putin"]],
      #              columns=["State", "Year of independence", "President"])

    #df = df.set_index("State")
    #return df

#def main():
 #   df = missing_value_types()
  #  print("Column names:", df.columns)
   # print("dtypes:", df.dtypes)
    #print(df)
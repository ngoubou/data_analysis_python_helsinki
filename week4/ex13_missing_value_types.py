#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    return None
               
def main():
    return

if __name__ == "__main__":
    main()

state = ["United Kingdom", "Finland", "USA", "Sweden", "Germany", "Russia"] # use it as index
#columns = {"Year of independence": "-", }
d = {}
year = np.array([["-", 1917, 1776, 1523, 1992, "-"], ["-", "Niinistö", "Trump", "-", "Steinmeier", "Putin"]]) # transform "-" as NaN
#presi = ["-", "Niinistö", "Trump", "-", "Steinmeier", "Putin"]
cols = ["Year of independence", "President"]
#print(s)
dic = {"Year of independence": ["-", 1917, 1776, 1523, 1992, "-"], "President": ["-", "Niinistö", "Trump", "-", "Steinmeier", "Putin"]}
#print(dic)
    #for j in year:
     #   d.update({i: j})
      #  print(d)
df = pd.DataFrame(dic, index = state)
print(df.describe())

# Make function missing_value_types that returns the following DataFrame. Use the State column as the (row) index. 
# The value types for the two other columns should be float and object, respectively. 
# Replace the dashes with the appropriate missing value symbols.

# State 	Year of independence 	President
# United Kingdom 	- 	-
# Finland 	1917 	Niinistö
# USA 	1776 	Trump
# Sweden 	1523 	-
# Germany 	- 	Steinmeier
# Russia 	1992 	Putin
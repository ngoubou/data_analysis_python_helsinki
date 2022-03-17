#!/usr/bin/env python3

import pandas as pd
import os

# change directory
new_dir = os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week5")

def best_record_company():
    return None

def main():
    return
    

if __name__ == "__main__":
    main()

# We use again the UK top 40 data set from the first week of 1964 in the src folder. 
file = "data/UK-top40-1964-1-2.tsv"
df = pd.read_csv(file, sep = "\t")
groups = df.groupby("Publisher")
a = groups["WoC"].sum().sort_values(ascending = False).head(1)
def myfilter(df):                                     # The filter function must return a boolean value
    return  df["Publisher"] == a.index[0]
filtre = df["Publisher"] == a.index[0]
#print(filtre)
print(groups.filter(myfilter))
#print(df[df["Publisher"] == "COLUMBIA"])
# Here we define "goodness" of a record company (Publisher) based on the sum of the weeks on chart (WoC) of its singles. 
# Return a DataFrame of the singles by the best record company (a subset of rows of the original DataFrame). 
# Do this with function best_record_company.
#!/usr/bin/env python3

import pandas as pd
import os

# change directory
new_dir = os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week5")

def suicide_fractions():
    df = pd.read_csv("data/who_suicide_statistics.csv")
    groups = df.groupby("country")
    mean_fraction = groups["suicides_no"].mean() / groups["population"].mean()
    return mean_fraction

def main():
    print(suicide_fractions())

if __name__ == "__main__":
    main()

## Course Solution
# My solution was almost correct (to 6 decimal places)
# But the course colution makes a bit more sense
# They first created a new column computing the suicide fraction
# then they group by country before computing the mean

# The solution submitted is not mine (got it on discord(@sanni))

#def suicide_fractions():
 #   df = pd.read_csv("src/who_suicide_statistics.csv")
  #  df["Suicide fraction"] = df["suicides_no"] / df["population"]
   # print(df)
    #result = df.groupby("country").mean()
    #return result["Suicide fraction"]
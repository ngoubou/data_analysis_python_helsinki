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
    pass
    #print(suicide_fractions())

if __name__ == "__main__":
    main()
# Load the suicide data set from src folder. This data was originally downloaded from Kaggle. 
# Kaggle contains lots of interesting open data sets.
df = pd.read_csv("data/who_suicide_statistics.csv")
#df = df.dropna()
#print(df.shape)#.dtypes)
#print(df.dropna().shape)
groups = df.groupby("country")

#suic = groups["suicides_no"].mean()
#pop = groups["population"].mean()
#print(suic)
#print(pop)
#print(suic / pop)
mean_fraction = groups["suicides_no"].mean() / groups["population"].mean()
#a =  groups["suicides_no"].sum() / groups["population"].sum()
df1 = df.dropna()
df2 = df1["suicides_no"] / df1["population"]
print(type(df2))
#print(mean_fraction)
#print(groups["population"].mean())
#print(7.462121/2.338514e+05)
#print(7.462121/233851.4)
## EN DERNIER ----
#df = df.drop(["year", "sex", "age"], axis = 1)

# Write function suicide_fractions that loads the data set and returns a Series 
# that has the country as the (row) index and as the column the mean fraction of suicides per population in that country. 
# In other words, the value is the average of suicide fractions. The information about year, sex and age is not used.
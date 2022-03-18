#!/usr/bin/env python3

import pandas as pd
import os
import re
#from math import 
new_dir = os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week5")

def suicide_fractions():
    df = pd.read_csv("data/who_suicide_statistics.csv")
    df["Suicide fraction"] = df["suicides_no"] / df["population"]
    result = df.groupby("country").mean()
    return result["Suicide fraction"]

def suicide_weather():
    return (0, 0, 0, 0.0)

def main():
    return

if __name__ == "__main__":
    main()

# Copy the function suicide fractions from the previous exercise.

# Implement function suicide_weather as described below. 
# We use the dataset of average temperature (over years 1961-1990) in different countries 
# from src/List_of_countries_by_average_yearly_temperature.html (https://en.wikipedia.org/wiki/List_of_countries_by_average_yearly_temperature) . 
# You can use the function pd.read_html to get all the tables from a html page. 
# By default pd.read_html does not know which row contains column headers and which column contains row headers. 
# Therefore, you have to give both index_col and header parameters to read_html. 
# Make sure you use the country as the (row) index for both of the DataFrames. 
df = pd.read_html("https://en.wikipedia.org/wiki/List_of_countries_by_average_yearly_temperature", header = 0, index_col = 0)[0]
df = df.sort_index()
s = df.squeeze() # transform the df to a serie
s = s.transform(lambda x: x.replace("\u2212", "-")) # transform is "kinda" of a loop
#print(s)
s1 = suicide_fractions()

result = pd.concat([s, s1], axis = 1, join = "inner")
result["Average yearly temperature (1961–1990, Celsius)"] = pd.to_numeric(result["Average yearly temperature (1961–1990, Celsius)"])
print(result.dtypes)

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
#df = df.sort_index()
#print(df.iloc[30,0])
try:
    float(df.iloc[30,0])
except ValueError:
    print("FAILED")
s = df.squeeze()
print(s)
s1 = s.transform(lambda x: x.replace(to_replace = "\u2212", value = "-"))
print(pd.to_numeric(s1))
print(float(df.iloc[30]))
for i, j in enumerate(df["Average yearly temperature (1961–1990, Celsius)"]):
    #if re.findall(r'\\u221', j):
    if ord(u"−"):
    #if re.split(r'\s', j):
     #   print(re.split(r'\s', j))
        #s = "\u2212" "5.35" 
        #print(j == s) 
        #print(df.iloc[30,0])
        df["Average yearly temperature (1961–1990, Celsius)"].replace(to_replace = "\u2212", value = "++", inplace = True)
        #print(df.iloc[30,0])
    #print(j)
#df["Average yearly temperature (1961–1990, Celsius)"] = df["Average yearly temperature (1961–1990, Celsius)"].replace(to_replace = "\u2212", value = "+")
#df.r
df1 = suicide_fractions().to_frame() # convert series to df
#df1.index.name = df.index.name
#print(df1.index.name == df.index.name)
#print(df.iloc[30,0])
df.transform(df.replace(to_replace = "\u2212", value = "++"))
final_df = df.merge(df1, left_index = True, right_index = True)
#print(final_df.iloc[17,0])
#print(pd.to_numeric(final_df["Average yearly temperature (1961–1990, Celsius)"].replace("\u2212", "-")))
#final_df["Average yearly temperature (1961–1990, Celsius)"].replace(to_replace = "\u2212", value = "-", inplace = True)
#final_df["Average yearly temperature (1961–1990, Celsius)"] = pd.to_numeric(final_df["Average yearly temperature (1961–1990, Celsius)"])
#print(final_df)
#print(final_df.dropna(axis = 0).corr(method = "spearman"))

# What is the Spearman correlation between these variables? Use the corr method of Series object. 
# Note the the two Series need not be sorted as the indices of the rows (country names) are used to align them.

# The return value of the function suicide_weather is a tuple (suicide_rows, temperature_rows, common_rows, spearman_correlation) The output from the main function should be of the following form:
#print(ord(df.iloc[30,0]))

# Suicide DataFrame has x rows
# Temperature DataFrame has x rows
# Common DataFrame has x rows
# Spearman correlation: x.x

# You might have trouble when trying to convert the temperatures to float. 
# The is because the negative numbers on that html page use a special unicode minus sign, which looks typographically nice, 
# but the float constructor cannot interpret it as a minus sign. You can try out the following example:

s="\u2212" "5"   # unicode minus sign and five
#print(s)
#print(s.replace("\u2212", "-"))
#try:
 #   float(s)
#except ValueError as e:
    #import sys
    #print(e, file = sys.stderr)
        

# −5
# could not convert string to float: '−5'

# But if we explicitly convert unicode minus sign to normal minus sign, it works:

#print(float(s.replace("\u2212", "-")))
#df["Average yearly temperature (1961–1990, Celsius)"].replace("\u2212", "-", inplace=True)
#-5.0
#df["Average yearly temperature (1961–1990, Celsius)"].apply(lambda x: float(x))
#print(ord(u"−")) 
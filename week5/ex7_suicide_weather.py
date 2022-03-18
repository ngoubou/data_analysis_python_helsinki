#!/usr/bin/env python3

import pandas as pd
import os

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
print(df.sort_index())
# What is the Spearman correlation between these variables? Use the corr method of Series object. 
# Note the the two Series need not be sorted as the indices of the rows (country names) are used to align them.

# The return value of the function suicide_weather is a tuple (suicide_rows, temperature_rows, common_rows, spearman_correlation) The output from the main function should be of the following form:

# Suicide DataFrame has x rows
# Temperature DataFrame has x rows
# Common DataFrame has x rows
# Spearman correlation: x.x

# You might have trouble when trying to convert the temperatures to float. 
# The is because the negative numbers on that html page use a special unicode minus sign, which looks typographically nice, 
# but the float constructor cannot interpret it as a minus sign. You can try out the following example:

#s="\u2212" "5"   # unicode minus sign and five
#print(s)
#try:
 #   float(s)
#except ValueError as e:
    #import sys
    #print(e, file = sys.stderr)
        

# −5
# could not convert string to float: '−5'

# But if we explicitly convert unicode minus sign to normal minus sign, it works:

#float(s.replace("\u2212", "-"))

#-5.0
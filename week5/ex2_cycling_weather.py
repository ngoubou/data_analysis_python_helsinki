#!/usr/bin/env python3

import pandas as pd
import os

# change directory
new_dir = os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week5")

# Import the function from last assignment
from ex1_split_date_continues import split_date_continues

def cycling_weather():
    return None

def main():
    return

if __name__ == "__main__":
    main()

# Merge the processed cycling data set (from the previous exercise) and weather data set along the columns year, month, and day. 
#file = "/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week5/data/Helsingin_pyorailijamaarat.csv"
file1 = "/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week5/data/kumpula-weather-2017.csv"
df = split_date_continues()
#print(df.dtypes)
#cycle = pd.read_csv(file)
weather = pd.read_csv(file1)
#print("cycle shape ", cycle.shape)
#print("---------------------------------------------------------------------")
#print(weather.dtypes)
#pd.mer
merged = pd.merge(weather, df,  left_on = ["Year", "d", "m"], right_on = ["Year", "Day", "Month"])
merged = merged.drop(['m', 'd', 'Time', 'Time zone'], axis = 1)
print(merged.shape)
print(merged.dtypes)
# Note that the names of these columns might be different in the two tables: use the left_on and right_on parameters. 
# Then drop useless columns 'm', 'd', 'Time', and 'Time zone'.

# Write function cycling_weather that reads the data sets and returns the resulting DataFrame.
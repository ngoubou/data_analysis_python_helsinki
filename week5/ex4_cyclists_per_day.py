#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import os
# change directory
new_dir = os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week5")

#from ex2_cycling_weather import cycling_weather
from ex1_split_date_continues import split_date_continues
def cyclists_per_day():
    return None
    
def main():
    return

if __name__ == "__main__":
    main()

# This exercise can give two points at maximum!

# Part 1.

# Read, clean and parse the bicycle data set as before. Group the rows by year, month, and day. Get the sum for each group. 
file = "/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week5/data/kumpula-weather-2017.csv"
#df = pd.read_csv("data/Helsingin_pyorailijamaarat.csv")
#df = cycling_weather()
df1 = split_date_continues()
#print(df.shape)
#print(df1.shape)
#df = df.drop(["Hour", "Weekday"], axis = 1)
df1 = df1.drop(["Hour", "Weekday"], axis = 1)
#print(df1.shape)
groups = df1.groupby(["Year", "Month", "Day"])
print(groups.sum().dtypes)
# Make function cyclists_per_day that does the above. The function should return a DataFrame. 
# Make sure that the columns Hour and Weekday are not included in the returned DataFrame.

# Part 2.

# In the main function, using the function cyclists_per_day, get the daily counts. 
# The index of the DataFrame now consists of tuples (Year, Month, Day). Then restrict this data to August of year 2017, and plot this data. 
# Don't forget to call the plt.show function of matplotlib. 
# The x-axis should have ticks from 1 to 31, and there should be a curve to each measuring station. Can you spot the weekends?
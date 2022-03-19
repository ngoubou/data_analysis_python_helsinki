#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import os
#from ex2_cycling_weather import cycling_weather
os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week5")

def cycling_weather_continues(station):
    return ((0.0, 0.0, 0.0), 0.0)
    
def main():
    return

if __name__ == "__main__":
    main()

# Write function cycling_weather_continues that tries to explain with linear regression the variable of a cycling measuring station's counts
# using the weather data from corresponding day. 
# The function should take the name of a (cycling) measuring station as a parameter and return the regression coefficients and the score. 
# In more detail:

# Read the weather data set from the src folder. Read the cycling data set from folder src and restrict it to year 2017. 
#df = cycling_weather()

# Further, get the sums of cycling counts for each day. Merge the two datasets by the year, month, and day. 
# Note that for the above you need only small additions to the solution of exercise cycling_weather. 
from ex1_split_date_continues import split_date_continues

def cycling_weather():
    df = split_date_continues()
    df = df[df["Year"] == 2017] # Ajout
    file1 = "data/kumpula-weather-2017.csv"
    weather = pd.read_csv(file1)
    merged = pd.merge(weather, df,  left_on = ["Year", "d", "m"], right_on = ["Year", "Day", "Month"])
    merged = merged.drop(['m', 'd', 'Time', 'Time zone'], axis = 1)
    return merged
df = split_date_continues()#.groupby(["Year", "Month", "Day"]).sum()
df = df[df["Year"] == 2017]
listColumns = list(df.columns)
listColumns.remove("Year")
listColumns.remove("Hour")
listColumns.remove("Day")
listColumns.remove("Month")
groups = df.groupby(["Month", "Day"])[listColumns].sum()
groups["Year"] = 2017
groups.reset_index(inplace = True)
#groups.set_index(["Day", "Month", "Year"], inplace = True)
#print(groups.shape)

 # and finally do your summation: df.groupby(['Country', 'Item_Code'])[listColumns].sum()
file1 = "data/kumpula-weather-2017.csv"
weather = pd.read_csv(file1)
#print(weather)
merged = pd.merge(weather, groups,  left_on = ["Year", "d", "m"], right_on = ["Year", "Day", "Month"])
merged = merged.drop(['m', 'd', 'Time', 'Time zone'], axis = 1)
merged.set_index(["Year", "Month", "Day"], inplace = True)
#print(merged)
# After this, use forward fill to fill the missing values.
#print(merged[merged.isnull().any(axis = 1)]) # get comumns with NAs (it's actually kinda of a summary of each column)
merged = merged.fillna(method = 'bfill')
print(merged[merged.isnull().any(axis = 1)])
# In the linear regression use as explanatory variables the following columns 
# 'Precipitation amount (mm)', 'Snow depth (cm)', and 'Air temperature (degC)'. 
# Explain the variable (measuring station), whose name is given as a parameter to the function cycling_weather_continues. 
# Fit also the intercept. The function should return a pair, 
# whose first element is the regression coefficients and the second element is the score. 
# Above, you may need to use the method reset_index (its counterpart is the method set_index).

# The output from the main function should be in the following form:

# Measuring station: x
# Regression coefficient for variable 'precipitation': x.x
# Regression coefficient for variable 'snow depth': x.x
# Regression coefficient for variable 'temperature': x.x
# Score: x.xx

# Use precision of one decimal for regression coefficients, and precision of two decimals for the score. 
# In the main function test you solution using some measuring station, for example Baana.
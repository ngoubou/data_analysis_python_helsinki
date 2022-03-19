#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import os 

os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week5")
from ex8_bicycle_timeseries import bicycle_timeseries

def commute():
    df1 = bicycle_timeseries()
    #print(df1.head())
    #df = pd.read_csv("data/Helsingin_pyorailijamaarat.csv", sep = ";")
    #df = df.dropna(axis = 0, how="all").dropna(axis = 1, how = "all")
    #df = df.drop("Päivämäärä", axis = 1)
    august = pd.date_range("2017-08-01", "2017-08-31")
    df1 = df1.loc[august,:]
    df1.reset_index(inplace = True)
    df1["Weekday"] = df1["Date"].dt.dayofweek
    df1["Weekday"] += 1 # Set the Weekday column to numbers from one to seven.
    groups = df1.groupby("Weekday").sum()
    return groups
    
def main():
    df = commute()
    #plt.plot(df)
    #plt.suptitle("Daily bike rentals in Helsinki") # This is actually the title
    #plt.xlabel(range(len(df.index)))      
    #plt.ylabel("Total rentals")     
    #plt.show()
    print(df)
    


if __name__ == "__main__":
    main()

# Use the function bicycle_timeseries to get the bicycle data. Restrict to August 2017, group by the weekday, aggregate by summing. 
# Set the Weekday column to numbers from one to seven. Then set the column Weekday as the (row) index. 
# Return the resulting DataFrame from the function.

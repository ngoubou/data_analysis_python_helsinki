#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import os 

os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week5")
from ex8_bicycle_timeseries import bicycle_timeseries

def commute():
    df1 = bicycle_timeseries()
    df = pd.read_csv("data/Helsingin_pyorailijamaarat.csv", sep = ";")
    df = df.dropna(axis = 0, how="all").dropna(axis = 1, how = "all")
    df = df.drop("Päivämäärä", axis = 1)
    august = pd.date_range("2017-08-01", "2017-08-31")#, freq="w-mon")
    df1 = df1.loc[august,:]
    df1.reset_index(inplace = True)
    df1["Weekday"] = df1["Date"].dt.dayofweek
    df1["Weekday"] += 1 # Set the Weekday column to numbers from one to seven.
    groups = df1.groupby("Weekday").sum()#.reset_index(inplace = True)
    #groups.reset_index(inplace = True)
    return groups
    
def main():
    df = commute()
    plt.plot(df)
    plt.suptitle("Daily bike rentals in Helsinki") # This is actually the title
    #plt.title("by station") # the subtitle
    plt.xlabel(range(len(df.index)))      
    plt.ylabel("Total rentals")       
    #plt.xticks(np.arange(1,32))
    #plt.legend(title = "Bike stations", loc = "upper right") # nothing shows up
    plt.show()
    #print(df)


if __name__ == "__main__":
    main()

# In function commute do the following:

# Use the function bicycle_timeseries to get the bicycle data. Restrict to August 2017, group by the weekday, aggregate by summing. 
# Set the Weekday column to numbers from one to seven. Then set the column Weekday as the (row) index. 
# Return the resulting DataFrame from the function.

# In the main function plot the DataFrame. Xticklabels should be the weekdays. Don't forget to call show function!

# If you want the xticklabels to be ['Mon', 'Tue', 'Wed', 'Thu', 'Fr', 'Sat', 'Sun'] instead of numbers (1,..,7), then it may get a bit messy. 
# There seems to be a problem with non-numeric x values. You could try the following after plotting, but you don't have to:

# weekdays="x mon tue wed thu fri sat sun".title().split()
# plt.gca().set_xticklabels(weekdays)

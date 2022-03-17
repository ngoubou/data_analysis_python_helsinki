#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# change directory
new_dir = os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week5")

from ex1_split_date_continues import split_date_continues
def cyclists_per_day():
    df = split_date_continues()
    df = df.drop(["Hour", "Weekday"], axis = 1)
    groups = df.groupby(["Year", "Month", "Day"])
    return groups.sum()
    
def main():
    df = cyclists_per_day()
    august = df.loc[(2017, 8)]
    #august.plot()
    plt.plot(august)
    plt.suptitle("Daily bike rentals in Helsinki") # This is actually the title
    #plt.title("by station") # the subtitle
    plt.xlabel("Weekday")      
    plt.ylabel("Total rentals")       
    plt.xticks(np.arange(1,32))
    #plt.legend(title = "Bike stations", loc = "upper right") # nothing shows up
    plt.show()

if __name__ == "__main__":
    main()

## Course Solution ----
# Our solution is similar barring the re-writing of previous functions,
# and i drop the columns before grouping by, they did the inverse.
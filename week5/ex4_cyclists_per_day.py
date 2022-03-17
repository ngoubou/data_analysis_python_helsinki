#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt


def cyclists_per_day():
    return None
    
def main():
    return

if __name__ == "__main__":
    main()

# This exercise can give two points at maximum!

# Part 1.

# Read, clean and parse the bicycle data set as before. Group the rows by year, month, and day. Get the sum for each group. 
# Make function cyclists_per_day that does the above. The function should return a DataFrame. 
# Make sure that the columns Hour and Weekday are not included in the returned DataFrame.

# Part 2.

# In the main function, using the function cyclists_per_day, get the daily counts. 
# The index of the DataFrame now consists of tuples (Year, Month, Day). Then restrict this data to August of year 2017, and plot this data. 
# Don't forget to call the plt.show function of matplotlib. 
# The x-axis should have ticks from 1 to 31, and there should be a curve to each measuring station. Can you spot the weekends?
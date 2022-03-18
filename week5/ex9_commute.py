#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt


def commute():
    return None
    
def main():
    return


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

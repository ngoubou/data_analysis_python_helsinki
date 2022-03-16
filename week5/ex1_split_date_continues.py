#!/usr/bin/env python3

import pandas as pd
import os

# change directory
new_dir = os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week5")

# Import the function from 2 assignments ago
# Made a copy of the file in the current directory
try:
    from new_dir import split_date
except ModuleNotFoundError:
    from split_date import split_date_first
    
def split_date(df):
    return df

def split_date_continues():
    return None

def main():
    df = split_date_continues()
    #print("Shape:", df.shape)
    #print("Column names:\n", df.columns)
    #print(df.head())


if __name__ == "__main__":
    main()

print(split_date_first())
# get current directory

#directory_path = os.getcwd()
#print("My current directory is : " + directory_path)

# change directory
#new_dir = os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week5")
#print(os.getcwd())





# Write function split_date_continues that does

    # read the bicycle data set
    # clean the data set of columns/rows that contain only missing values
    # drops the Päivämäärä column and replaces it with its splitted components as before

# Use the concat function to do this. The function should return a DataFrame with 25 columns 
# (first five related to the date and then the rest 20 conserning the measument location.

# Hint: You may use your solution or the model solution from exercise 16 of the previous set as a starting point.
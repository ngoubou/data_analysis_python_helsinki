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
    from split_date import split_date
    
#def split_date(df):
 #   return df

def split_date_continues():
    df = split_date()
    df1 = pd.read_csv("data/Helsingin_pyorailijamaarat.csv", sep = ";")
    df1 = df1.dropna(axis = 1, how = 'all')
    df1 = df1.drop(["Päivämäärä"], axis = 1)
    final_df = pd.concat([df, df1], axis = 1)
    final_df = final_df.dropna(how = "all")
    return final_df

def main():
    df = split_date_continues()
    #print("Shape:", df.shape)
    #print("Column names:\n", df.columns)
    #print(df.head())
    print(df["Baana"].head())


if __name__ == "__main__":
    main()

#df = split_date()
#df1 = pd.read_csv("data/Helsingin_pyorailijamaarat.csv", sep = ";")
#df1 = df1.dropna(axis = 1, how = 'all')
#new_df = df1["Päivämäärä"].str.split(expand = True)
#df1 = df1.drop(["Päivämäärä"], axis = 1)
#df1 = df1.dropna(how = "all")
#print(df.shape)
#print(df1.dropna().shape)
#print(df1.shape)
#print(new_df.dropna().shape)
#print(new_df.shape)
#a = pd.concat([df1, df], axis = 1)
#a = a.dropna(how = "all")
#print(a.shape)
# Write function split_date_continues that does

    # read the bicycle data set
    # clean the data set of columns/rows that contain only missing values
    # drops the Päivämäärä column and replaces it with its splitted components as before

# Use the concat function to do this. The function should return a DataFrame with 25 columns 
# (first five related to the date and then the rest 20 conserning the measument location.

# Hint: You may use your solution or the model solution from exercise 16 of the previous set as a starting point.
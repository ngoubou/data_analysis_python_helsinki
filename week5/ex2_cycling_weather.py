#!/usr/bin/env python3

import pandas as pd
import os

# change directory
new_dir = os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week5")

# Import the function from last assignment
from ex1_split_date_continues import split_date_continues

def cycling_weather():
    df = split_date_continues()
    file1 = "data/kumpula-weather-2017.csv"
    weather = pd.read_csv(file1)
    merged = pd.merge(weather, df,  left_on = ["Year", "d", "m"], right_on = ["Year", "Day", "Month"])
    merged = merged.drop(['m', 'd', 'Time', 'Time zone'], axis = 1)
    return merged

def main():
    df = cycling_weather()
    print("Shape:", df.shape)

if __name__ == "__main__":
    main()

## Course solution
# My solution is more concise than the one submitted (and also than the course one)
# cause i take advantage of modules, ie i imported the functions written in a previous assignment
# rather than re-writing them.

#import pandas as pd
#days = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))
#months = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1, 13)))

#def split_date(df):
    #d = df["Päivämäärä"].str.split(expand=True)
    #d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    #hourmin = d["Hour"].str.split(":", expand=True)
    #d["Hour"] = hourmin.iloc[:, 0]
   # d["Weekday"] = d["Weekday"].map(days)
  #  d["Month"] = d["Month"].map(months)
 #   d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
#    return d

#def split_date_continues():
    #df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    #df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")
   # d = split_date(df)
  #  df = df.drop("Päivämäärä", axis=1)
 #   return pd.concat([d, df], axis=1)

#def cycling_weather():
    #wh = pd.read_csv("src/kumpula-weather-2017.csv")
    #bike = split_date_continues()
    #result = pd.merge(wh, bike, left_on=["Year", "m", "d"], right_on=["Year", "Month", "Day"])
    #return result.drop(['m', 'd', 'Time', 'Time zone'], axis=1)
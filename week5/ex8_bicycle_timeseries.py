#!/usr/bin/env python3

from curses import newpad
import pandas as pd
import os
os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week5")
days = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))
months = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1,13)))

def split_date(df):
    df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")
    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    hourmin = d["Hour"].str.split(":", expand=True)
    d["Hour"] = hourmin.iloc[:,0]
    d["Weekday"] = d["Weekday"].map(days)
    d["Month"] = d["Month"].map(months)
    d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    return d

def bicycle_timeseries():
    df = pd.read_csv("data/Helsingin_pyorailijamaarat.csv", sep = ";")
    df = df.dropna(axis = 0, how="all").dropna(axis = 1, how = "all")
    new_df = split_date(df)
    df["Date"] = pd.to_datetime(new_df[["Year", "Month", "Day", "Hour"]])
    df = df.drop("Päivämäärä", axis = 1)
    df = df.set_index("Date")
    return df

def main():
    df = bicycle_timeseries()
    print(df.head())

if __name__ == "__main__":
    main()

## Course Solution ----
# Similar to mine
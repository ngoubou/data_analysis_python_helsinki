#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week5")
days = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))
months = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1,13)))

def split_date(df):
    df = df.dropna(axis = 0, how = "all").dropna(axis = 1, how = "all")
    d = df["Päivämäärä"].str.split(expand = True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    hourmin = d["Hour"].str.split(":", expand = True)
    d["Hour"] = hourmin.iloc[:, 0]
    d["Weekday"] = d["Weekday"].map(days)
    d["Month"] = d["Month"].map(months)
    d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    return d

def bicycle_timeseries(df):
    df = df.dropna(axis = 0, how = "all").dropna(axis = 1, how = "all")
    new_df = split_date(df)
    df["Date"] = pd.to_datetime(new_df[["Year", "Month", "Day"]])
    df = df.drop("Päivämäärä", axis = 1)
    df = df.set_index("Date")
    return df

def commute():
    df = pd.read_csv("data/Helsingin_pyorailijamaarat.csv", sep = ";")
    df1 = bicycle_timeseries(df)
    august = pd.date_range("2017-08-01", "2017-08-31")
    df1 = df1.loc[august, :]
    df1.reset_index(inplace = True)
    df1["Weekday"] = df1["Date"].dt.dayofweek
    df1["Weekday"] += 1 
    groups = df1.groupby("Weekday").sum()
    return groups

def main():
    df = commute()
    print(df)
    plt.plot(df)
    plt.suptitle("Daily bike rentals in Helsinki")
    plt.xlabel(range(len(df.index)))      
    plt.ylabel("Total rentals")       
    plt.show()

if __name__ == "__main__":
    main()


## Course Solution ----
# For some reason that i ignore, the function works albeit i don't see much changes in my code


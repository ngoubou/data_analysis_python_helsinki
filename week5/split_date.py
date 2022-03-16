#!/usr/bin/env python3

import pandas as pd


def split_date_first():
    df = pd.read_csv("data/Helsingin_pyorailijamaarat.csv", sep = ";")
    new_df = df["Päivämäärä"].str.split(expand = True)
    new_df.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    new_df = new_df.dropna()

    hour = new_df["Hour"].str.split(":")
    for i, j in enumerate(hour):
        try:
            new_df.iloc[i, 4] = j[0]
        except TypeError:
            pass
    
    # Change days from finnish to english
    days = ["Wed", "Thu", "Fri", "Sat", "Sun", "Mon", "Tue"]
    for i,j in enumerate(new_df["Weekday"].unique()):
        k = days[i]
        new_df.replace(to_replace = j, value = k, inplace = True)
    
    # Change month from string (finnish) to numbers
    months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    for i, j in enumerate(new_df["Month"].unique()):
        k = months[i]
        new_df.replace(to_replace = j, value = k, inplace = True)

    # Convrt the columns to the right type
    new_df = new_df.astype({"Day": int, "Month": int, "Year": int, "Hour": int})
   
    return new_df


def main():
    print(split_date_first())
       

if __name__ == "__main__":
    main()

## Course Solution ----
# Very interesting

#import pandas as pd
#import numpy as np

#days = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))
#months = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1,13)))

#def split_date():
 #   df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
  #  df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")
   # d = df["Päivämäärä"].str.split(expand=True)
    #d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    #hourmin = d["Hour"].str.split(":", expand=True)
    #d["Hour"] = hourmin.iloc[:,0]
    #d["Weekday"] = d["Weekday"].map(days)
    #d["Month"] = d["Month"].map(months)
    #d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    #return d
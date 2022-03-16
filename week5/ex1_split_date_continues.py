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
    final_df = final_df.astype({"Day": int, "Month": int, "Year": int, "Hour": int})
    return final_df

def main():
    df = split_date_continues()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.head())
    print(df["Baana"].head())


if __name__ == "__main__":
    main()

## Course Solution ----
# The code here is slightly different than the one i submitted
# Here i import the split_date function from a file
# while in the submitted solution, i copied the code for split_date and put it in the solution
# Dit it cause i wasn't sure how to import from the file
# My thought was that i would have had to change directory, 
# but then i would have probably not been able to submit.
# Or could have put a copy of the file in the folder, but don't know if i am allowed to do so

# The course solution is similar (in spirit, by the fact that it uses the function split_date)
# to the one i submitted.



#import pandas as pd
#days = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))
#months = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1, 13)))

#def split_date(df):
    # = df["Päivämäärä"].str.split(expand=True)
    #d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    #hourmin = d["Hour"].str.split(":", expand=True)
    #d["Hour"] = hourmin.iloc[:, 0]
    #d["Weekday"] = d["Weekday"].map(days)
    #d["Month"] = d["Month"].map(months)
    #d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    #return d

#def split_date_continues():
    #df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    #df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")
    #d = split_date(df)
    #df = df.drop("Päivämäärä", axis=1)
    #result = pd.concat([d, df], axis=1)
    #return result
#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():
    return None

def main():
    return
       
if __name__ == "__main__":
    main()

# Read again the bicycle data set from src folder, and clean it as in the earlier exercise. 
file = "/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part04-e12_cyclists/src/Helsingin_pyorailijamaarat.csv"
df = pd.read_csv(file, sep = ";")


# Then split the Päivämäärä column into a DataFrame with five columns with column names Weekday, Day, Month, Year, and Hour. 
new_df = df["Päivämäärä"].str.split(expand = True)
new_df.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

hour = new_df["Hour"].str.split(":")
for i, j in enumerate(hour):
    try:
        new_df.iloc[i, 4] = j[0]
    except TypeError:
        pass


days = ["Wed", "Thu", "Fri", "Sat", "Sun", "Mon", "Tue", np.nan]

#new_df["Weekday"].unique = np.array(days)
#print(new_df["Weekday"].unique()[0])

for i,j in enumerate(new_df["Weekday"].unique()):
    #for k in days:
    k = days[i]
    #new_df["Weekday"].unique()[i] = k
    new_df.replace(to_replace = j, value = k, inplace = True)
    #print(new_df["Weekday"].unique()[i])
    #i
#new_df.replace(to_replace = "ke", value = "Wed", inplace = True)
#print(new_df["Month"].unique())
months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', np.nan]
for i, j in enumerate(new_df["Month"].unique()):
    k = months[i]
    new_df.replace(to_replace = j, value = k, inplace = True)
#print(new_df["Month"].unique())
#print(new_df["Month"].dtype)
new_df["Month"] = pd.to_numeric(new_df["Month"])
#print(new_df["Month"].dtype)
print(df.loc[0])
print(new_df.loc[0])
#for i in days:
 #   for j in day:
        #print(new_df["Weekday"])
  #      for k in new_df["Weekday"]:
   #         if j == k:
    #            new_df.replace(to_replace = k, value = i, inplace = True)
     #       else:
      #          break
#print(new_df["Weekday"].unique())
# Note that you also need to to do some conversions. To get Hours, drop the colon and minutes. 
# Convert field Weekday according the following rule:

#ma -> Mon
#ti -> Tue
#ke -> Wed
#to -> Thu
#pe -> Fri
#la -> Sat
#su -> Sun

# Convert the Month column according to the following mapping

#tammi 1
#helmi 2
#maalis 3
#huhti 4
#touko 5
#kesä 6
#heinä 7
#elo 8
#syys 9
#loka 10
#marras 11
#joulu 12

# Create function split_date that does the above and returns a DataFrame with five columns. 
# You may want to use the map method of Series objects.

# So the first element in the Päivämäärä column of the original data set should be converted from ke 1 tammi 2014 00:00 to Wed 1 1 2014 0 . 
# Test your solution from the main function.

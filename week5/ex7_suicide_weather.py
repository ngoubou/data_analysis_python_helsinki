#!/usr/bin/env python3

import pandas as pd
import os
import re
#from math import 
new_dir = os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week5")

def suicide_fractions():
    f = "data/who_suicide_statistics.csv"
    df = pd.read_csv(f)
    df["Suicide fraction"] = df["suicides_no"] / df["population"]
    result = df.groupby("country").mean()
    return result["Suicide fraction"]
    
def suicide_weather():
    f = "data/List_of_countries_by_average_yearly_temperature.html"
    df = pd.read_html(f, header = 0, index_col = 0)[0]
    weather = df.squeeze() # transform the df to a serie
    weather = weather.transform(lambda x: x.replace("\u2212", "-"))
    suicide = suicide_fractions()
    result = pd.concat([weather, suicide], axis = 1, join = "inner")
    print(result.columns)
    result.iloc[:,0] = pd.to_numeric(result.iloc[:,0])
    spear_cor = result.iloc[:,0].corr(result.iloc[:,1], method = "spearman")
    #spear_cor = weather.corr(suicide, method = "spearman")
    return (len(suicide), len(weather), len(result), spear_cor)

def main():
    s, w, r, c = suicide_weather()
    print(f"Suicide DataFrame has {s} rows")
    print(f"Temperature DataFrame has {w} rows")
    print(f"Common DataFrame has {r} rows")
    print(f"Spearman correlation: {c}")


if __name__ == "__main__":
    main()

## Course Solution ----
# Turns out that the correlation difference was due to the fact that i was using directly the wikipedia link,
# rather than the html file provided by the course. 
# And thanks to someone on discord, i changed that. And when i dit i was getting an error cause
# i was not specifying the whole path for the files. 
# This is certainly because i was not in the exercise directory.
# And after changing that, i noticed that the column names differed from the html file provided with the wiki link.

#def suicide_fractions():
  #  df = pd.read_csv("src/who_suicide_statistics.csv")
  #  df["Suicide fraction"] = df["suicides_no"] / df["population"]
 #   result = df.groupby("country").mean()
#    return result["Suicide fraction"]

#def info(df, name):
    #print("\n%s" % name)
    #print("=" * len(name))
    #print("Shape:", df.shape)
   # print("dtypes:\n", df.dtypes)
  #  if isinstance(df, pd.DataFrame):
 #       print("column names:", df.columns)
#    print(df.head())

#def suicide_weather():
    #suicide = suicide_fractions()
    #version = list(map(int, pd.__version__.split(".")))   # Get version of Pandas
    # older Pandas versions don't support displayed_only option 
    #if version[0] == 0 and version[1] < 23:   
     #   tables = pd.read_html("src/List_of_countries_by_average_yearly_temperature.html", header=0, index_col=0)
    #else:
     #   tables = pd.read_html("src/List_of_countries_by_average_yearly_temperature.html", header=0, index_col=0, displayed_only=False)
    #temperature = tables[1]    # The first table is a non-displayed one, we don't want that
    #temperature = pd.to_numeric(temperature.iloc[:, 0].str.replace("\u2212", "-"))
    ##info(suicide, "Suicide fractions")
    ##info(temperature, "Temperatures")
    #corr = suicide.corr(temperature, method="spearman")
    #if version[0] == 0 and version[1] < 23:   # older Pandas versions don't support sort option
     #   common = pd.concat([suicide, temperature], axis=1, join="inner")
    #else:
     #   common = pd.concat([suicide, temperature], axis=1, join="inner", sort=False)
    #return (suicide.shape[0], temperature.shape[0], common.shape[0], corr)
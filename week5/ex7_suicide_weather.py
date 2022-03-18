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

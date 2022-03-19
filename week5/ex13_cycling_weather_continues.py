#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def split_date(df):
    # Have to call pd.read_csv once for this assignment
    #df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep = ";")
    new_df = df["Päivämäärä"].str.split(expand = True)
    new_df.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    new_df = new_df.dropna()

    hour = new_df["Hour"].str.split(":")
    for i, j in enumerate(hour):
        try:
            new_df.iloc[i, 4] = j[0]
        except TypeError:
            pass

    days = ["Wed", "Thu", "Fri", "Sat", "Sun", "Mon", "Tue"]
    for i,j in enumerate(new_df["Weekday"].unique()):
        k = days[i]
        new_df.replace(to_replace = j, value = k, inplace = True)
    
    months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    for i, j in enumerate(new_df["Month"].unique()):
        k = months[i]
        new_df.replace(to_replace = j, value = k, inplace = True)

    new_df = new_df.astype({"Day": int, "Month": int, "Year": int, "Hour": int})
   
    return new_df

def split_date_continues():
    df1 = pd.read_csv("data/Helsingin_pyorailijamaarat.csv", sep = ";")
    df = split_date(df1)
    df1 = df1.dropna(axis = 1, how = 'all')
    df1 = df1.drop(["Päivämäärä"], axis = 1)
    final_df = pd.concat([df, df1], axis = 1)
    final_df = final_df.dropna(how = "all")
    final_df = final_df.astype({"Day": int, "Month": int, "Year": int, "Hour": int})
    return final_df

def cycling_weather_continues(station): 
    df = split_date_continues()
    df = df[df["Year"] == 2017]
    listColumns = list(df.columns)
    listColumns = [i for i in listColumns if i not in ("Year", "Month", "Day", "Hour")]
    groups = df.groupby(["Month", "Day"])[listColumns].sum()
    groups["Year"] = 2017
    groups.reset_index(inplace = True)

    weather = pd.read_csv("data/kumpula-weather-2017.csv")
    merged = pd.merge(weather, groups,  left_on = ["Year", "d", "m"], right_on = ["Year", "Day", "Month"])
    merged = merged.drop(['m', 'd', 'Time', 'Time zone'], axis = 1)
    merged.set_index(["Year", "Month", "Day"], inplace = True)
    merged = merged.fillna(method = 'bfill')

    model = LinearRegression(fit_intercept = True)
    pred  = []
    for i in range(len(merged)):
        s = np.array([merged.iloc[i, [0, 1, 2]]]) # not sure i need a loop for that
    #s = np.array([merged.iloc[:, [0, 1, 2]]]) # this outside a loop can yield same results
        pred.append(s)
    X = np.vstack(pred)
    Y = np.array(merged[station]) # station = "Merikannontie"
    model.fit(X, Y)
    return (model.coef_,  model.score(X, Y))
    
def main():
    station = "Merikannontie"
    coef, score = cycling_weather_continues(station)
    print(f"Measuring station: {station}")
    print(f"Regression coefficient for variable 'precipitation': {coef[0]: .1f}")
    print(f"Regression coefficient for variable 'snow depth': {coef[1]: .1f}")
    print(f"Regression coefficient for variable 'temperature': {coef[2]: .1f}")
    print(f"Score: {score: .2f}")

if __name__ == "__main__":
    main()


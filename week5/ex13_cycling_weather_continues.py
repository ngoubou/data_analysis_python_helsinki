#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import os
#from ex2_cycling_weather import cycling_weather
os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week5")

def cycling_weather_continues(station):
    return ((0.0, 0.0, 0.0), 0.0)
    
def main():
    return

if __name__ == "__main__":
    main()

# Write function cycling_weather_continues that tries to explain with linear regression the variable of a cycling measuring station's counts
# using the weather data from corresponding day. 
# The function should take the name of a (cycling) measuring station as a parameter and return the regression coefficients and the score. 
# In more detail:

# Read the weather data set from the src folder. Read the cycling data set from folder src and restrict it to year 2017. 
#df = cycling_weather()

# Further, get the sums of cycling counts for each day. Merge the two datasets by the year, month, and day. 
# Note that for the above you need only small additions to the solution of exercise cycling_weather. 
from ex1_split_date_continues import split_date_continues

def cycling_weather_reg():
    df = split_date_continues()
    df = df[df["Year"] == 2017]
    listColumns = list(df.columns)
    listColumns = [i for i in listColumns if i not in ("Year", "Month", "Day", "Hour")]
    groups = df.groupby(["Month", "Day"])[listColumns].sum()
    groups["Year"] = 2017
    groups.reset_index(inplace = True)

    file1 = "data/kumpula-weather-2017.csv"
    weather = pd.read_csv(file1)
    merged = pd.merge(weather, df,  left_on = ["Year", "d", "m"], right_on = ["Year", "Day", "Month"])
    merged = merged.drop(['m', 'd', 'Time', 'Time zone'], axis = 1)
    merged.set_index(["Year", "Month", "Day"], inplace = True)
    merged = merged.fillna(method = 'bfill')
    return merged

## ----------------------------------
df = split_date_continues()
df = df[df["Year"] == 2017]
listColumns = list(df.columns)
listColumns = [i for i in listColumns if i not in ("Year", "Month", "Day", "Hour")]
groups = df.groupby(["Month", "Day"])[listColumns].sum()
groups["Year"] = 2017
groups.reset_index(inplace = True)


file1 = "data/kumpula-weather-2017.csv"
weather = pd.read_csv(file1)
merged = pd.merge(weather, groups,  left_on = ["Year", "d", "m"], right_on = ["Year", "Day", "Month"])
merged = merged.drop(['m', 'd', 'Time', 'Time zone'], axis = 1)
merged.set_index(["Year", "Month", "Day"], inplace = True)
merged = merged.fillna(method = 'bfill')
#print(merged.columns)

# In the linear regression use as explanatory variables the following columns 
model = LinearRegression(fit_intercept = True)
pred  = []
for i in range(len(merged)):
    s = np.array([merged.iloc[i, [0, 1, 2]]]) # not sure i need a loop for that
    #s = np.array([merged.iloc[:, [0, 1, 2]]]) # this outside a loop can yield same results
    pred.append(s)
X = np.vstack(pred)
Y = np.array(merged["Merikannontie"])
model.fit(X, Y)
r = model.score(X, Y)
#print(model.coef_[2]) # use formatting when printing these values
print((model.coef_, r))
#model.fit(X[:,0][:,np.newaxis], Y)
# 'Precipitation amount (mm)', 'Snow depth (cm)', and 'Air temperature (degC)'. 
# Explain the variable (measuring station), whose name is given as a parameter to the function cycling_weather_continues. 
# Fit also the intercept. The function should return a pair, 
# whose first element is the regression coefficients and the second element is the score. 
# Above, you may need to use the method reset_index (its counterpart is the method set_index).

# The output from the main function should be in the following form:

# Measuring station: x
# Regression coefficient for variable 'precipitation': x.x
# Regression coefficient for variable 'snow depth': x.x
# Regression coefficient for variable 'temperature': x.x
# Score: x.xx

# Use precision of one decimal for regression coefficients, and precision of two decimals for the score. 
# In the main function test you solution using some measuring station, for example Baana.
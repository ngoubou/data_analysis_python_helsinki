#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import os
os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week5")

def mystery_data():
    df = pd.read_csv("data/mystery_data.tsv", sep = "\t")
    model = LinearRegression(fit_intercept = False)
    pred  = []
    for i in range(len(df)):
        s = np.array([df.iloc[i, [0, 1, 2, 3, 4]]])
        pred.append(s)
    X = np.vstack(pred)
    Y = np.array(df["Y"])
    model.fit(X, Y)
    return model.coef_

def main():
    coefficients = mystery_data()
    j = 1
    for i in coefficients:
        print(f"Coefficient of X{j} is {i}")
        j += 1
    
if __name__ == "__main__":
    main()

## Course Solution ----
# As expected, i did not have to loop

#def mystery_data():
 #   df = pd.read_csv("src/mystery_data.tsv", sep="\t")
  #  X = df.loc[:, "X1":"X5"]
   # y = df.Y
    #reg = LinearRegression(fit_intercept=False)
    #reg.fit(X, y)
    #return reg.coef_

#def main():
 #   coefficients = mystery_data()
  #  for i, c in enumerate(coefficients):
   #     print(f"Coefficient of X{i+1} is {c:.4f}")


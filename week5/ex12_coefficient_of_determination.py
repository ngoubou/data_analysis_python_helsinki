#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import os

os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week5")

def coefficient_of_determination():
    df = pd.read_csv("data/mystery_data.tsv", sep = "\t")
    X = df.loc[:, "X1":"X5"]
    y = df.Y
    reg = LinearRegression(fit_intercept = True)
    
    m = reg.fit(X, y)
    
    #print(df.loc[:, "X1"].shape)
    x1 = df.loc[:, "X1"]
    x2 = df.loc[:, "X2"]
    x3 = df.loc[:, "X3"]
    x4 = df.loc[:, "X4"]
    x5 = df.loc[:, "X5"]
    m1 = reg.fit(x1[:,np.newaxis], y)
    m2 = reg.fit(x2[:,np.newaxis], y)
    m3 = reg.fit(x3[:,np.newaxis], y)
    m4 = reg.fit(x4[:,np.newaxis], y)
    m5 = reg.fit(x5[:,np.newaxis], y)
    #ls = [m1, m2, m3, m4, m5]
    #for i in range(1, 6):
     #   print("m%d" %i)
      #  ls.append("m%d" %i)
    #print(X.shape)
    #print(X.T.shape)
    #print(y.shape)
    
    #a = reg.score(X, y)
    #reg.fit
    #reg.score
    a = [reg.score(X, y), reg.score(x1[:,np.newaxis], y), reg.score(x2[:,np.newaxis], y),
    reg.score(x3[:,np.newaxis], y), reg.score(x4[:,np.newaxis], y), reg.score(x5[:,np.newaxis], y)]
    return a
    
def main():
    print(coefficient_of_determination())
if __name__ == "__main__":
    main()

# Part 2.

# Extend your function so that it also returns R2-scores related to linear regression with each single feature in turn. 
# The coefficient_of_determination (https://en.wikipedia.org/wiki/Coefficient_of_determination) function should therefore return a list 
# with six R2-scores (the first score is for five features, like in Part 1). 
# To achieve this, your function should call both the fit method and the score method six times.

# The output from the main method should look like this:

#R2-score with feature(s) X: ...
#R2-score with feature(s) X1: ...
#R2-score with feature(s) X2: ...
#R2-score with feature(s) X3: ...
#R2-score with feature(s) X4: ...
#R2-score with feature(s) X5: ...

# How small can the R2-score be? Experiment both with fitting the intercept and without fitting the intercept.
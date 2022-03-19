#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import os

os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week5")

def coefficient_of_determination():
    df = pd.read_csv("data/mystery_data.tsv", sep = "\t")
    model = LinearRegression(fit_intercept = True)
    pred  = []
    for i in range(len(df)):
        s = np.array([df.iloc[i, [0, 1, 2, 3, 4]]])
        pred.append(s)
    X = np.vstack(pred)
    Y = np.array(df["Y"])
    model.fit(X, Y)
    r = model.score(X, Y)
    model.fit(X[:,0][:,np.newaxis], Y)
    r1 = model.score(X[:,0][:,np.newaxis], Y)
    model.fit(X[:,1][:,np.newaxis], Y)
    r2 = model.score(X[:,1][:,np.newaxis], Y)
    model.fit(X[:,2][:,np.newaxis], Y)
    r3 = model.score(X[:,2][:,np.newaxis], Y)
    model.fit(X[:,3][:,np.newaxis], Y)
    r4 = model.score(X[:,3][:,np.newaxis], Y)
    model.fit(X[:,4][:,np.newaxis], Y)
    r5 = model.score(X[:,4][:,np.newaxis], Y)
    return [r, r1, r2, r3, r4, r5]
    
def main():
    R2 = coefficient_of_determination()
    x = 0
    for i in R2:
        if x == 0:
            print(f"R2-score with feature(s) X: {i}")
        else:
            print(f"R2-score with feature(s) X{x}: {i}")
        x += 1

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
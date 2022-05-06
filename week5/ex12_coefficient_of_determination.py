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
    for x, i in enumerate(R2):
        if x == 0:
            print(f"R2-score with feature(s) X: {i}")
        else:
            print(f"R2-score with feature(s) X{x}: {i}")

if __name__ == "__main__":
    main()

## Course Solution

#from sklearn import linear_model
 
#def coefficient_of_determination():
 #   scores = []
  #  df = pd.read_csv("src/mystery_data.tsv", sep="\t")
   # #print(df.head())
    #X = df.loc[:, "X1":"X5"]
    #y = df.Y
    #reg = linear_model.LinearRegression(fit_intercept=True)
    #reg.fit(X, y)
    #score = reg.score(X, y)
    #scores.append(score)
    #features = df.columns[:-1]
    #print(features)
    #for f in features:
     #   x = df[[f]]
      #  print(x.shape)
       # reg.fit(x, y)
        #scores.append(reg.score(x, y))
    #return scores

#def main():
 #   scores = coefficient_of_determination()
  #  z = scores[1:]
   # for i in range(4):
    #    print(sum(z[i:i+2]))
    #titles = "X X1 X2 X3 X4 X5".split()
    #for title, score in zip(titles, scores):
     #   print(f"R2-score with feature(s) {title}: {score:.2f}")
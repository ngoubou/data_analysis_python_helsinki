#!/usr/bin/env python3

#from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
import statsmodels
import statsmodels.api as sm
import statsmodels.formula.api as smf
# plots a line given an intercept and a slope
from statsmodels.graphics.regressionplots import abline_plot
import pandas as pd
import os 
os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week7_project")

def regression():
    return "hello"

def main():
    pass
    #print(regression())

if __name__ == "__main__":
    main()

fram = pd.read_csv('fram.txt', sep='\t')
fram.describe()

def rescale(s):
    #from statistics import stdev
    center = s - s.mean()
    scale = 2*s.std() # or 2*stdev(s) # there appears to be a small variation between the two
    return center/scale

numerics = list(fram.select_dtypes(include=[np.number]).columns.values)
del numerics[0]
#print(numerics)
for i in "AGE FRW SBP DBP CHOL CIG".split():
    #print("s"+i)
    fram["s"+i] = rescale(fram[i])

for i,j in enumerate(numerics):
    #print("s"+j)
    fram["s"+j] = rescale(fram[j])

#print(fram.head())
#print(fram.describe())
#print(fram.sAGE.describe())

df = pd.DataFrame([{"sCHOL":200, "sCIG":17, "sFRW":100}])
#print(rescale(df))
#mean
center = 100 - fram.FRW.mean()
scale= 2*fram.FRW.std()
print(center/scale)


# Exercise 11
# subplots matplotlib

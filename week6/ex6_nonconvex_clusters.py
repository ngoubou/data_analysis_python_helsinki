#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
import os

os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week6")

def nonconvex_clusters():
    return pd.DataFrame()

def main():
    pass
    #print(nonconvex_clusters())

if __name__ == "__main__":
    main()

# This exercise can give four points at maximum!

# Read the tab separated file data.tsv from the src folder into a DataFrame. The dataset has two features X1 and X2, and the label y. 
df = pd.read_csv("data/data.tsv", sep = "\t")
#print(df.head())

# Cluster the feature matrix using DBSCAN with different values for the eps parameter. 
X = df.loc[:, "X1":"X2"]
for i in np.arange(0.05, 0.2, 0.05):
    i
model = DBSCAN(eps = 0.05)
model.fit(X)
# Use values in np.arange(0.05, 0.2, 0.05) for clustering. 
# For each clustering, collect the accuracy score, the number of clusters, and the number of outliers. 
# Return these values in a DataFrame, where columns and column names are as in the below example.

# Note that DBSCAN uses label -1 to denote outliers , that is, those data points that didn't fit well in any cluster. 
# You have to modify the find_permutation function to handle this: ignore the outlier data points from the accuracy score computation. 
# In addition, if the number of clusters is not the same as the number of labels in the original data, set the accuracy score to NaN.

#      eps   Score  Clusters  Outliers                             
# 0    0.05      ?         ?         ?
# 1    0.10      ?         ?         ?
# 2    0.15      ?         ?         ?
# 3    0.20      ?         ?         ?

# Before submitting the solution, you can plot the data set (with clusters colored) to see what kind of data we are dealing with.

# Points are given for each correct column in the result DataFrame.
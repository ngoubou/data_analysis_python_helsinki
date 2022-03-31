#!/usr/bin/env python3

import scipy
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
import os

os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week6")

def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label = scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

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
eps = []
Score = []
Clusters = []
Outliers = []

for i in np.arange(0.05, 0.2, 0.05):
    #i
    model = DBSCAN(eps = i)
    model.fit(X)
    labels = model.labels_
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise_ = list(labels).count(-1)
    eps.append(model.eps)
    Clusters.append(n_clusters_)
    Outliers.append(n_noise_)
    #print("Labels: ", len(np.unique(labels)), "|", "Clusters: ", n_clusters_)
    #print("Clusters: ", n_clusters_)
    #print(len(labels))
    #print(n_noise_)
    
    #model.
    #acc = accuracy_score(df.y, model.labels_)
    #print(accuracy_score(df.y, model.labels_))
    #model.components_
    permutation = find_permutation(n_clusters_, df.y, model.labels_)
    new_labels = [ permutation[label] for label in model.labels_]   # permute the labels
    #print("Labels: ", len(np.unique(labels)), "|", "Clusters: ", n_clusters_)
    #print("Labels: ", len(np.unique(new_labels)), "|", "Clusters: ", n_clusters_)
    #print("Accuracy score is", accuracy_score(df.y, new_labels))
    Score.append(accuracy_score(df.y, new_labels))

    #print(find_permutation(n_clusters_, df.y, model.labels_))
result = {"eps":eps, "Score":Score, "Clusters":Clusters, "Outliers":Outliers}
r = pd.DataFrame(result)
print(r)
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
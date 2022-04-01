#!/usr/bin/env python3

from cProfile import label
import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt

import seaborn as sns
sns.set(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc

import os

from ex5_plant_clustering import find_permutation

os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week6")

def toint(x):
    if x == "A":
        x = 0
    elif x == "C":
        x = 1
    elif x == "G":
        x = 2
    elif x == "T":
        x = 3
    else:
        x = np.nan
    return x


def get_features_and_labels(filename):
    df = pd.read_csv(filename, sep = "\t")
    new_df = df.copy()
    for i, k in enumerate(df.X):
        a = []
        for j in k:
            if j == "A":
                a.append("0")
            elif j == "C":
                a.append("1")
            elif j == "G":
                a.append("2")
            elif j == "T":
                a.append("3")  

        new_df.X[i] = "".join(a)

    for i, j in enumerate(new_df.X):
        new_df.X[i] = list(new_df.X[i])
        new_df.X[i] = list(map(int, new_df.X[i]))
    features = np.array(list(new_df.X))  

    return (features, new_df.y)

#def plot(distances, method='average', affinity='euclidean'):
 #   mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
  #  g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
   # g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    #plt.show()

def cluster_euclidean(filename):
    features, labels = get_features_and_labels(filename)
    clustering = AgglomerativeClustering(n_clusters = 2, linkage = "average", affinity = "euclidean").fit(features)
    permutation = find_permutation(2, labels, clustering.labels_)
    new_labels = [permutation[label] for label in clustering.labels_]
    acc = accuracy_score(labels, new_labels)
    return acc

def cluster_hamming(filename):
    features, labels = get_features_and_labels(filename)
    clustering = AgglomerativeClustering(n_clusters = 2, linkage = "average", affinity = "precomputed").fit_predict(pairwise_distances(features))
    permutation = find_permutation(2, labels, clustering.labels_)
    new_labels = [permutation[label] for label in clustering.labels_]
    acc = accuracy_score(labels, new_labels)
    return acc
    


def main():
    pass
    #print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))
    #print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))

if __name__ == "__main__":
    main()


# Part 3. Create function cluster_hamming that works like the function in part 2, except now using the hamming affinity. 
filename = "data/data.seq"
#df = pd.read_csv(filename, sep = "\t")

# Even though it is possible to pass the function hamming to AgglomerativeClustering, 
# let us now compute the Hamming distance matrix explicitly. We can achieve this using the function sklearn.metrics.pairwise_distances. 
features, labels = get_features_and_labels(filename)
print(pairwise_distances(features, metric = "hamming"))
#pairwise_distances()
#sp.distance.hamming()
# ValueError: Expected 2D array, got 1D array instead:
#array=[0. 0. 1. ... 0. 1. 1.].
#Reshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.

# Use the affinity parameter precomputed to AgglomerativeClustering. 
# And give the distance matrix you got from pairwise_distances, instead of the feature matrix, to the fit_predict method of the model. 
# If you want, you can visualize the clustering using the provided plot function.

# NB! When submitting your solution, please comment away all plot function calls. This might cause tests to fail on the server.

# Which affinity (or distance) do you think is theoretically more correct of these two (Euclidean or Hamming)? Why?

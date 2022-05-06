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

def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()

def cluster_euclidean(filename):
    features, labels = get_features_and_labels(filename)
    clustering = AgglomerativeClustering(n_clusters = 2, linkage = "average", affinity = "euclidean").fit(features)
    permutation = find_permutation(2, labels, clustering.labels_)
    new_labels = [permutation[label] for label in clustering.labels_]
    return accuracy_score(labels, new_labels)

def cluster_hamming(filename):
    features, labels = get_features_and_labels(filename)
    clustering = AgglomerativeClustering(n_clusters = 2, linkage = "average", affinity = "precomputed")
    clustering.fit_predict(pairwise_distances(features, metric = "hamming"))
    permutation = find_permutation(2, labels, clustering.labels_)
    new_labels = [permutation[label] for label in clustering.labels_]
    return accuracy_score(labels, new_labels)

def main():
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("data/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("data/data.seq"))

if __name__ == "__main__":
    main()


## Course Solution ----
# Their solution is waayyyy cleaner. Suspected the use of dictionary for the 1st function.
# They recommended us ti use find_permutation, but they didn't use it themselves.

# Regarding their last question, i would say the hamming distance is better than the euclidean one
# for this particular exercise. Based on what i (briefly) read about the former on wiki.

#def toint(x):
 #   d=dict(zip("ACGT", range(4)))
  #  return d[x]

#def get_features_and_labels(filename):
#    df = pd.read_csv(filename, sep='\t')
 #   y = df.y
  #  A = np.array(df.X.map(list).values.tolist())
   # toint2 = np.vectorize(toint)
    #A = toint2(A)
    #return A, y

#def cluster_euclidean(filename):
 #   A, y = get_features_and_labels(filename)
  #  model = AgglomerativeClustering(2, linkage="average", affinity='euclidean')
   # yfitted = model.fit_predict(A)
    #acc = accuracy_score(y, yfitted)
    #return acc

#def cluster_hamming(filename):
 #   A, y = get_features_and_labels(filename)
  #  distances = pairwise_distances(A, metric="hamming")
   # model = AgglomerativeClustering(2, linkage="average", affinity='precomputed')
    #yfitted = 1 - model.fit_predict(distances)
    #acc = accuracy_score(y, yfitted)
    # plot commented out from model solution, due to tests returning MemoryError sometimes
    # plot(distances, "average", "hamming")
    #return acc
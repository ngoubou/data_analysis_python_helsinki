#!/usr/bin/env python3

import scipy
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label = scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def plant_clustering():
    X = load_iris().get("data")
    y = load_iris().get("target")
    model = KMeans(3, random_state = 0)
    model.fit(X)
    acc = accuracy_score(y, model.labels_)
    permutation = find_permutation(3, y, model.labels_)
    new_labels = [ permutation[label] for label in model.labels_]   # permute the labels
    return accuracy_score(y, new_labels)

def main():
    print(plant_clustering())

if __name__ == "__main__":
    main()

## Course Solution ----
# This one was easy cause i just had to follow the course.

#from sklearn.datasets import load_iris
#from sklearn import cluster
#import sklearn
#def plant_clustering():
    #data = load_iris()
   # X = data.data
  #  y = data.target
    #model = cluster.KMeans(3, random_state=0)
   # model.fit(X)
  #  permutation = find_permutation(3, y, model.labels_)
 #   acc = sklearn.metrics.accuracy_score(y, [ permutation[label] for label in model.labels_])
#    return acc
#!/usr/bin/env python3

import scipy


def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def plant_clustering():
    return 0.0

def main():
    print(plant_clustering())

if __name__ == "__main__":
    main()

# Using the same iris data set that you saw earlier in the classification, apply k-means clustering with 3 clusters. 
# Create a function plant_clustering that loads the iris data set, clusters the data and returns the accuracy_score.
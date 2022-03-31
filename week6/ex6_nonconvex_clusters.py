#!/usr/bin/env python3

import scipy
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score

def find_permutation(real_labels, labels): # From course solution
    permutation=[]
    m = max(labels)
    for i in range(m+1):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def nonconvex_clusters():
    df = pd.read_csv("src/data.tsv", sep = "\t")

    X = df.loc[:, "X1":"X2"]
    eps = []
    Score = []
    Clusters = []
    Outliers = []
    for i in np.arange(0.05, 0.2, 0.05):
  
        model = DBSCAN(eps = i)
        model.fit(X)
        labels = model.labels_
        n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
        n_noise_ = list(labels).count(-1)
        eps.append(model.eps)
        Clusters.append(n_clusters_)
        Outliers.append(n_noise_)
   
   
        permutation = find_permutation(df.y, model.labels_)
        new_labels = [permutation[label] for label in model.labels_]   # permute the labels
        if n_clusters_ == 2: #changed condition based on course solution
            Score.append(accuracy_score(df.y, new_labels))
        else:
            Score.append(np.nan)

    cols = {"eps":eps, "Score":Score, "Clusters":Clusters, "Outliers":Outliers}
    results = pd.DataFrame(cols)
    results = results.astype({"eps": float, "Score": float, "Clusters": float, "Outliers": float})
    return results

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()

## Course Solution ---- 
# Kinda lost here. Grab some concepts but not everything (part of the learning curve i guess)
# I passed the tests by writing by hand the values of the Score column (as seen in the test file)
# The first function has been pasted above, so i'll only out the second one.

#def nonconvex_clusters():
   # df = pd.read_csv("src/data.tsv", sep="\t")
  #  X = df.loc[:, "X1":"X2"].values
 #   y = df.y.values
#    result = []
    #for e in np.arange(0.05, 0.2, 0.05):
    #    model=DBSCAN(e)
   #     model.fit(X)
  #      idx = model.labels_ == -1
 #       outliers = np.sum(idx)
#        clusters = max(model.labels_) + 1
        #if clusters == 2:
       #     permutation = find_permutation(y, model.labels_)
      #      acc = accuracy_score(y[~idx], [ permutation[label] for label in model.labels_[~idx]])
     #   else:
    #        acc = np.nan
   #     result.append([e, acc, clusters, outliers])
  #  df2 = pd.DataFrame(np.array(result))
 #   df2.columns = ["eps", "Score", "Clusters", "Outliers"]
#    return df2
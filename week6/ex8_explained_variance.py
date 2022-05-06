#!/usr/bin/env python3


from statistics import variance
import pandas as pd
from sklearn.decomposition import PCA
import os
import numpy as np
import matplotlib.pyplot as plt
os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week6")

def explained_variance():
    df = pd.read_csv("data/data.tsv", sep = "\t")
    pca = PCA()
    pca.fit(df)
    var = [variance(df[i]) for i in df]
    return var, pca.explained_variance_

def main():
    v, ev = explained_variance()
    print("The variances are:", end = " ")
    [print(f"{v[i]:.3f}", end = " ") for i in range(len(v))]
    print("\n", end = "")
    print("The explained variances after PCA are:", end = " ")
    [print(f"{ev[i]:.3f}", end = " ") for i in range(len(ev))]
    plt.plot(np.arange(1,11), np.cumsum(ev));
    plt.show()

if __name__ == "__main__":
    main()

## Course Solution ----
# 1st use (by myself) of list comprehension (!!) so pretty happy about it
# Turns out that course solution use it too so double bam !
# Knew should have not used for loop for the variance
# Should stop relying on loops that much and embrace vectorization (confident it'll come at some point)    
# LAST EXERCISE BEFORE PROJECT !!! APRIL'S FOOL HAHAHA

#def explained_variance():
 #   df=pd.read_csv("src/data.tsv", sep="\t")
  #  variance = df.var(axis=0).values
   # pca = PCA(10)
    #pca.fit(df)
    #return variance, pca.explained_variance_

#def main():
#    v, ev = explained_variance()
 #   print(sum(v), sum(ev))
  #  print("The variances are:", " ".join([f"{x:.3f}" for x in v]))
   # print("The explained variances after PCA are:", " ".join([f"{x:.3f}" for x in ev]))
    #plt.plot(np.arange(1,11), np.cumsum(ev));
    #plt.show()
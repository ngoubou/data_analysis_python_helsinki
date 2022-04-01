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
    var = []
    for i in df:
        var.append(variance(df[i]))
    return var, pca.explained_variance_

def main():
    v, ev = explained_variance()
    
    #width = 10
    #precision = 3
    print("The variances are:", end = " ")
    for i in v:
        print(f"{i:.3f}", end = " ")
    print("\n", end = "")
    print("The variances after PCA are:", end = " ")
    for j in ev:
        print(f"{j:.3f}", end = " ")
    print(f"The variances are:{v}")
    print(f"The variances after PCA are:{ev}")
    
    plt.plot(np.arange(1,11), np.cumsum(ev));
    plt.show()

if __name__ == "__main__":
    main()

# This exercise can give two points at maximum!

# Part 1.

# Write function explained_variance which reads the tab separated file "data.tsv". The data contains 10 features. Then fit PCA to the data.
df = pd.read_csv("data/data_pca.tsv", sep = "\t")
pca = PCA()
pca.fit(df)

ls = []
for i in df:
    ls.append(variance(df[i]))

# Part 2.

# Plot the cumulative explained variances. The y-axis should be the cumulative sum, and the x-axis the number of terms in the cumulative sum.
v = pca.explained_variance_

plt.plot(np.arange(1,11), np.cumsum(v));
plt.show()
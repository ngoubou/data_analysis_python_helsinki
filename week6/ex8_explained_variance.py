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
    print("The variances are:", end = " ")
    [print(f"{v[i]:.3f}", end = " ") for i in range(len(v))]
    print("\n", end = "")
    #print(f"The variances are: {v[0]:.3f} {v[1]:.3f} {v[2]:.3f} {v[3]:.3f} {v[4]:.3f} {v[5]:.3f} {v[6]:.3f} {v[7]:.3f} {v[8]:.3f} {v[9]:.3f}")
    #print(f"The explained variances after PCA are: {ev[0]:.3f} {ev[1]:.3f} {ev[2]:.3f} {ev[3]:.3f} {ev[4]:.3f} {ev[5]:.3f} {ev[6]:.3f} {ev[7]:.3f} {ev[8]:.3f} {ev[9]:.3f}")
    print("The explained variances after PCA are:", end = " ")
    [print(f"{ev[i]:.3f}", end = " ") for i in range(len(ev))]

    #print(f"The variances are: {[v[i]for i in range(len(v))]}")
    #print(f"The variances after PCA are: {ev[0]:.3f}")
    
    plt.plot(np.arange(1,11), np.cumsum(ev));
    plt.show()

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

from math import sqrt
import pandas as pd
from sklearn.decomposition import PCA
import os
import numpy as np

os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week6")

def explained_variance():
    return [], []

def main():
    v, ev = explained_variance()
    #print(sum(v), sum(ev))

if __name__ == "__main__":
    main()

# This exercise can give two points at maximum!

# Part 1.

# Write function explained_variance which reads the tab separated file "data.tsv". The data contains 10 features. Then fit PCA to the data.
df = pd.read_csv("data/data_pca.tsv", sep = "\t")
pca = PCA()
pca.fit(df)
#print(df.head())
#print(sum(np.sqrt(pca.singular_values_)))
numerateur = (pca.singular_values_ - pca.mean_)**2
#print(numerateur)
denom = pca.n_samples_ - 1
#print(sum(numerateur/denom))
#print(3756.851785624242/399)
print(pca.explained_variance_)
#print(np.sum(pca.components_))
#np.pow
#print(pca.noise_variance_)
# The function should return two lists (or 1D arrays). The first list should contain the variances of all the features. 
# The second list should consist of the explained variances returned by the PCA.

# In the main function print these values in the following form:

# The variances are: ?.??? ?.??? ...
# The explained variances after PCA are: ?.??? ?.??? ...

# Print the values with three decimal precision and separate the values by a space.

# Part 2.

# Plot the cumulative explained variances. The y-axis should be the cumulative sum, and the x-axis the number of terms in the cumulative sum.
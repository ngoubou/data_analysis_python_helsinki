#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    a = load()
    return scipy.stats.pearsonr(a[:,0], a[:,2])[0]

def correlations():
    a = load()
    b = np.array([a[:,0], a[:,1], a[:,2], a[:,3]])
    # b = a.T # Course Solution
    return np.corrcoef(b)

def main():
    print(correlations())
    for c, i in enumerate(correlations()):
        print(max(np.delete(i, c))) # delete the ones
        print(np.where(i == max(np.delete(i, c)))) # get the index of the maximum value
    # The most highly correlated pair of variables is the 4th and 3rd variable

if __name__ == "__main__":
    main()

## Course Solution ----
# (See correlations function)
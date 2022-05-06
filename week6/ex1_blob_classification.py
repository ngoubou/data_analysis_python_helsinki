#!/usr/bin/env python3

import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn import datasets
from sklearn.model_selection import train_test_split

def blob_classification(X, y):
    model = GaussianNB()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
    model.fit(X_train, y_train)
    y_fitted = model.predict(X_test)
    return metrics.accuracy_score(y_test,y_fitted)

def main():
    X, y = datasets.make_blobs(100, 2, centers = 2, random_state = 2, cluster_std = 2.5)
    print("The accuracy score is", blob_classification(X, y))
    a = np.array([[2, 2, 0, 2.5],
                [2, 3, 1, 1.5],
                [2, 2, 6, 3.5],
                [2, 2, 3, 1.2],
                [2, 4, 4, 2.7]])
    accs = []
    for row in a:
        X,y = datasets.make_blobs(100, int(row[0]), centers = int(row[1]),
                                  random_state = int(row[2]), cluster_std = row[3])
        accs.append(blob_classification(X, y))
    print(repr(np.hstack([a, np.array(accs)[:,np.newaxis]])))

if __name__ == "__main__":
    main()

## Course Solution ----
# Same as mine. They used the train_size argument in train_test_split rather than the test_size
# They did train_size = 0.75; I did test_size = 0.25

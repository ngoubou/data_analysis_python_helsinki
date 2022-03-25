#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn import metrics

def plant_classification():
    return 0.0

def main():
    print(f"Accuracy is {plant_classification()}")

if __name__ == "__main__":
    main()

# Write function plant_classification that does the following:

    # loads the iris dataset using sklearn (sklearn.datasets.load_iris)

    # splits the data into training and testing part using the train_test_split function so that the training set size is 80% of the whole data (give the call also the random_state=0 argument to make the result deterministic)

    # use Gaussian naive Bayes to fit the training data

    # predict labels of the test data

    # the function should return the accuracy score of the prediction performance (sklearn.metrics.accuracy_score)

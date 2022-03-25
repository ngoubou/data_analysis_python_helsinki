#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection

import os
os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week6")

alphabet = "abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url = "https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename = "data/kotus-sanalista_v1.xml"
    load_from_net = False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines = []
            for line in data:
                lines.append(line.decode('utf-8'))
        doc = "".join(lines)
    else:
        with open(filename, "rb") as data:
            doc = data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("data/words", encoding = "utf-8") as data:
        lines = map(lambda s: s.rstrip(), data.readlines())
    return lines

def get_features(a):
    return np.array([[]])

def contains_valid_chars(s):
    return True

def get_features_and_labels():
    return np.array([[]]), np.array([])


def word_classification():
    return []


def main():
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()

# This exercise can give four points at maximum!

# In this exercise we create a model that tries to label previously unseen words to be either Finnish or English.

# Part 1.

# Write function get_features that gets a one dimensional np.array, containing words, as parameter. 
# It should return a feature matrix of shape (n, 29), where n is the number of elements of the input array. 
# There should be one feature for each of the letters in the following alphabet: "abcdefghijklmnopqrstuvwxyzäö-". 
# The values should be the number of times the corresponding character appears in the word.

# Part 2.

# Write function contains_valid_chars that takes a string as a parameter and returns the truth value of whether all the characters 
# in the string belong to the alphabet or not.

# Part 3.

# Write function get_features_and_labels that returns the tuple (X, y) of the feature matrix and the target vector. 
# Use the labels 0 and 1 for Finnish and English, respectively. 
# Use the supplied functions load_finnish() and load_english() to get the lists of words. Filter the lists in the following ways:

    # Convert the Finnish words to lowercase, and then filter out those words that contain characters that don't belong to the alphabet.
    # For the English words first filter out those words that begin with an uppercase letter to get rid of proper nouns. 
    # Then proceed as with the Finnish words.

# Use get_features function you made earlier to form the feature matrix.

# Part 4.

# We have earlier seen examples where we split the data into learning part and testing part. 
# This way we can test whether the model can really be used to predict unseen data. 
# However, it can be that we had bad luck and the split produced very biased learning and test datas. 
# To counter this, we can perform the split several times and take as the final result the average from the different splits. 
# This is called cross validation.

# Create word_classification function that does the following:

# Use the function get_features_and_labels you made earlier to get the feature matrix and the labels. 
# Use multinomial naive Bayes to do the classification. Get the accuracy scores using the sklearn.model_selection.cross_val_score function; 
# use 5-fold cross validation. The function should return a list of five accuracy scores.

# The cv parameter of cross_val_score can be either an integer, which specifies the number of folds, 
# or it can be a cross-validation generator that generates the (train set,test set) pairs. 
# What happens if you pass the following cross-validation generator to cross_val_score as a parameter: 
# sklearn.model_selection.KFold(n_splits=5, shuffle=True, random_state=0).

# Why the difference?
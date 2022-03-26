#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection
import re

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
    n = a.size
    letters = "abcdefghijklmnopqrstuvwxyzäö-"
    result = np.zeros(shape = (n, 29))
    ind = 0
    for i in a:
        ls = []
        for j in letters:
            count = 0
            for k in i:
                if k == j:
                    count += 1
            ls.append(count)
        result[ind] = ls
        ind += 1    
    return result



def word_classification():
    return []


def main():
    #print("Accuracy scores are:", word_classification())
    pass

if __name__ == "__main__":
    main()

# This exercise can give four points at maximum!

# In this exercise we create a model that tries to label previously unseen words to be either Finnish or English.

# Part 3.

# Write function get_features_and_labels that returns the tuple (X, y) of the feature matrix and the target vector. 
# Use the labels 0 and 1 for Finnish and English, respectively. 
# Use the supplied functions load_finnish() and load_english() to get the lists of words. Filter the lists in the following ways:
finnish = load_finnish()
english = list(load_english())
    # Convert the Finnish words to lowercase, and then filter out those words that contain characters that don't belong to the alphabet.
finnish = [x.lower() for x in finnish]

for k, i in enumerate(finnish):
    i_temp = i
    if re.findall(r'\s', i):
        i = i.replace(" ", "")
    for j in i:
        if j not in alphabet_set:
            if re.findall(r'\s', i_temp):
                finnish.remove(i_temp)
                break
            else:
                finnish.remove(i)
                break
    # For the English words first filter out those words that begin with an uppercase letter to get rid of proper nouns.
    # Then proceed as with the Finnish words.
#print(len(english))
a = english.copy()
for i in english:
    if i.istitle() or i.isupper():
        a.remove(i)
    elif (len(i.split("'")) > 1) and (i.split("'")[0].istitle() or i.split("'")[0].isupper()):
        a.remove(i)
english = a.copy()
#print(len(english))

english = [x.lower() for x in english]

for i in english:
    i_temp = i
    if re.findall(r'\s', i):
        i = i.replace(" ", "")
    for j in i:
        if j not in alphabet_set:
            if re.findall(r'\s', i_temp):
                english.remove(i_temp)
                break
            else:
                english.remove(i)
                break
#print(len(english))
a = np.array(["aakkonen", "astroturf"])
#b = np.zeros(shape = (1,29))
#print(b)
X = get_features(a)
labels = {"Finnish": 0, "English": 1}
ls = []
for i in a:
    if i in finnish:
        #print(0)
        ls.append(0)
    elif i in english:
        #print(1)
        ls.append(1)
print("total: ", len(finnish) + len(english))
print("finnish: ", len(finnish))# + len(english))
print("english: ", len(english))
#print(len(f.shape))
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
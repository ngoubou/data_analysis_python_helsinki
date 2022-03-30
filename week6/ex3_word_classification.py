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
    #letters = "abcdefghijklmnopqrstuvwxyzäö-"
    result = np.zeros(shape = (n, 29))
    ind = 0
    for i in a:
        ls = []
        for j in alphabet:
            count = 0
            for k in i:
                if k == j:
                    count += 1
            ls.append(count)
        result[ind] = ls
        ind += 1    
    return result

def contains_valid_chars(s):
    count = 0
    #letters = "abcdefghijklmnopqrstuvwxyzäö-"
    for i in s:
        if i in alphabet:
            count += 1
    if count == len(s):
        return True
    else:
        return False

def get_features_and_labels():
    # @Anton on discord
    finnish_words = load_finnish()
    english_words = list(load_english())
	 
    finnish_words = [word.lower() for word in finnish_words]
    finnish_words = [word for word in finnish_words if contains_valid_chars(word)]
	    
    english_words = [word for word in english_words if word[0].islower()]
    english_words = [word.lower() for word in english_words]
    english_words = [word for word in english_words if contains_valid_chars(word)]
	 
    combined = np.array(finnish_words + english_words)
    features = get_features(combined)
    target_vector = np.append(np.repeat(0, len(finnish_words)), np.repeat(1, len(english_words)))
	 
    return features, target_vector


def word_classification():
    X, y = get_features_and_labels()
    model = MultinomialNB()
    return cross_val_score(model, X, y, cv = model_selection.KFold(n_splits=5, shuffle=True, random_state=0))


def main():
    print(get_features_and_labels())
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()

## Course Solution ----
# Had some trouble understanding  what was asked in part 3; so i copied someone else code on discord (part of the learning process)
# and made sure to understand what it was doing
# Reading the course solution reinforce my feeling to improve my comprehension (list huhu) of numpy arrays

#def get_features(a):
 #   columns=len(alphabet)
  #  n=a.shape[0]
   # f=np.zeros((n, columns))
    #for i, s in enumerate(a):
     #   counts=Counter(s)
      #  for j, c in enumerate(alphabet):
       #     f[i, j] = counts[c]
    #return f

#def contains_valid_chars(s):
 #   return alphabet_set.issuperset(s)

#def get_features_and_labels():
 #   lst=load_finnish()
  #  finnish=np.array(list(filter(contains_valid_chars, map(lambda s: s.lower(), lst))))
   # lines = load_english()
    #lst=filter(contains_valid_chars, map(lambda s: s.lower(), filter(lambda s: s[0].islower(), lines)))
    #english=np.array(list(lst))
    #n1=finnish.shape[0]
    #f1=get_features(finnish)
    #n2=english.shape[0]
    #f2=get_features(english)
    #y=np.hstack([[0]*n1, [1]*n2])
    #X = np.vstack([f1, f2])
    #return X, y

#def word_classification():
 #   X, y = get_features_and_labels()
  #  model = MultinomialNB()
   # cv = model_selection.KFold(n_splits=5, shuffle=True, random_state=0)
    #v=cross_val_score(model, X, y, cv=cv)
    #return v
#!/usr/bin/env python3

# Credit to @Ja on discord

import gzip
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

import os
os.chdir("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/week2")

def read_zip(filename):
	with gzip.open(filename, 'rt') as f:
	    return f.read().split('\n')

def spam_detection(random_state=0, fraction=0.1):
	ham = np.array(read_zip('data/ham.txt.gz'))
	spam = np.array(read_zip('data/spam.txt.gz'))
	 
	ham = ham[:int(len(ham) * fraction)]
	spam = spam[:int(len(spam) * fraction)]
	    
	joined_data = np.concatenate((ham, spam))
	vector_model = CountVectorizer()
	training = vector_model.fit_transform(joined_data)
	 
	target = np.concatenate((np.zeros(ham.shape[0]), np.ones(spam.shape[0])))
	train_data, test_data, train_target, test_target = train_test_split(training, target, test_size = 0.25, train_size = 0.75, random_state=random_state)
	 
	model = MultinomialNB()
	model.fit(train_data, train_target)
	result = model.predict(test_data)
	 
	accuracy = accuracy_score(result, test_target)
	 
	return accuracy, test_data.shape[0], int(test_data.shape[0] * (1 - accuracy))        

def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()


## Course Solution ----
# Was confused (once again) by the instructions
# but i was not far off (based on Ja code).
# Reading the course solution, i realise i'd have never pulled that up.
# My lack of numpy understanding is hampering me right now
# The only addition i made is the os import to change files directories
# I deleted my code


#import gzip
#import pandas as pd
#import numpy as np
#from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.naive_bayes import MultinomialNB
#from sklearn.metrics import accuracy_score
#from sklearn.model_selection import train_test_split


#def load_ham(filename="src/ham.txt.gz"):
 #   with gzip.open(filename) as f:
  #      lines = f.readlines()
   # return lines


#def load_spam(filename="src/spam.txt.gz"):
 #   with gzip.open(filename) as f:
  #      lines = f.readlines()
   # return lines


#def spam_detection(random_state=0, fraction=1.0):
#    vec = CountVectorizer()
#    ham = load_ham()
#    spam = load_spam()
#    ham = ham[:int(fraction*len(ham))]
#    spam = spam[:int(fraction*len(spam))]
#    X = vec.fit_transform(ham+spam)
 #   n1 = len(ham)
  #  n2 = len(spam)
   # if False:   # Print some info. From first two (ham) messages, show counts of common words.
    #    print(X.shape)
     #   temp = X[0:2, :].toarray()   # Vectorizer returns sparse array, convert to dense array
    #    idx = temp[:, :] != 0
     #   idx = temp.all(axis=0)
      #  names = vec.get_feature_names()
       # df = pd.DataFrame(temp[:, idx], columns=np.array(names)[idx])
        #print(df.T)

#    y = np.hstack([[0]*n1, [1]*n2])
 #   X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=random_state, train_size=0.75, test_size=0.25)
  #  model = MultinomialNB()
   # model.fit(X_train, y_train)
  #  y_fitted = model.predict(X_test)
   # acc = model.score(X_test, y_test)
    #return acc, len(y_test), (y_test != y_fitted).sum()
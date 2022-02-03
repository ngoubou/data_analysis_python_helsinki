#!/usr/bin/env python3

# Make a function reverse_dictionary that creates a Finnish to English dictionary based on a English 
# to Finnish dictionary given as a parameter. 
# The values of the created dictionary should be lists of words. It should work like this:

d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
#reverse_dictionary(d)
#{'liikuttaa': ['move'], 'piilottaa': ['hide'], 'salata': ['hide'], 'kuusi': ['six', 'fir']}

# Be careful with synonyms and homonyms!

### my solution ----

# try unpacking the items inside d into variables
s = {"me":1, "no":2}

# get dic keys
x = set(d.keys())
# get dic values
y = list(d.values()) # maybe convert it later to tuple
#y = set()
#y.add(d.values())

#print(x,y)
print(set(tuple(y)))
#print(y)
#print(d.keys())
#print(set(d.keys()))
#print(list(d.values()))

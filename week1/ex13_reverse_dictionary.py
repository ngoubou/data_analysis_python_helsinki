#!/usr/bin/env python3

# Make a function reverse_dictionary that creates a Finnish to English dictionary based on a English 
# to Finnish dictionary given as a parameter. 
# The values of the created dictionary should be lists of words. It should work like this:

d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
#reverse_dictionary(d)
#{'liikuttaa': ['move'], 'piilottaa': ['hide'], 'salata': ['hide'], 'kuusi': ['six', 'fir']}

# Be careful with synonyms and homonyms!

### my solution ----

# try unpacking the items in d into variables
s = {"me":1, "no":2}

# get dic keys
x = set(s.keys())
# get dic values
y = set(s.values())

print(x,y)


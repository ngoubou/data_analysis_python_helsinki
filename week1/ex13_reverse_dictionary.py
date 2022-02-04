#!/usr/bin/env python3

# Make a function reverse_dictionary that creates a Finnish to English dictionary based on a English 
# to Finnish dictionary given as a parameter. 
# The values of the created dictionary should be lists of words. It should work like this:

d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
#reverse_dictionary(d)
#{'liikuttaa': ['move'], 'piilottaa': ['hide'], 'salata': ['hide'], 'kuusi': ['six', 'fir']}

# Be careful with synonyms and homonyms!

### my solution ----c

# try unpacking the items inside d into variables
s = {"me":1, "no":2}

# get dic keys
x = list(d.keys())
# get dic values
y = list(d.values()) # use this for the condition in the foor loop
# if there are more than one item in a list, repeat
# unpack values of y so it can be iterable
z = sum(list(d.values()),[]) # use it for the new keys

#print(len(y))
# use keys as alues and vise versa
a = {}
i = 0
while i < len(z):
#for i, j in enumerate(z): # remplacer z par y # i indices and j values
# for i in len(z):    
    #print(j)
    #print(z[i+1])
    if len(y[i]) > 1:
        a[z[i]] = x[i] # a[j]
        a[z[i+1]] = x[i]
        print(a)
        i += len(y[i])
    else:
    #print(len(y[i]))
        
        a[z[i]] = x[i] # a[j]
        print(a)
        i += 1
        # gérer les doublons dans z
        # take advantage of sets methods
    #print(y)
    #i += 1
#for key, value in d.items():
    #a[value] = list(key)
    #print(key)
    #print(value)

print(a)
#print(x,y)



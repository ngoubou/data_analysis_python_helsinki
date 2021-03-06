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
while i < len(y): # gérer la condition; len(y) ou len(z)
    a[z[i]] = [x[i]] # a[j]
#for i, j in enumerate(z): # remplacer z par y # i indices and j values
# for i in len(z):    
    #print(j)
    #print(z[i+1])
    if len(y[i]) > 1:
        a[z[i+1]] = [x[i]]
        print(a)
        #a.values = list(a.values())
        #print(y[i])
        i += len(y[i])
            #print(y[i])
    else:
        print(a)
        if y[i] == y[i-1]:
            a[z[i]] = [x[i-1], x[i]]
            #print(y[i], y[i-1])
            print(a)
            # transform values to list
            # append to list

        i += 1
            #print(y[i])
            # gérer les doublons dans z
            # take advantage of sets methods
    #print(y)
    #i += 1
print(a)
#print(x,y)


## COURSE SOLUTION ----

def reverse_dictionary(d):
    
    result = {}

    for key, value in d.items():

        for v in value:

            if v in result:

                result[v].append(key)

            else:

                result[v] = [key]

    return result

 

def main():

    d = {"move":["liikuttaa"], "hide":["piilottaa", "salata"]}

    print(d)

    print(reverse_dictionary(d))

 

    d = {"move":["liikuttaa"], "hide":["piilottaa", "salata"],

         "six" : ["kuusi"], "fir" : ["kuusi"]}

    print(d)

    print(reverse_dictionary(d))

 

if __name__ == "__main__":

    main()

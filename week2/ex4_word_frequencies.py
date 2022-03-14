#!/usr/bin/env python3

import re
from unittest import result

def word_frequencies(filename = "alice.txt"):
    dic = {}
    
    with open(filename, "r") as f:
        for line in f:
            words = re.split(r'\s', line) # split the lines into words 
            
            for i in words:
                i = i.strip("""!"#$%&'()*,-./:;?@[]_""") # remove punctuation from ends & starts of words
                dic[i] = dic.get(i, 0) + 1
    return dic

def main():
    pass

if __name__ == "__main__":
    main()

        

## COURSE SOLUTION ----
#def word_frequencies(filename):
    
    #result = {}

   # with open(filename) as in_file:

       # for w in in_file.read().split():

        #    ws = w.strip("""!"#$%&'()*,-./:;?@[]_""")

           # if ws not in result:

             #   result[ws] = 0

            #result[ws] += 1

    #return result
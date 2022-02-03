#!/usr/bin/env python3

def distinct_characters(L):
    return {}

def main():
    ls = ["check", "look", "try", "pop"]
    print(distinct_characters(ls))

if __name__ == "__main__":
    main()

# Write function distinct_characters that gets a list of strings as a parameter.
# It should return a dictionary whose keys are the strings of the input list 
# and the corresponding values are the numbers of distinct characters in the key.

# Use the set container to temporarily store the distinct characters in a string. 
# Example of usage: distinct_characters(["check", "look", "try", "pop"]) should return
#  { "check" : 4, "look" : 3, "try" : 3, "pop" : 2}.

s = set(["check", "look", "try", "pop"])
for i, x in enumerate(s):
    #print(i)
    print(x)
    print(len(set(x)))

# écrire for loop combiné à enumerate
# afin d'accéder à chaque élément du set
# puis compter longeur
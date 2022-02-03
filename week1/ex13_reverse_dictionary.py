#!/usr/bin/env python3

def reverse_dictionary(d):
    return {}

def main():
    pass

if __name__ == "__main__":
    main()

# Let d be a dictionary that has English words as keys and a list of Finnish words as values. 
# So, the dictionary can be used to find out the Finnish equivalents of an English word in the following way:
d = {}
d["move"]
["liikuttaa"]
d["hide"]
["piilottaa", "salata"]

# Make a function reverse_dictionary that creates a Finnish to English dictionary based on a English 
# to Finnish dictionary given as a parameter. 
# The values of the created dictionary should be lists of words. It should work like this:

d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
reverse_dictionary(d)
{'liikuttaa': ['move'], 'piilottaa': ['hide'], 'salata': ['hide'], 'kuusi': ['six', 'fir']}

# Be careful with synonyms and homonyms!
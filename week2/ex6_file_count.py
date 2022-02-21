#!/usr/bin/env python3

from fileinput import filename
import sys

def file_count(filename):
    return (0, 0, 0)

def main():
    pass

if __name__ == "__main__":
    main()

# This exercise can give two points at maximum!

# Part 1.

# Create a function file_count that gets a filename as parameter and returns a triple of numbers. 
# The function should read the file, count the number of lines, words, and characters in the file, 
# and return a triple with these count in this order. You get division into words by splitting 
# at whitespace. You don't have to remove punctuation.

# Part 2.

# Create a main function that in a loop calls file_count using each filename in the list of 
# command line parameters sys.argv[1:] as a parameter, in turn. 
# For call python3 src/file_count file1 file2 ... the output should be

#?      ?       ?       file1
#?      ?       ?       file2
#...

# The fields are separated by tabs (\t). 
# The fields are in order: linecount, wordcount, charactercount, filename.
import re
import sys
# 1 - read the file
filename = "/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part02-e06_file_count/src/test.txt"
with open(filename, "r") as file:
    count_lines = 0
    words = []
    count_words = 0
    for line in file:
        count_lines += 1 # count the number of lines in the files
        if line != "\n": # do it for non empty lines
            words.append(re.split(r'\s', line)) # split the lines into words 
    
    for word in words:
        for i in word:
            if i: # if it is not an empty string
                count_words += 1
    print(count_lines)
    print(count_words)
  

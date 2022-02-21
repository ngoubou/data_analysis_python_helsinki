#!/usr/bin/env python3

import sys
import re

def file_count(filename):
    with open(filename, "r") as file:
        count_lines = 0
        words = []
        count_words = 0
        count_char = 0
        # count lines and add words to list
        for line in file:
            count_lines += 1 # count the number of lines in the files
            if line != "\n": # do it for non empty lines
                words.append(re.split(r'\s', line)) # split the lines into words 

    # words count
        for word in words:
            for i in word:
                if i: # if it is not an empty string
                    count_words += 1
                for character in i:
                    count_char += 1
                count_char += 1 # count the space between two words

    return (count_lines, count_words, count_char)

def main():
    for i in sys.argv[1:]:
        z = file_count(i)
        print(f"{z[0]}\t{z[1]}\t{z[2]}\t{i}")

if __name__ == "__main__":
    main()

## Course Solution ----

#import sys

#def file_count(filename):
 #   lines=0
  #  words=0
   # chars=0
    #with open(filename) as f:
     #   for line in f:
#            lines += 1
#            words += len(line.split())
#            chars += len(line)
#    return (lines, words, chars) 

#def main():

#    for filename in sys.argv[1:]:
#        lines, words, chars = file_count(filename)
#        print(f"{lines}\t{words}\t{chars}\t{filename}")
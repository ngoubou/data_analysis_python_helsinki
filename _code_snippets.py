# coding=utf-8
# put the above at the start of a file to use special characters in the comments
#l = []

# check if a list is empty
#if not l:
 # print("List is empty")

# check if list is sorted
# for a list named l
#all(l[j] <= l[j+1] for j in range(len(l)-1))

# check if all elements of a list is in another list
#all(x in ['b', 'a', 'foo', 'bar'] for x in ['a', 'b'])

# select all elements of a list except the last one
# works aussi for differents indexes and values
#mylist = [0, 1, 2, 3, 4, 5]
#x = mylist[-1]
#mylist[:x] + mylist[x+1:]

# combine  all lists into one list
#y = sum(mylist,[]) # where mylist is a list of lists

# create cell on a python file
#"#%%" # minus the first pound and the quotation marks

# get current directory
import os
#directory_path = os.getcwd()
#print("My current directory is : " + directory_path)
#folder_name = os.path.basename(directory_path)
#print("My directory name is : " + folder_name)

# change directory
new_dir = os.chdir("/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part02-e04_word_frequencies")
print(os.getcwd())

# read a file
#f = open("exercises_instructions.txt", "r") # write full path if file not in directory.
        
#for i in range(10):            # And read the first ten lines
 #   line = f.readline()
  #  print(f"Line {i}: {line}", end="")
#f.close()
# rather use context manager 

import numpy as np
a = np.array([1,4,2,7,9,5])

print(a[::-1])    # Reverses the array
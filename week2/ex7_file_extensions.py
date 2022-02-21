#!/usr/bin/env python3
import re
def file_extensions(filename):
    return ([], {})

def main():
    pass

if __name__ == "__main__":
    main()

filename = "/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part02-e07_file_extensions/src/filenames.txt"
files = []
a = []
with open(filename, "r") as file:
    for line in file:
        if not re.findall(r"(.*)\.", line): # if there's no extension
            files.append(line.strip("\n"))
       
        else:
            files.append(re.findall(r"(.*)\.", line)[0]) # take everything 
       
    print((files, 1))

# This exercise can give two points at maximum!

# Part 1.

# Write function file_extensions that gets as a parameter a filename. 
# It should read through the lines from this file. Each line contains a filename. 
# Find the extension for each filename. The function should return a pair, 
# where the first element is a list containing all filenames with no extension 
# (with the preceding period (.) removed). 
# The second element of the pair is a dictionary with extensions as keys and corresponding values
#  are lists with filenames having that extension.

# Sounds a bit complicated, but hopefully the next example will clarify this. 
# If the file contains the following lines

#file1.txt
#mydocument.pdf
#file2.txt
#archive.tar.gz
#test

# then the return value should be the pair: 
# (["test"], { "txt" : ["file1.txt", "file2.txt"], "pdf" : ["mydocument.pdf"], "gz" : ["archive.tar.gz"] } )

# Part 2.

# Write a main method that calls the file_extensions function with "src/filenames.txt" as the argument. 
# Then print the results so that for each extension there is a line consisting of the extension and 
# the number of files with that extension. 
# The first line of the output should give the number of files without extensions.

# With the example in part 1, the output should be

#1 files with no extension
#gz 1
#pdf 1
#txt 2

# Had there been no filenames without extension then the first line would have been 0 files 
# with no extension. In the printout list the extensions in alphabetical order.
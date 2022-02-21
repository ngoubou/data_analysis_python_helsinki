#!/usr/bin/env python3
import re
def file_extensions(filename):
    return ([], {})

def main():
    pass

if __name__ == "__main__":
    main()

filename = "/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part02-e07_file_extensions/src/filenames.txt"

with open(filename, "r") as file:
    files = []
    dic = {}
    dic_values = []  # what i'll use for the dic values
    dic_keys = []
    # read the file and put the file names in a list
    for line in file:
        if not re.findall(r"(.*)\.", line): # if there's no extension
            files.append(line.strip("\n"))
            dic_values.append(line.strip("\n"))
            dic_keys.append(line.strip("\n")) # dic key
       
        else:
            files.append(re.findall(r"(.*)\.", line)[0]) # take everything before the extension (ie the dot)
            dic_values.append(line.strip("\n"))
            dic_keys.append(re.findall(r"\.(.*)", line)[0])
 
    #dic_keys[3] = re.findall(r"\.(.*)", dic_keys[3])[0] # delete the "tar" before converting to set
    # doing so cause a set is unordered so can't use indices because it changes everytime
    dic_keys = list(set(dic_keys)) # remove duplicates from keys
    

    for i in dic_keys:
        a = []
        for j in dic_values:
            
            if re.findall(r'\.', j) and re.findall(r'\.(.*)', j)[0] == i:
                a.append(j)
                dic[i] = a # = a
                
            elif i == j: # if the file has no extension
                print(i)
          

print(dic)

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
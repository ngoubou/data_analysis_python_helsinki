#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    return []

def main():
    pass

if __name__ == "__main__":
    main()

# The file src/listing.txt contains a list of files with one line per file. Each line contains 7 fields: 
# access rights, number of references, owner's name, name of owning group, file size, date, filename. 
# These fields are separated with one or more spaces. 
# Note that there may be spaces also within these seven fields.

# Write function file_listing that loads the file src/listing.txt. 
# It should return a list of tuples (size, month, day, hour, minute, filename).
# Use regular expressions to do this (either match, search, findall, or finditer method).

# An example: for line

# -rw-r--r-- 1 jttoivon hyad-all   25399 Nov  2 21:25 exception_hierarchy.pdf

# the function should create the tuple (25399, "Nov", 2, 21, 25, "exception_hierarchy.pdf").


# 1 - read the file
f = open("/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part02-e02_file_listing/src/listing.txt", "r") # write full path if file not in directory.

ls = []        
for i in range(1,48):           
    line = f.readline()
    print(f"Line {i}: {line}", end="")
    mo = re.search(r'hyad-all\s{1,}(.*)', line) # va dans chaque ligne et trouve quelque chose
    print(mo.groups())
    ls.append(mo.groups())

f.close()
print(ls) # what i'll return
#mo = re.search(r'\d+ (\d+) \d+ (\d+)', 'first 123 45 67 890 last')
#print(mo)
#print(mo.groups())
# \.txt(.*) # matches everything after ".txt" in the following sentence :
# this/is/just.some/test.txt/some/other

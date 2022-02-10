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
#ls1 = []      
for i in range(1,48):           
    line = f.readline()
    #print(f"Line {i}: {line}", end="")
    mo = re.findall(r'hyad-all\s{1,}(.*)', line) # va dans chaque ligne et prends ce qui est après hyad-all
    #a = tuple(mo[0].split(" "))
    good = re.split(r'\s\s|\s|:', mo[0]) # sépare s'il y a un espace (ou double), ou un ":"
    #print(good)
    #b = re.split(r"[^\w']+", mo[0]) # the preferred result so far
    #print(b)
    #print(a[3].split(":"))
    #print(a)
    #c = ".".join([b[5], b[-1]])
   # print(b)
    #print(good)
    #print(mo[0])
    ls.append(good)
    #print(ls[i-1])
    #if len(ls[i-1]) > 6:
        #for j in ls[i-1]:
            #if not j:
                #good.pop(i-1)
                
    #ls1.append(good)
    #print(ls)
   # print(ls1)
                

        
   
    #ls.append(c)
    #print(ls)

f.close()

#print(len(ls))
#print(ls[0][0])
#ls = list(map(list, ls))
#print(ls)
for i, j in enumerate(ls):
    for k, l in enumerate(j):
        if len(ls[i]) > 6: # to be deleted, just to track the error
            print("yes")
            print(ls[i])

        if re.findall(r'^[\b\d?\d\b]+', l): # si ce sont des chiffres
            #print(ls[i][k])
            ls[i][k] = int(ls[i][k])
        if not ls[i][k]: # should not be doing that cause there should not be any empty string
            ls[i][k] = int('0'+ls[i][k]) 
            #print(ls[i][k])
            #print("list is not empty not as the lakers team")
        #print(i)
ls = list(map(tuple, ls))
print(ls) # what i'll return
#mo = re.search(r'\d+ (\d+) \d+ (\d+)', 'first 123 45 67 890 last')
#print(mo)
#print(mo.groups())
# \.txt(.*) # matches everything after ".txt" in the following sentence :
# this/is/just.some/test.txt/some/other
# 'hyad-all\s{1,}(.*)' # matches everything after 'hyad-all' and some spaces (at least one space)
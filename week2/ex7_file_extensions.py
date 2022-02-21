#!/usr/bin/env python3
import sys
import re

def file_extensions(filename):
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
                    if i == "tar.gz":
                        i = re.findall(r'\.(.*)', i)[0]
                    a.append(j)
                    dic[i] = a 
                
                elif i == j: # if the file has no extension
                    s = i
    return ([s], dic)

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

def main():
    for i in sys.argv[1:]:
        z = file_extensions(i)
     
        test = []
        testt = []
        c = 0
        d = {}
        if not re.findall(r'\.', z[0][0]): # s'il n'y a pas d'extension
            c += 1
            print(f"{c} files with no extension")
            #78
       
        for k in list(z[1].values()):
            test.append(len(k))
        for j in z[1]:   
            testt.append(j)
        
        for m,n in enumerate(testt):
            #print(m,n)
            d[n] = test[m]
        dic2 = {}
        for i in sorted(d):
            dic2[i]=d[i]
     
        for l in range(len(test)):
          
            print(f"{list(dic2.keys())[l]} {list(dic2.values())[l]}")
            #1
     

if __name__ == "__main__":
    main()

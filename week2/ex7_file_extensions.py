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
 

def main():
    z = file_extensions("filenames.txt")
    try:
        print(f"{0} files with no extension") # when it's 1 it does not work and i don't know 
        # why it works for zero
        
        for j in sorted(z[1]):
            dic2 = {}
            dic2[j] = z[1][j]
            print(list(dic2.keys())[0], len(list(dic2.values())[0]))
    except:
         print(f"0 files with no extension")
     
    
     
   
if __name__ == "__main__":
    main()

## Course Solution ----

#def file_extensions(filename):
    
   # no_extension=[]

   # d = {}

    #with open(filename) as f:

        #for line in f:

            #line=line.strip()

            #v = line.split('.')

           # if len(v) == 1:

          #      no_extension.append(line)

         #   else:

        #        extension = v[-1]

       #         if extension not in d:

      #              d[extension] = []

     #           d[extension].append(line)

    #return (no_extension, d)

 

#def main():

 #   no_extension, d = file_extensions("src/filenames.txt")

  #  print(f"{len(no_extension)} files with no extension")

   # for extension, files in sorted(d.items()):

    #    print(f"{extension} {len(files)}")
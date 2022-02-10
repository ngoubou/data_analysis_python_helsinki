#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    # 1 - read the file
    f = open("/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part02-e02_file_listing/src/listing.txt", "r") # write full path if file not in directory.

    ls = []  


    for i in range(1,48):           
        line = f.readline()
        mo = re.findall(r'hyad-all\s{1,}(.*)', line) # va dans chaque ligne et prends ce qui est après hyad-all
        good = re.split(r'\s\s|\s|:', mo[0]) # sépare s'il y a un espace (ou double), ou un ":"
    
        ls.append(good)
    

    f.close()


    for i, j in enumerate(ls):
        for k, l in enumerate(j):
    
            if re.findall(r'^[\b\d?\d\b]+', l): # si ce sont des chiffres
                ls[i][k] = int(ls[i][k])
     
    ls = list(map(tuple, ls))
    return []

def main():
    pass

if __name__ == "__main__":
    main()



## Course Solution ----

#def file_listing(filename="src/listing.txt"):
    
 #   with open(filename) as f:

  #      lines = f.readlines()

   # result=[]

    #for line in lines:

     #   pattern = r".{10}\s+\d+\s+.+\s+.+\s+(\d+)\s+(...)\s+(\d+)\s+(\d\d):(\d\d)\s+(.+)"

      #  if True:      # Two alternative ways of doing the same thing

       #     m = re.match(pattern, line)

        #else:


         #   compiled_pattern = re.compile(pattern)

          #  m = compiled_pattern.match(line)

        #if m:

         #   t = m.groups()

          #  result.append((int(t[0]), t[1], int(t[2]), int(t[3]), int(t[4]), t[5]))

        #else:

         #   print(line)

#    return result
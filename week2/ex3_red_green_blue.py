#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    return []


def main():
    pass

if __name__ == "__main__":
    main()

# The file src/rgb.txt contains names of colors and their numerical representations in RGB format.
# The RGB format allows a color to be represented as a mixture of red, green, and blue components. 
# Each component can have an integer value in the range [0,255]. 
# Each line in the file contains four fields: red, green, blue, and colorname. 
# Each field is separated by some amount of whitespace (tab or space in this case). 
# The text file is formatted to make it print nicely, but that makes it harder to process by a computer. 
# Note that some color names can also contain a space character.

# Write function red_green_blue that reads the file rgb.txt from the folder src. 
# Remove the irrelevant first line of the file. The function should return a list of strings. 
# Clean-up the file so that the strings in the returned list have four fields
# separated by a single tab character (\t). Use regular expressions to do this.

# The first string in the returned list should be:

# '255\t250\t250\tsnow'

ls = []
ls1 = []
with open("/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part02-e03_red_green_blue/src/rgb.txt", "r") as f:
    for line in f:
        #print(line)
        ls.append(line)
        #print(ls)


# remove the 1st line of the file
ls.pop(0)

# loop through every element of the list
for i, j in enumerate(ls):
    if re.findall(r'^[\s\s|\s]', j): # s'il y a un espace en début de ligne
        #print(j)
        j = j.lstrip() # supprimer espace en début de ligne
        #print(j)

    #print(len(ls[i]))
    #print(ls[i])
    #for k in ls[i]: # replace every white space and double tab by a single tab
    #print(ls[i])    
    if i > 155: # TO BE DELETED JUST TO TRACK WHERE THE ERROR STARTS 
        print(i) # i = line - 2
    ## # PRENDS TOUT CE QUI EST AVANT LE NOM DE LA COULEUR
    no_color = re.findall(r'(.*)\t\t', j) 
    #print(no_color[0])
    if no_color[0].endswith(" "):
        no_color[0] = no_color[0].rstrip(" ")
        #print("y a R")
    #print(type(a))
    #no_color = no_color[0].split(" ")
    no_color = re.split(r'\s\s\s\s\s|\s\s\s\s|\s\s\s|\s\s|\s', no_color[0]) # sépare s'il y a un espace (ou double)
    #print(len(a))
    no_color = "\t".join(no_color)
    

    ### PRENDS LE NOM DE LA COULEUR
    colour = re.findall(r'\t\t(.*)', j) 

    ## JOIN COLOR AND NO COLOR BY A TAB
    result = "\t".join([no_color, colour[0]])
    #print(result.split("\t"))
    #print(colour[0])
    #a = result + "\n"
    ls1.append(result)
    #print(ls1)
    #print("\t".join(a))
    #a = a.replace(" ", "\t")
   # print(a)

    # PLUS DE 4 CATÉGORIES 
    #if len(ls1[i].split("\t")) != 4: # TO BE DELETED
     #   print(ls1[i].split("\t"))
      #  print(len(ls1[i].split("\t")))

    #ls[i] = ls[i].replace(" ", "\t") # replace every white space by a single tab
    #ls[i] = ls[i].replace("\t\t", "\t") # replace every double tab by a single tab
    #ls[i] = ls[i].rstrip("\n") # delete '\n' at the end of the line
    #print(ls[i])    
   
for k in ls1:
    if len(k.split("\t")) != 4: # ligne 158
        print(k.split("\t"))
        print(len(k.split("\t")))
#!/usr/bin/env python3

import re

def red_green_blue(filename = "rgb.txt"):
    temp_list = []
    result = []
    with open(filename, "r") as f:
        for line in f:
            temp_list.append(line)
    
    # remove the 1st line of the file
    temp_list.pop(0)

    # loop through every element of the list
    for j in temp_list:
        if re.findall(r'^[\s\s|\s]', j): # s'il y a un espace en début de ligne
  
            j = j.lstrip() # supprimer espace en début de ligne

        ## PRENDS TOUT CE QUI EST AVANT LE NOM DE LA COULEUR
        no_color = re.findall(r'(.*)\t\t', j) 
        if no_color[0].endswith(" "):  # handles lines finishing with a space
            no_color[0] = no_color[0].rstrip(" ")
            
        no_color = re.split(r'\s\s\s\s\s|\s\s\s\s|\s\s\s|\s\s|\s', no_color[0])
        no_color = "\t".join(no_color)

        ## PRENDS LE NOM DE LA COULEUR
        colour = re.findall(r'\t\t(.*)', j) 

        ## JOIN COLOR AND NO COLOR BY A TAB
        all_line = "\t".join([no_color, colour[0]])
 

        result.append(all_line)

    return result


def main():
    pass

if __name__ == "__main__":
    main()

## Course Solution ----


#def red_green_blue(filename="src/rgb.txt"):
    
   # with open(filename) as in_file:

        #l = re.findall(r"(\d+)\s+(\d+)\s+(\d+)\s+(.*)\n", in_file.read())

        #return [

          #  "{}\t{}\t{}\t{}".format(r, g, b, name)

          #  for r, g, b, name

          #  in l

       # ]
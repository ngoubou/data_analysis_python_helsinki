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
with open("/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part02-e03_red_green_blue/src/rgb.txt", "r") as f:
    for line in f:
        #print(line)
        ls.append(line)
        #print(ls)


# remove the 1st line of the file
ls.pop(0)

# loop through every element of the list
for i in ls:
    print(i)
print(ls)
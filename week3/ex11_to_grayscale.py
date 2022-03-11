#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt



def main():
    pass

if __name__ == "__main__":
    main()

# Part 1.

# Write a function to_grayscale that takes an RGB image (three dimensional array) and returns a two dimensional gray-scale image. 
# The conversion to gray-scale should take a weighted sum of the red, green, and blue values, and use that as the value of gray. 
# The first axis is the x, the second is y, and the third is the color components (red, green, blue). 
# Use the weights 0.2126, 0.7152, and 0.0722 for red, green, and blue, respectively. 
# These weights are so because the human eye is most sensitive to green color and least sensitive to blue color.

# In the main function you can, for example, use the provided image src/painting.png. 
# Display the grayscale image with the plt.imshow function. 
# You may have to call the function plt.gray to set the color palette (colormap) to gray. 
# (See help(plt.colormaps) for more information about colormaps.)

# Part 2.

# Write functions to_red, to_green, and to_blue that get a three dimensional array as a parameter and return a three dimensional arrays. 
# For instance, the function to_red should zero out the green and blue color components and return the result. 
# In the main function create a figure with three subfigures: the top one should be the red image, the middle one the green image, 
# and the bottom one the blue image.
#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(painting):
    for i in painting[:,:,:]:
        #print(i)
        for j in i:
        #print(j)
            j[0] = 0.2126 * j[0]
            j[1] = 0.7152 * j[1]
            j[2] = 0.0722 * j[2]
    result = painting[:,:,0] # drop the last dimension of the array
    return result

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

# gray =  0.2126 * red + 0.7152 * green + 0.0722 * blue


painting=plt.imread("/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part03-e11_to_grayscale/src/painting.png")
print(painting.shape)
#print(f"The image consists of {painting.shape[0] * painting.shape[1]} pixels")
#plt.imshow(painting);
#plt.imshow(painting[:,::-1]);              # mirror the image in x direction
t = painting[:,:,0] # what i'll return at the end
#print(t.shape)
# In the following we set the pixels on the first 30 rows white:
#print(painting[0,0,:])
#print(painting[0,0,:]*2)
for i in painting[:,:,:]:
    #print(i)
    for j in i:
        #print(j)
        j[0] = 0.2126 * j[0]
        j[1] = 0.7152 * j[1]
        j[2] = 0.0722 * j[2]
        #print(j)
print(painting.shape)
painting2 = painting.copy()    # don't mess the original painting!
painting2[0:30, :, :] = 1.0    # max value for all three components produces white
#plt.imshow(painting2);
#print(painting2.shape)



# Part 2.

# Write functions to_red, to_green, and to_blue that get a three dimensional array as a parameter and return a three dimensional arrays. 
# For instance, the function to_red should zero out the green and blue color components and return the result. 
# In the main function create a figure with three subfigures: the top one should be the red image, the middle one the green image, 
# and the bottom one the blue image.
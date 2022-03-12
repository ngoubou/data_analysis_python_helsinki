#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    return (0,0)   # note the order: (center_y, center_x)

def radial_distance(a):
    return np.array([[]])

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    return np.array([[]])

def radial_mask(a):
    return np.array([[]])

def radial_fade(a):
    return np.array([[]])

def main():
    pass

if __name__ == "__main__":
    main()

# Make program that does fading of an image as earlier, except now not in horizontal direction but in radial direction. 
# As we move away from the centre of the image, the pixels fade to black.

# Part1.

# Write function center that returns coordinate pair (center_y, center_x) of the image center. 
# Note that these coordinates might not be integers. Example of usage:

# print(center(np.zeros((10, 11, 3))))
# (4.5, 5)

# The function should work both for two and three dimensional images, that is grayscale and color images.

# Write also function radial_distance that returns for image with width w and height h an array with shape (h,w), where the number at index (i,j) gives the euclidean distance from the point (i,j) to the center of the image.

# Part 2.

# Create function scale(a, tmin=0.0, tmax=1.0) that returns a copy of the array a with its elements scaled to be in the range [tmin,tmax].

# Using the functions radial_distance and scale write function radial_mask that takes an image as a parameter and returns an array with same height and width filled with values between 0.0 and 1.0. Do this using the scale function. To make the resulting array values near the center of array to be close to 1 and closer to the edges of the array are values closer to be 0, subtract the previous array from 1.

# Write also function radial_fade that returns the image multiplied by its radial mask.

# Test your functions in the main function, which should create, using matplotlib, a figure that has three subfigures stacked vertically. On top the original painting.png, in the middle the mask, and on the bottom the faded image.
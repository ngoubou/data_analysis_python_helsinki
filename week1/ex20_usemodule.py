#!/usr/bin/env python3
"""Creates a module that contains two functions for computing the hypothenuse and the area 
of a right-angled triangle."""

from math import sqrt

def hypothenuse(L, l):
    """Returns the length of the hypothenuse when given the lengths 
        of two other sides of a right-angled triangle"""
    hypo = sqrt(L**2 + l**2)
    return hypo

def area(b, h):
    """Returns the area of the right-angled triangle, when two sides, 
        perpendicular to each other, are given as parameters."""
    a = (b * h) / 2
    return a


__author__ = "Lionel Ngoubou"
__version__ = "0.1"
# __doc__ = "i do not exactly know what to write here, just hope it'll solve my problem"

# Create your own module as file triangle.py in the src folder. The module should contain two functions:

    # hypothenuse which returns the length of the hypothenuse when given the lengths 
    # of two other sides of a right-angled triangle

    # area which returns the area of the right-angled triangle, when two sides, 
    # perpendicular to each other, are given as parameters.

# Make sure both the functions and the module have descriptive docstrings. 
# Add also the __version__ and __author__ attributes to the module.
# Call both your functions from the main function (which is in file usemodule.py).

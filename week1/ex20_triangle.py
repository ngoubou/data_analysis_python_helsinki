#!/usr/bin/env python3
"""Creates a module that contains two functions for computing the hypothenuse and the area 
of a right-angled triangle."""

from math import sqrt

def hypothenuse(L, l):
    """Returns the length of the hypothenuse when given the lengths 
        of two other sides of a right-angled triangle"""
    return sqrt(L**2 + l**2)

def area(b, h):
    """Returns the area of the right-angled triangle, when two sides, 
        perpendicular to each other, are given as parameters."""
    return (b * h) / 2


__author__ = "Lionel Ngoubou"
__version__ = "0.1"

# Done Week 1 finally !!!!
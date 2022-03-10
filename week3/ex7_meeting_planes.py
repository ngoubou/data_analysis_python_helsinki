#!/usr/bin/env python3

import numpy as np

def meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    return []

def main():
    a1=1
    b1=4
    c1=5
    a2=3
    b2=2
    c2=1
    a3=2
    b3=4
    c3=1

    x, y, z = meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3)
    print(f"Planes meet at x={x}, y={y} and z={z}")

if __name__ == "__main__":
    main()

# Write function meeting_planes that gets the coefficients of three planes as parameters and returns 
# the point where the planes meet. 
# The equations for the planes are: 
# z=a1y+b1x+c1, z=a2y+b2x+c2 and z=a3y+b3x+c3.

# Example of usage:

# x, y, z = meeting_planes(a1, b1, c1,  a2, b2, c2,  a3, b3, c3)

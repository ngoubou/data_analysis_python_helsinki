#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    np.array([])

def main():
    np.array([])

if __name__ == "__main__":
    main()

# Let x and y be m-dimensional vectors. 
# The angle α\alphaα between two vectors is defined by the equation cos⁡xy(α) = ..., 
# where the angle brackets denote the inner product, and ∣∣x∣∣ = ...

# Write function vector_angles that gets two arrays X and Y with same shape (n,m) as parameters. 
# Each row in the arrays corresponds to a vector. The function should return vector of shape (n,) 
# with the corresponding angles between vectors of X and Y in degrees, not in radians. 
# Again, don't use loops, but use vectorized operations.

# Note: function np.arccos is only defined on the domain [-1.0,1.0]. 
# If you try to compute np.arccos(1.000000001), it will fail.
# These kind of errors can occur due to use of finite precision in numerical computations. 
# Force the argument to be in the correct range (clip method).

#Test your solution in the main program.
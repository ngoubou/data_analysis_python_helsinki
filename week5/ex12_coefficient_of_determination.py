#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model


def coefficient_of_determination():
    return []
    
def main():

if __name__ == "__main__":
    main()

# Using the same data as in the previous exercise, instead of printing the regression coefficients, print the coefficient of determination. 
# The coefficient of determination, denoted by R2, tells how well the linear regression fits the data. 
# The maximum value of the coefficient of determination is 1. That means the best possible fit.

# Part 1.

# Using all the features (X1 to X5), fit the data using a linear regression (include the intercept). 
# Get the coefficient of determination using the score method of the LinearRegression class. 
# Write a function coefficient_of_determination to do all this. It should return a list containing the R2-score as the only value.

# Part 2.

# Extend your function so that it also returns R2-scores related to linear regression with each single feature in turn. 
# The coefficient_of_determination (https://en.wikipedia.org/wiki/Coefficient_of_determination) function should therefore return a list 
# with six R2-scores (the first score is for five features, like in Part 1). 
# To achieve this, your function should call both the fit method and the score method six times.

# The output from the main method should look like this:

#R2-score with feature(s) X: ...
#R2-score with feature(s) X1: ...
#R2-score with feature(s) X2: ...
#R2-score with feature(s) X3: ...
#R2-score with feature(s) X4: ...
#R2-score with feature(s) X5: ...

# How small can the R2-score be? Experiment both with fitting the intercept and without fitting the intercept.
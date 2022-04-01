#!/usr/bin/env python3


def explained_variance():
    return [], []

def main():
    v, ev = explained_variance()
    print(sum(v), sum(ev))

if __name__ == "__main__":
    main()

# This exercise can give two points at maximum!

# Part 1.

# Write function explained_variance which reads the tab separated file "data.tsv". The data contains 10 features. Then fit PCA to the data. 
# The function should return two lists (or 1D arrays). The first list should contain the variances of all the features. 
# The second list should consist of the explained variances returned by the PCA.

# In the main function print these values in the following form:

# The variances are: ?.??? ?.??? ...
# The explained variances after PCA are: ?.??? ?.??? ...

# Print the values with three decimal precision and separate the values by a space.

# Part 2.

# Plot the cumulative explained variances. The y-axis should be the cumulative sum, and the x-axis the number of terms in the cumulative sum.
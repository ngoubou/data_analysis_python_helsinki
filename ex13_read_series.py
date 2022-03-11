#!/usr/bin/env python3

import pandas as pd    # This is the standard way of importing the Pandas library
import numpy as np

def read_series():
    return pd.Series()

def main():
    pass

if __name__ == "__main__":
    main()

# Write function read_series that reads input lines from the user and return a Series. 
# Each line should contain first the index and then the corresponding value, separated by whitespace. 
# The index and values are strings (in this case dtype is object). An empty line signals the end of Series. 
# Malformed input should cause an exception. 
# An input line is malformed, if it is non-empty and, when split at whitespace, does not result in two parts.

# Test your function from the main function.
#!/usr/bin/env python3

import pandas as pd
import numpy as np


def cleaning_data():
    return None

def main():
    return

if __name__ == "__main__":
    main()

# This exercise can give two points at maximum!

# The entries in the following table of US presidents are not uniformly formatted. 
# Make function cleaning_data that reads the table from the tsv file src/presidents.tsv and returns the cleaned version of it. 
# Note, you must do the edits programmatically using the string edit methods, not by creating a new DataFrame by hand. T
# he columns should have dtypes object, integer, float, integer, object. 
# The where method of DataFrames can be helpful, likewise the string methods of Series objects. 
# You get an additional point, if you manage to get the columns President and Vice-president right!

#President 	Start 	Last 	Seasons 	Vice-president
#donald trump 	2017 Jan 	- 	1 	Mike pence
#barack obama 	2009 	2017 	2 	joe Biden
#bush, george 	2001 	2009 	2 	Cheney, dick
#Clinton, Bill 	1993 	2001 	two 	gore, Al
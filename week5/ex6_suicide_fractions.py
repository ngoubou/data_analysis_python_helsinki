#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    return pd.Series()

def main():
    return

if __name__ == "__main__":
    main()

# Load the suicide data set from src folder. This data was originally downloaded from Kaggle. 
# Kaggle contains lots of interesting open data sets.

# Write function suicide_fractions that loads the data set and returns a Series 
# that has the country as the (row) index and as the column the mean fraction of suicides per population in that country. 
# In other words, the value is the average of suicide fractions. The information about year, sex and age is not used.
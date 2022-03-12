#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    file = "/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part04-e09_snow_depth/src/kumpula-weather-2017.csv"
    df = pd.read_csv(file)
    df = df["Snow depth (cm)"]
    return df.max()

def main():
    print(f"Max snow depth: {snow_depth()}")

if __name__ == "__main__":
    main()

## Couse Solution ----
# (Almost) Similar to the course one

#def snow_depth():
#    df = pd.read_csv("src/kumpula-weather-2017.csv")
#    return df["Snow depth (cm)"].max()
 
#def main():
#    max_depth = snow_depth()
#    print(f"Max snow depth: {max_depth:.1f}")
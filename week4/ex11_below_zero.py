#!/usr/bin/env python3

import pandas as pd

def below_zero():
    file = "/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part04-e11_below_zero/src/kumpula-weather-2017.csv"
    df = pd.read_csv(file)
    df = df[df["Air temperature (degC)"] < 0]
    return len(df)

def main():
    b_z = below_zero()
    print(f"Number of days below zero: {b_z}")

if __name__ == "__main__":
    main()


## Course Solution ----
#def below_zero():
#    df = pd.read_csv("src/kumpula-weather-2017.csv")
#    return sum(df["Air temperature (degC)"] < 0.0)
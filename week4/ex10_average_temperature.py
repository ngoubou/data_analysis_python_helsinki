#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    df = df[df["m"] == 7]
    return df["Air temperature (degC)"].mean()

def main():
    avg_temp = average_temperature()
    print(f"Average temperature in July: {avg_temp:.1f}")

if __name__ == "__main__":
    main()

## Course Solution ----
# Similar to the course solution (99%)
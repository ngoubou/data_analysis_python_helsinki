#!/usr/bin/env python3

import pandas as pd

def cyclists():
    file = "/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part04-e12_cyclists/src/Helsingin_pyorailijamaarat.csv"
    df = pd.read_csv(file, sep = ";")
    df = df.dropna(how = "all")
    df = df.dropna(axis = 1, how = "all")
    return df


def main():
    print(cyclists())
    
if __name__ == "__main__":
    main()


## Course Solution ----
# Same as mine
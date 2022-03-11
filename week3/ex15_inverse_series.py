#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    return pd.Series(s.index, index = s.values)

def main():
    s = pd.Series([1, 2, 3, 4])

    print(inverse_series(s))

if __name__ == "__main__":
    main()


## Course Solution ----
# Same as mine
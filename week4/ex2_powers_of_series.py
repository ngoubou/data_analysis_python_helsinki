#!/usr/bin/env python3

import pandas as pd

def powers_of_series(s, k):
    d = {}
    for i in range(1, k + 1):
        d.update({i: s.values**i})
    df = pd.DataFrame(d, index = s.index)
    return df
    
def main():
    ind = list("abcd")
    s = pd.Series([1,2,3,4], index = ind)
    print(powers_of_series(s, 3))
    
if __name__ == "__main__":
    main()

## Course Solution ----
# I wouldn't say their solution is better (define better),
# you could argue both are good (before timing it)

#def powers_of_series(s, k):
 #   c = [ s**i for i in range(1,k+1) ]
  #  df = pd.DataFrame(dict(zip(range(1,k+1), c)))
   # return df
#!/usr/bin/env python3

import pandas as pd

def cities():
    df = pd.DataFrame([[643272, 715.48], [643272, 528.03], [231853, 689.59], [223027, 240.35], [201810, 3817.52]], 
    columns = ["Population", "Total area"], index = ["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"])
    return df
    
def main():
    print(cities())
    
if __name__ == "__main__":
    main()

## Course Solution ----
# Their solution is more concise and that's normally the way i go about it

def cities():
    a = [[643272, 715.48],
       [279044, 528.03],
       [231853, 689.59],
       [223027, 240.35],
       [201810, 3817.52]]
    cols = ["Population", "Total area"]
    ind = ["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"]
    df = pd.DataFrame(a, index=ind, columns=cols)
    return df
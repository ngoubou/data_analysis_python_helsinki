#!/usr/bin/env python3

import pandas as pd

def municipalities_of_finland():
    file = "/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part04-e04_municipalities_of_finland/src/municipal.tsv"
    df = pd.read_csv(file, sep = "\t", index_col = 0) # use the first column as the rows index
    return df["Akaa": "Äänekoski"] # return the rows corresponding to municipalities in Finland
    
def main():
    print(municipalities_of_finland())
    
if __name__ == "__main__":
    main()

## Course Solution ----
# Similar to mine, only use main() to print different values of the df

#def main():
#    df=municipalities_of_finland()
#    print(df.iloc[0,0])
#    print(df.iloc[-1,-1])
#    #df=pd.DataFrame()
#    print("Shape: {}, {}".format(*df.shape))
#    for name in df.columns:
#        print(name)
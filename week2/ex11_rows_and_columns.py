#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    result = []
    for rows in a:
        result.append(rows)
    return result

def get_columns(a):
    result = []
    for cols in a.T:
        result.append(cols)
    return result
    

def main():
    np.random.seed(0)
    a = np.random.randint(0,10, (4,4))
    print("a:", a)  
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))


if __name__ == "__main__":
    main()

## Course Solution ----
# They used list comprehension

# def get_rows(a):
    #result = [row for row in a]
    #return result

 

#def get_columns(a):
 #   result = [row for row in a.T]
  #  return result
#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
    return [np.array([rows]) for rows in a]

def get_column_vectors(a):
    result = []
    for cols in a.T:
        ls = [[[cols[j]]] for j in range(len(cols))]
        result.append(np.concatenate(ls))
    return result


def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))


if __name__ == "__main__":
    main()

## Course Solution ----
# Once again, as suspected, it was way easier than what i did.
# Will i ever get better at this? To be continued...

#def get_row_vectors(a):
    #return np.split(a, a.shape[0], axis=0)

 

#def get_column_vectors(a):
    #return np.split(a, a.shape[1], axis=1)
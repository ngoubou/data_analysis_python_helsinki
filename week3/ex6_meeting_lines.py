#!/usr/bin/env python3

import numpy as np

def meeting_lines(a1, b1, a2, b2):
    A = np.array([[-a1, 1], [-a2, 1]])
    b = np.array([b1, b2])   
    return np.linalg.solve(A, b)


def main():
    a1=1
    b1=4
    a2=3
    b2=2

    x, y  = meeting_lines(a1, b1, a2, b2)
    print(f"Lines meet at x={x} and y={y}")
    

if __name__ == "__main__":
    main()

## Course Solution ----
# Had (and still have) to brush my linear algebra knowledge to solve this
# Been struggling (a bit) since end of last week assignments because i forgot a lot about matrix operations

# My solution is the same as the course one
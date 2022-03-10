#!/usr/bin/env python3

import numpy as np

#def meeting_lines(a1, b1, a2, b2):
 #   a = np.array([[-a1,1], [-a2,1]])
  #  b = np.array([b1,b2])   
   # return np.linalg.solve(a, b)
    
def almost_meeting_lines(a1, b1, a2, b2):
    a = np.array([[-a1,1], [-a2,1]])
    b = np.array([b1,b2])
    tt = []
    c = 0 # keep track of number of times it computes the exact solution
    try:
        t = np.linalg.solve(a, b) # si celui-ci produit une erreur
        c += 1
    except np.linalg.LinAlgError:
        t = np.linalg.lstsq(a,b)[0] # calcule least square

    if c > 0:
        tt.append(True)
    else:
        tt.append(False)
    return t, tt[0]

def main():
    a1=1
    b1=2
    a2=-1
    b2=0

    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")

    a1=a2=1
    b1=2
    b2=-2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1=1
    b1=2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b1)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1=1
    b1=2
    a2=1
    b2=1
    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

if __name__ == "__main__":
    main()

## Course Solution ----
# Very interesting cause it helps me brush off my linear algebra skills
# but it really has been painful

#def almost_meeting_lines(a1, b1, a2, b2):
#    A=np.array([[-a1,1],[-a2,1]])
#    b=np.array([b1,b2])
#    x, residuals, rank, s = np.linalg.lstsq(A, b)
#    exact = rank==2
#    return x, bool(exact)
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
    c = 0
    try:
        t = np.linalg.solve(a, b) # si celui-ci produit une erreur
        c += 1
    except np.linalg.LinAlgError:
        t = np.linalg.lstsq(a,b)[0] # calcule least square
        #c -= 1 
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

# In the earlier "meeting lines" exercise there is a problem if the lines don't meet at all. 
# Extend that solution so that it tells the meeting point if it exists, 
# and otherwise finds the point that is closest to the both lines. 
# You can use the numpy.linalg.lstsq for this.
#a1=1
#b1=2
#a2=-1
#b2=0
#np.linalg.lsts
# Example of usage:

# (x, y), exact = almost_meeting_lines(1, 2, -1, 0)
# print(x, y, exact)
# -1.000000 1.000000 True


import math
#print(math.cos(0))

## Breaking the namespace
from math import cos 
#print(cos(1))

#print(dir())

a = 5
def f(i):
    return i + 1

#print(dir())

print(2**2)
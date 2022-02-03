import numpy as np
for i in range(10):
        L = [int(i) for i in set(np.random.randint(-100, 100, 10))]
        mi = min(L)
        ma = max(L)
        complement = list(set(range(mi, ma+1)) - set(L))
print(L)
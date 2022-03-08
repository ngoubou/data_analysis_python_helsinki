#!/usr/bin/env python3

import numpy as np
from scipy.linalg import norm
from math import pi

a = np.array([[0,0,1], [-1,1,0]])
b = np.array([[0,1,0], [1,1,0]])

## 1 - Compute the inner product between the vectors of X and Y
prod_in = np.inner(a, b)
#print(prod_in)

## 2 - Compute the product of the l1 norms of X and Y
prod_norms = norm(a, 1) * norm(b, 1)
#print(prod_norms)

## 3 - Compute the arccos of the ratio between 1 et 2 and returns the dvalue in degree rather than radian
angle = np.arccos(np.clip(prod_in / prod_norms, -1, 1)) * 180 / pi

## TO DO ----
# Revoir implémentations de inner product et norm
# Voir exemples de documentation de chacune des fonctions
# Voir exemples math et voir ce que ça fait 
#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt

def fit_line(x, y):
    model=LinearRegression(fit_intercept=True)
    model.fit(x[:,np.newaxis], y)
    xfit=np.linspace(1, 3, 10)
    print(xfit)
    yfit=model.predict(xfit[:, np.newaxis])
    print(yfit)
    return(model.coef_[0], model.intercept_)
    
def main():
    x = np.array([1,2,3])
    y = np.array([1,2.5,3]) + 1
    s, i = fit_line(x, y)

    xfit = np.linspace(1, 3, 3)
    yfit = s * x + i + 1 * np.random.randn(3)
    print("Slope:", s)
    print("Intercept:", i)
    plt.plot(xfit, yfit, color = "black")
    plt.plot(x, y, "o")
    plt.show()


if __name__ == "__main__":
    main()

## Course Solution ----

#def fit_line(x, y):
 #   reg = LinearRegression()
  #  X = x.reshape((-1, 1))
   # reg.fit(X, y)
    #return reg.coef_[0], reg.intercept_

#def main():
 #   x = np.array([1, 2, 3])
  #  y = np.array([1, 2.5, 3]) + 1
   # slope, intercept = fit_line(x, y)
    #print("Slope:", slope)
    #print("Intercept:", intercept)
    #plt.scatter(x, y)
    #x1 = np.linspace(min(x)-1, max(x)+1, 10)
    #plt.plot(x1, x1*slope + intercept, 'red')
    #plt.show()
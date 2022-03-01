#!/usr/bin/env python3

#print(1)
class Rational:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __repr__(self): # support printing floats
        return f"{self.first / self.last}"
    
    # i now implement the basic operations and comparisons
    def __mul__(self, other):
        return Rational(self.first * other.first, self.last * other.last)

    def __truediv__(self, other):
        return Rational(self.first * other.last, self.last * other.first)

    def __add__(self, other): 
        return Rational(self.first * other.last + self.last * other.first, self.last * other.last)
    
    def __sub__(self, other):
        return Rational(self.first * other.last - self.last * other.first, self.last * other.last)

def main():
    r1 = Rational(1,4)
    r2 = Rational(2, 3)
    print(r1)
    print(r2)
    print(r1 * r2)
    print(r1 / r2)
    print(r1 + r2)
    print(r1 - r2)


if __name__ == "__main__":
    main()
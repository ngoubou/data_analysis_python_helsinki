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
    
    def __eq__(self, other):
        return self.first / self.last == other.first / other.last
        #return Rational(self.first, self.last) == Rational(other.first, other.last) # produces an error

    def __gt__(self, other):
        return self.first / self.last > other.first / other.last
    
    def __lt__(self, other):
        return self.first / self.last < other.first / other.last

    # implement comparisons
    #def 


def main():
    r1 = Rational(1,4)
    r2 = Rational(2, 3)
    print(r1)
    print(r2)
    print(r1 * r2)
    print(r1 / r2)
    print(r1 + r2)
    print(r1 - r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
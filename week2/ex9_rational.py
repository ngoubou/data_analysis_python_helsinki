#!/usr/bin/env python3

from fractions import Fraction # for expressing the floats as fractions as instructed

class Rational:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __str__(self): # support printing floats # can use str or repr
        return f"{Fraction(self.first / self.last).limit_denominator()}"
    
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

# Course Solution ----

# the only time (so far) i prefer my solution

#class Rational(object):    
 #   def __init__(self, n, d):
  #      self.n = n
   #     self.d = d

    #def __str__(self):
     #   return "%i/%i" % (self.n, self.d)

    #def __repr__(self):
     #   return "Rational(%i, %i)" % (self.n, self.d)

    #def __mul__(self, r2):
     #   a = self.n * r2.n
      #  b = self.d * r2.d
       # return Rational(a,b)

    #def __truediv__(self, r2):
     #   a = self.n * r2.d
      #  b = self.d * r2.n
       # return Rational(a,b)
 
    #def __add__(self, r2):
     #   d1 = self.d
      #  d2 = r2.d
       # a = self.n * d2 + r2.n * d1
        #b = d1 * d2
        #return Rational(a, b)

    #def __sub__(self, r2):
     #   d1 = self.d
      #  d2 = r2.d
       # a = self.n * d2 - r2.n * d1
        #b = d1 * d2
        #return Rational(a, b)

    #def __eq__(self, r2):
     #   return self.n * r2.d == self.d *r2.n

    #def __lt__(self, r2):
     #   return self.n * r2.d < self.d *r2.n

    #def __gt__(self, r2):
     #   return self.n * r2.d > self.d *r2.n
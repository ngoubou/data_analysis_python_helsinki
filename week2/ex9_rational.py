#!/usr/bin/env python3

class Rational(object):
    """Create a class called Rational"""
    #x = 0
    def __init__(self, num1, num2):
        "This initialises an instance of type ClassName"
        self.num1 = num1 # creates an instance attribute
        self.num2 = num2
        #c = num1 / num2
    def __truediv__(self):
        #x += 1
        print(self.num1.__truediv__(self.num2))
        #print(x.__truediv__(y))
        #return s/ss
        #return self.num1 / self.num2
    #def div(self):
        #print(self.num1/self.num2)
    
#class test(Rational):
 #   def g(self, a, b):
        #print(Rational(a, b).__div__())
  #      Rational(a, b).div()
    #Rational().div()
    #print(__truediv__())
    #print(x)
#class Test(Rational):
 #   def __init__(self, num1, num2):
  #      self.num1 = num1 # creates an instance attribute
   #     self.num2 = num2
    #print(Rational.__truediv__())
    #pass

## USE CLASS INHERITANCE 

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    r1.__truediv__()
    r2.__truediv__()
    #print(r1)
   # x = test(1,5)
    #r1.div()
    #x.g(1,5)
    #print(x)
    #r3 = Test(1,4)
    #print(r3)
    #print(r1.__truediv__()) #the result i want
    #print(r2)
   # print(r1*r2)
    #print(r1/r2)
    #print(r1+r2)
    #print(r1-r2)
   # print(Rational(1,2) == Rational(2,4))
    #print(Rational(1,2) > Rational(2,4))
    #print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()

# Create a class Rational whose instances are rational numbers. 
# A new rational number can be created with the call to the class. 
# For example, the call r=Rational(1,4) creates a rational number “one quarter”. 
# Make the instances support the following operations: + - * / < > == with their natural behaviour. 
# Make the rationals also printable so that from the printout 
# we can clearly see that they are rational numbers. 
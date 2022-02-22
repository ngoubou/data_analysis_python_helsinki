#!/usr/bin/env python3

class Rational(object):
    """Create a class called Rational"""
    def __init__(self, num1, num2):
        "This initialises an instance of type ClassName"
        self.num1 = num1 # creates an instance attribute
        self.num2 = num2
        #c = num1 / num2
    def __truediv__(self):
        print(self.num1/self.num2)

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1.__truediv__())
    print(r2)
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
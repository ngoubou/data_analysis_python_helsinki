#!/usr/bin/env python3

class Prepend(object):
    """Create a class called Prepend"""
    
    def __init__(self, start):
        "This initialises an instance of type ClassName"
        self.start = start # creates an instance attribute
    
    def write(self, s):#, param1):
        """This is a method of the class"""
        print(self.start + s)
 

def main():
    p = Prepend("+++ ")    
    p.write("Hello")

if __name__ == "__main__":
    main()

# One of the rare instances where my solution equals the course one
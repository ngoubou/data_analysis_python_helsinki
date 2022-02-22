#!/usr/bin/env python3

class Prepend(object):
    # Add the methods of the class here
    """Create a class called Prepend"""
    
    def __init__(self, param1):#, param2):
        "This initialises an instance of type ClassName"
        self.start = param1 # creates an instance attribute
        #c = param2      # creates a local variable of the function
        # statements ...
    
    def write(self):#, param1):
        """This is a method of the class"""
        # some statements
        print(self)
    
    a = 1 # This creates a class attribute

def main():
    pass

if __name__ == "__main__":
    main()

# Create a class called Prepend. We create an instance of the class by giving a string as a parameter
# to the initializer. The initializer stores the parameter in an instance attribute start. 
# The class also has a method write(s) which prints the string s prepended with the start string. 
# An example of usage:

# p = Prepend("+++ ")
#p.write("Hello");

# Will print

# +++ Hello

# Try out using the class from the main function.
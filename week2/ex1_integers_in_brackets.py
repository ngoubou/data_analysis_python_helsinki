#!/usr/bin/env python3


import imp


def integers_in_brackets(s):
    return []

def main():
    pass

if __name__ == "__main__":
    main()

# Write function integers_in_brackets that finds from a given string all integers
# that are enclosed in brackets.

# Example run: integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx") returns [12, -43, 12]. 
# So there can be whitespace between the number and the brackets, 
# but no other character besides those that make up the integer.

# Test your function from the main function.

# input string
import re
s = " afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"
output = re.findall(r'[+-]?\d+', s) #[12, -43, 12]

# i want everything that starts with either a digit or [+-]
# and ends with a digit


# use map to convert each element of the list as an integer
# before printing it

print(output)
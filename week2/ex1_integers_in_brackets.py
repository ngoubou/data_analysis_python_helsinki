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
#s = " afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"
s = "  afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xxx"
#output = re.findall(r'[+-]?\d+', s) #[12, -43, 12]

# i want everything that starts with either a digit or [+-]
# and ends with a digit


# use map to convert each element of the list as an integer
# before printing it

#print(output)
#-\b\d+\b #|\b[\+-]

# numbers starting and ending with a digit
#print(re.findall(r'\b\d+\b', s)) # best so far
#print(re.findall(r'[^a-zA-Z_+]?\d+', s))
#print(re.findall(r'[^\-]?\d+', s)) # pas bon
output = re.findall(r'[-]?\b\d+\b', s)
#print(output)
#print(list(map(int, output))) # got it
#print(re.findall(r'[+-]?\d+', s))
print(re.findall(r'[-]?\b[\d]\d\b', s)) # PARTIR DE LUI
#print(re.findall(r'^[^+-]', s))
#print(re.findall(r'[^+\d]+', s))
#print(re.findall(r'[+-]?\d+\b', s))

# print everything that ends with a digit
#print(re.findall(r'\d+\b', s)) # prints every end digit if i dont use '+'

# print everything that starts with a digit
#print(re.findall(r'\b\d+', s))

# print everything that starts with "+"
#print(re.findall(r'\b\++', s))

#print(re.findall(r'[+-]?\d+', s))
print(re.search(r'\d+ (\d+) \d+ (\d+)', 'first 123 45 67 890 last'))
#a = "+-43 25 48"
#print(re.findall(r'^(-|\+)', a))
#print(re.findall(r'[^\d\b]+\b\d+\b', a)) # prends +-43
#print(re.findall(r'[^\d\b]+', a)) # prends +- et 'top'
#print(re.findall(r'[^ea]', a))
#print(re.findall(r'^"ea"', a))
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

# i want everything that starts with either a digit, or [+-] but not both [+-]
# and ends with a digit


# use map to convert each element of the list as an integer
# before printing it



# numbers starting and ending with a digit

output = re.findall(r'[-]?\b[\d]\d\b', s)
#print(re.findall(r'\b\d?\d\b', s))
print(output)
#print(list(map(int, output))) # got it
# [^\[\]+?=\-] # matches everything but "+" and "-"
# '[^\+\-][-+]?\b[\d]\d\b' # matches [47 and [+12
# '[^\b\[\]\bA-Za-z]' # matches every digit inside the brackets
#print(re.findall(r'[^\+\-][-+]?\b[\d]\d\b', s))
mo = re.findall(r'[^\+\-][-+]?\b[\d]\d\b', s)

ls  = []
for i in mo:
    yo = re.findall(r'[-]?\b[\d]\d\b', i)
    #print(yo[0])
    ls.append(yo[0])
    #ls.append(re.findall(r'[-]?\b[\d]\d\b', i))

print(ls)
print(list(map(int, ls)))
#print(re.findall(r'[-]?\b[\d]\d\b', mo))

# this is not exactly how it should be done, but it is what it is

## Course Solution ----
#def integers_in_brackets(s):
    
    #result = re.findall(r"\[\s*([+-]?\d+)\s*\]", s)

    #return list(map(int, result))


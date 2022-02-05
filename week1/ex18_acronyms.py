#!/usr/bin/env python3


def acronyms(s):
    return []

def main():
    print(acronyms("""For the purposes of the EU General Data Protection Regulation (GDPR), the controller of your personal information is International Business Machines Corporation (IBM Corp.), 1 New Orchard Road, Armonk, New York, United States, unless indicated otherwise. Where IBM Corp. or a subsidiary it controls (not established in the European Economic Area (EEA)) is required to appoint a legal representative in the EEA, the representative for all such cases is IBM United Kingdom Limited, PO Box 41, North Harbour, Portsmouth, Hampshire, United Kingdom PO6 3AU."""))


if __name__ == "__main__":
    main()

# Write function acronyms which takes a string as a parameter and returns a list of acronyms.
# A word is an acronym if it has length at least two, and all its characters are in uppercase. 
# Before acronym detection, delete punctuation with the strip method.

# Test this function in the main function with the following call:

# print(acronyms("""For the purposes of the EU General Data Protection Regulation (GDPR), the controller of your personal information is International Business Machines Corporation (IBM Corp.), 1 New Orchard Road, Armonk, New York, United States, unless indicated otherwise. Where IBM Corp. or a subsidiary it controls (not established in the European Economic Area (EEA)) is required to appoint a legal representative in the EEA, the representative for all such cases is IBM United Kingdom Limited, PO Box 41, North Harbour, Portsmouth, Hampshire, United Kingdom PO6 3AU."""))

# This should return ['EU', 'GDPR', 'IBM', 'IBM', 'EEA', 'EEA', 'IBM', 'PO', 'PO6', '3AU']

s = """For the purposes of the EU General Data Protection Regulation (GDPR), the controller of your personal information is International Business Machines Corporation (IBM Corp.), 1 New Orchard Road, Armonk, New York, United States, unless indicated otherwise. Where IBM Corp. or a subsidiary it controls (not established in the European Economic Area (EEA)) is required to appoint a legal representative in the EEA, the representative for all such cases is IBM United Kingdom Limited, PO Box 41, North Harbour, Portsmouth, Hampshire, United Kingdom PO6 3AU."""

# strips only trim the leading and trailing characters specified in the sep argument

# print(s.find("EU"))
a = s.split(",")
#print("".join(a))

#print(len(a))
#print(type(a[0]))
#print(a)
#for i in range(len(a)):
res = []
for i in a:

   # print(a[i].isupper())
    #a[i].find(a[i].isupper())
    
    #print(i.isalnum())
   #print(type(i.split(" ")))
    b = i.split(" ")
    for j in b:
        if j.isupper():
            j = j.strip("()")
            res.append(j)
        #print(j.isupper())

# delete parentheses
#for k in res:
    #print(k)
    #print(k.strip("()"))
    #k = k.strip("()")
    #print(k.lstrip("("))
    #print(k.rstrip(")"))
    
print(res)
print(len(res))
    #print(len(i))
    #print(i.split(" "))
    #print(len(i.split(" ")))
    #print(type(i.split(" ")))
    #print(i.split(" ").isupper())
    #print(i)
    #print(i.split())

#print('abc GG def--ghi'.split("G"))
#print("issi" in "mississipi")
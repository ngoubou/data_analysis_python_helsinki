#!/usr/bin/env python3


def acronyms(s):
    # split the input into multiple sentences separated by a comma
    a = s.split(",")

    # create an empty list where i'll store the acronyms
    res = []

    # slit each sentence into multiple words a
    for i in a:
        b = i.split(" ")
        # extract uppercases and remove parentheses around the words
        for j in b:
            if j.isupper():
                j = j.strip("()")
                res.append(j)
    return res

def main():
    print(acronyms("""For the purposes of the EU General Data Protection Regulation (GDPR), the controller of your personal information is International Business Machines Corporation (IBM Corp.), 1 New Orchard Road, Armonk, New York, United States, unless indicated otherwise. Where IBM Corp. or a subsidiary it controls (not established in the European Economic Area (EEA)) is required to appoint a legal representative in the EEA, the representative for all such cases is IBM United Kingdom Limited, PO Box 41, North Harbour, Portsmouth, Hampshire, United Kingdom PO6 3AU."""))


if __name__ == "__main__":
    main()

## Course Solution ----

from string import punctuation

def acronyms(s):

    L = [x.strip(punctuation) for x in s.split() ]

    return [ x for x in L if x.isupper() and len(x) >= 2 ]

# they never mentionned the string import, so didn't think of importing anything
# i strictly use the methods seen so far
# but their code is (once again) cleaner.

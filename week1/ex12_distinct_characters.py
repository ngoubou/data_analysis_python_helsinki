#!/usr/bin/env python3

def distinct_characters(L):
    # convert the input list to a set (not necessary based on course solution)
    s = set(L)
    return {x: len(set(x)) for x in s}

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()


# Course solution

#def distinct_characters(L):
    #result = {}
    #for s in L:
        #result[s] = len(set(s))

    #return result
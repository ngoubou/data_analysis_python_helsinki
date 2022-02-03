#!/usr/bin/env python3

def distinct_characters(L):
    # convert the input list to a set (not necessary based on course solution)
    s = set(L)
    # create a dictionary that will store the final key and values
    d = {}
    for i, x in enumerate(s): # i'm just keeping the i cause removing it produces a different format 
        #print(i)
        #print(x, len(set(x)))
        # x store each item in s and len(set(x)) counts the distinct characters in each item
        d[x] = len(set(x)) 

   
    return d

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
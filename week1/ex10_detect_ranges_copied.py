#!/usr/bin/env python3

 

def detect_ranges(L):
    #L.sort()
    ls = sorted(L)
    res = []
    i=0
    size = len(ls)

    while i < size-1:
        #if next number is +1 bigger
        if (ls[i+1]-ls[i] == 1): 
            r1= ls[i]        #start of range
            #loop as long next number is +1 bigger and end not reached
            while (i < size-1) and (ls[i+1]-ls[i] == 1):  
                i += 1
            r2 = ls[i]+1        #end of range
            res.append(((r1,r2))) #add pair 
        else:   
            res.append(ls[i]) #add single number
        i += 1
        if (i==size-1): 
            res.append(ls[i]) #add if next number is last 
    return  res

 

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    #Li = [4, 2, 0, -2, -4]
    result = detect_ranges(L)
    print(result)

if __name__ == "__main__":

    main()

# code is not mine, got it from course discord user @petripa
# i just modified the "L" list by "ls" in the detect_ranges function
# prior to that modification, i was failing test 1 and 5.

## Course Solution ----

def detect_ranges(L):
    if not L:           # empty list
        return L
    L = sorted(L)
#    L.sort()
    result = []
    begin, end = L[0], L[0]
    for x in L:
        if x == end:
            end += 1             # increase range
        else:
            if begin + 1 == end: # range of length 1
                result.append(begin)
            else:
                result.append((begin, end))
            begin = x
            end = begin + 1
    if begin + 1 == end: # range of length 1
        result.append(begin)
    else:
        result.append((begin, end))
    return result
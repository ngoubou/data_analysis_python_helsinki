#!/usr/bin/env python3

def positive_list(L):
    def is_positive(x):
        """Returns True if x is posiive and False if not"""
        return x > 0
    
    return list(filter(is_positive, L))

def main():
    pass

if __name__ == "__main__":
    main()

## COURSE SOLUTION ----

#def positive_list(L):
    
#    return list(filter(lambda x: x > 0, L))
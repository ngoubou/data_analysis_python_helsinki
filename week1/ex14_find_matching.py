#!/usr/bin/env python3

def find_matching(L, pattern):
    ls = []
    for i, x in enumerate(L):
        if pattern in x:
            ls.append(i)
    return ls

def main():
    pass

if __name__ == "__main__":
    main()


## COURSE SOLUTION ----

# same as mine

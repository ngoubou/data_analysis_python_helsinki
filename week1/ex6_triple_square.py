#!/usr/bin/env python3

def triple(x):
    return x * 3
    
def square(x):
    return x ** 2

def main():
    pass
    for i in range(1,11):
        s = square(i)
        t = triple(i)
        if s > t:
            break
        #print(f"triple({i})=={t} square({i})=={s}")
        print("triple({0})=={1} square({0})=={2}".format(i, t, s)) # from course solution

        #print()
    

if __name__ == "__main__":
    main()

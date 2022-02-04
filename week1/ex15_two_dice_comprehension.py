#!/usr/bin/env python3

def main():
    ls = []
    k = 0
    for i in range(1,7):
        for j in range(1,7):
            if i + j == 5:
            #print("(" + str(i) + "," + str(j) + ")")
                ls.append("(" + str(i) + "," + str(j) + ")")
                print(ls[k])
                k += 1
    pass

if __name__ == "__main__":
    main()

# Exercise 5 remake
# comparing my solution to the course, i did not at all used list comprehension
## COURSE SOLUTION ----

# def main():
#    print("\n".join(f"({a},{b})" for a in range(1, 7) for b in range(1, 7) if a + b == 5))
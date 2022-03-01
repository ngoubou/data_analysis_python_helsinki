#!/usr/bin/env python3

#print(1)
class Rational:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __repr__(self):
        return f"{self.first / self.last}"
    

def main():
    r1 = Rational(1,4)
    r2 = Rational(2, 3)
    print(r1)
    print(r2)


if __name__ == "__main__":
    main()
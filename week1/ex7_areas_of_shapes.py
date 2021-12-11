#!/usr/bin/env python3

import math
def circle(r):
    return math.pi * r**2

def rectangle(w, h):
    return w * h

def triangle(b, h):
    return b * h / 2

def main():
    
    lst = ["triangle", "rectangle", "circle"]
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if len(shape) == 0:
            break
        if not shape in lst:
            print("Unknown shape!")
        #for i in len(lst):
   
        if shape == lst[0]:
            #if shape == "triangle":
            #   print(shape)ff
            b = float(input("Give base of the triangle: "))
            h = float(input("Give height of the triangle: "))
            t = triangle(b,h)
            print(f"The area is {t:6f}")
           
        if shape == lst[1]:
            w = float(input("Give width of the rectangle: "))
            h = float(input("Give height of the rectangle: "))
            r = rectangle(w,h)
            print(f"The area is {r:6f}")
        
        if shape == lst[2]:
            r = float(input('Give radius of the circle: '))
            c = circle(r)
            print(f"The area is {c:6f}")
           
        
# if and only if the code works (ie i got correct grades), improve it using for loop

if __name__ == "__main__":
    main()

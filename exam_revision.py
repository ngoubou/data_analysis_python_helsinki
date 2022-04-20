#!/usr/bin/env python3
# def double(x):
#     "This function multiplies its argument by two hoes."
#     return x*2
# print(double(4), double(1.2), double("abc")) # It even happens to work for strings!
# print("The docstring is:", double.__doc__)
#print(help(double))

# def sum_of_squares(*t):
#     "Computes the sum of squares of arbitrary number of arguments"
#     return sum(x**2 for x in t)
# lst=[1,5,8]
# print("With list unpacked as arguments to the functions:", sum_of_squares(*lst))
# print(sum_of_squares(-2))
# print(sum_of_squares(-2,4,5))

# print(1, 2, 3, end=' |', sep=' -*- ')

# def f():            # outer function
#     b=2
#     def g():        # inner function
#         nonlocal b # Without this nonlocal statement,
#         b=3         # this will create a new local variable
#         print(b)
#     g()
#     print(b)

# print(f())


# def triple(s):
#     return s * 3

# def square(s):
#     return s**2

# for i in range(1,11):    
#     if square(i) > triple(i):
#         break
#     print(f"triple({i})=={triple(i)} square({i})=={square(i)}")
from math import pi


while True:
    shape = input("Choose a shape (triangle, rectangle, circle): ")
    if not shape:
        break
    elif shape not in ["triangle", "rectangle", "circle"]:
        print("Unknown shape!")
    
    if shape == "triangle":
        base = input("Give base of the triangle: ")
        height = input("Give height of the triangle: ")
        print(f"The area is {float(base)*float(height)/2:.6f}")
    elif shape == "rectangle":
        width = input("Give width of the rectangle: ")
        height = input("Give height of the rectangle: ")
        print(f"The area is {float(width)*float(height):.6f}")
    else:
        radius = input("Give radius of the circle: ")
        print(f"The area is {float(radius)**2*pi:.6f}")
    break

# Then it will ask for dimensions for that particular shape. 
# When all the necessary dimensions are given, it prints the area, and starts the loop all over again. 
# Use format specifier f for the area.

#What happens if you give incorrect dimensions, like giving string "aa" as radius?
# You don't have to check for errors in the input.
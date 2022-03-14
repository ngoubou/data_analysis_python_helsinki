#!/usr/bin/env python3

# Don't modify the below hack



try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    # Call the functions from here
    print(triangle.hypothenuse(5,6))
    print(triangle.area(9,8))
# i wasn't haing the full points cause i did not specify the module
# i used hypothenuse(5,6), instead of triangle.hypothenuse(5,6)
# i should use the second line cause i just use import triangle
# and not from triangle import
# the import statement is already in the file

if __name__ == "__main__":
    main()

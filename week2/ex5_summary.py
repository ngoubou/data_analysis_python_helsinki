#!/usr/bin/env python3

from statistics import mean, variance
import sys

def summary(filename):

    return (0,0,0)

def main():
    pass

if __name__ == "__main__":
    main()



# 1 read each line and convert the numbers to floats
from math import sqrt

ls = []
for i in range(1,4): 
    print(i)
    print(sys.argv[i:])


    with open(str(sys.argv[i]), "r") as f:
        for line in f:
            line = float(line.strip("\n"))
            ls.append(line)



sd = sqrt(variance(ls))
print(round(sum(ls), 6), round(mean(ls), 6), round(sd, 6))
#print(sys.argv[1:]

# DONT SPECIFY ANY FILE IN THE OPEN FUNCTION
# COMMAND LINE PARAMETERS WILL TAKE CARE OF IT

# This exercise can give two points at maximum!

# Part 1.

# Create a function called summary that gets a filename as a parameter. 
# The input file should contain a floating point number on each line of the file. 
# Make your function read these numbers and then return a triple containing the sum, average, 
# and standard deviation of these numbers for the file. 
# As a reminder, the formula for corrected sample standard deviation is 
# ∑i=1n(xi−x‾)2n−1\sqrt{\frac{\sum_{i=1}^n (x_i - \overline x)^2}{n-1}}n−1∑i=1n​(xi​−x)2​​, 
# where x‾\overline xx is the average.

# The main function should call the function summary for each filename in the list sys.argv[1:] 
# of command line parameters. (Skip sys.argv[0] since it contains the name of the current program.)

# Example of usage from the command line: python3 src/summary.py src/example.txt src/example2.txt

# Print floating point numbers using six decimals precision. The output should look like this:

# File: src/example.txt Sum: 51.400000 Average: 10.280000 Stddev: 8.904606
# File: src/example2.txt Sum: 5446.200000 Average: 1815.400000 Stddev: 3124.294045

# Part 2.

# If some line doesn’t represent a number, you can just ignore that line. 
# You can achieve this with the try-except block. An example of recovering from an exceptional situation:

#try:
#    x = float(line)           # The float constructor raises ValueError exception if conversion is no possible
#except ValueError:
    # Statements in here are executed when the above conversion fails

# We will cover more about exceptions later in the course.
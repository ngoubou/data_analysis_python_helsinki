#!/usr/bin/env python3

import sys
from statistics import mean, variance
from math import sqrt

#ls = []

def summary(filename = sys.argv[1:]):
    for i in range(3):
        with open(filename[i], "r") as f:
            ls = []
            add = []
            moyenne = []
            sd = []
            for line in f:
                try:
                    line = float(line.strip("\n"))          # The float constructor raises ValueError exception if conversion is no possible
                except ValueError:
                   continue
                ls.append(line)
    
        add.append(sum(ls))
        moyenne.append(mean(ls))
        sd.append(sqrt(variance(ls)))
    #print(add[0], moyenne[0], sd[0])

    return (add[0], moyenne[0], sd[0]) # si j'utilise list comprehension, define empty list above function

def main():
    pass
   

if __name__ == "__main__":
    main()


### -------------------------------
# Sum is not working (might have to do with sys argv)
# filename handling
# try except usage
### -------------------------------


# 1 read each line and convert the numbers to floats
#from math import sqrt

files = ["/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part02-e05_summary/src/example.txt",
"/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part02-e05_summary/src/example2.txt",
"/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part02-e05_summary/src/example3.txt"]
for i in range(3):
    with open(files[i], "r") as f:
        ls = []
        add = []
        moyenne = []
        sd = []
        for line in f:
            try:        
                line = float(line.strip("\n"))
            except ValueError:
                continue # ignore characters
                    
            ls.append(line)

    add.append(sum(ls))
    moyenne.append(mean(ls))
    sd.append(sqrt(variance(ls)))
    print(add[0], moyenne[0], sd[0])
1+1
#sd = sqrt(variance(ls))
#print(sum(ls), mean(ls), sd)
a = sys.argv[1:]
#print(type(a))
print(a)
#print(len(a))
#print(type(sys.argv[1:]))



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
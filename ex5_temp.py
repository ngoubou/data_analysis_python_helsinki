#!/usr/bin/env python3

from fileinput import filename
import sys
from statistics import mean, variance
from math import sqrt


def summary(filename):
    #for i in range(1,4):
    
    if filename:


        with open(filename, "r") as f:
            ls = []
            add = []
            moyenne = []
            sd = []
            for line in f:
            

                try:
                    line = float(line.strip("\n"))           # The float constructor raises ValueError exception if conversion is no possible
                except ValueError:
                    continue

                ls.append(line)
    
        add.append(sum(ls))
        moyenne.append(mean(ls))
        sd.append(sqrt(variance(ls)))
    
    else: # what to do if empty file
        add = [float(0)]
        moyenne = [float(0)]
        sd = [float(0)]

    #if add[0] != 0 and  moyenne[0] != 0 and  sd[0] != 0:
        #return (add[0], moyenne[0], round(sd[0], 6))
    #if add[0] == 0 and  moyenne[0] == 0 and  sd[0] == 0:
        #return f"File: file0 Sum: {float(add[0])} Average: {float(moyenne[0])} Stddev: {float(sd[0])}" #"File: file0 Sum:" + add[0]
    #else:
    return (float(add[0]), float(moyenne[0]), float(round(sd[0], 6)))

def main():
    if len(sys.argv) == 1:
        #filename = "src/example.txt"
	    print(summary(filename))
    else:
        for filename in sys.argv[1:]:
    	    print(summary(filename))

    #for i in range(7):
    #sys.argv[1:] = ["file%i" % i for i in range(8)]
    #sys.argv[1:] = ["/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part02-e05_summary/src/example.txt"] + sys.argv[1:]
    #print(sys.argv[1:])
    #print(len(sys.argv[1:]))
    #for i in range(1,7):
        #print(i)
        #print(summary(sys.argv[1:]))
    #print(summary("/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part02-e05_summary/src/example.txt"))
    #print(summary("/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part02-e05_summary/src/example2.txt"))
    #print(summary("/Users/Mamba/Library/Application Support/tmc/vscode/mooc-data-analysis-with-python-2021/part02-e05_summary/src/example3.txt"))
    #print(summary("/Users/mamba/Downloads/Data_Scientist_Path/Courses/python_helsinki/test_file.txt"))
    #print(summary(""))
    #print(summary(""))
    #print(summary(""))


    #pass

if __name__ == "__main__":
    main()


###### DISCORD --------------------------
#!/usr/bin/env python3
	 
import numpy
import re
import sys
	 
def summary(filename):
    lst = []    
    with open(filename, "r") as data:
        for x in data:
            y = re.sub("\\n", "", x)
            try:
                float(y)
            except ValueError:
                pass
            else:
                lst.append(float(y))
    
    sm = sum(lst)
    avg = sum(lst)/len(lst)
    stdev = numpy.std(lst, ddof=1)

    return (sm, avg, stdev)


def main():
    if len(sys.argv) == 1:
        filename = "src/example.txt"
        print(summary(filename))

    else:
        for filename in sys.argv[1:]:
            print(summary(filename))


if __name__ == "__main__":
    main()
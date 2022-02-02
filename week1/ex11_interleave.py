# Write function interleave that gets arbitrary number of lists as parameters. 
# You may assume that all the lists have equal length. 
# The function should return one list containing all the elements from the input lists interleaved. 
# Test your function from the main function of the program.

# Example: interleave([1,2,3], [20,30,40], ['a', 'b', 'c']) should return [1, 20, 'a', 2, 30, 'b', 3, 40, 'c'].
#  Use the zip function to implement interleave. Remember the extend method of list objects.

def interleave(*lists):
    ls = []
    for i in zip(*lists):
        ls.extend(i)

        #print(list(i))
    #return list(zip(*lists))
    return ls

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()

# easiest exercise of the whole course so far. Took me less than 30 minutes
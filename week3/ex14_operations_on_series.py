#!/usr/bin/env python3


def create_series(L1, L2):
    return (None, None)
    
def modify_series(s1, s2):
    return (None, None)
    
def main():
    return
    
if __name__ == "__main__":
    main()

# Write function create_series that gets two lists of numbers as parameters. 
# Both lists should have length 3. The function should first create two Series, s1 and s2. 
# The first series should have values from the first parameter list and have corresponding indices a, b, and c. 
# The second series should get its values from the second parameter list and have again the corresponding indices a, b, and c. 
# The function should return the pair of these Series.

# Then, write a function modify_series that gets two Series as parameters. 
# It should add to the first Series s1 a new value with index d. 
# The new value should be the same as the value in Series s2 with index b. 
# Then delete the element from s2 that has index b. 
# Now the first Series should have four values, while the second list has only two values. 
# Adding a new element to a Series can be achieved by assignment, like with dictionaries. 
# Deletion of an element from a Series can be done with the del statement.

# Test these functions from the main function. 
# Try adding together the Series returned by the modify_series function. 
# The operations on Series use the indices to keep the element-wise operations aligned. 
# If for some index the operation could not be performed, the resulting value will be NaN (Not A Number).
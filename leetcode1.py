#!/usr/bin/env python3

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

def twoSum(nums, target):
    i = 0
    j = nums[i]
    k = 0
    while True:
        try:
            #print(j + nums[i + 1])
            if j + nums[i + 1] == target:
            #print(j + nums[i + 1])
                output = [i, i + 1]
                break
            else:
            #print()
                i += 1
            
        except IndexError:
        #pass # passe au chiffre suivant
            j = nums[k + 1]
            k += 1
            i -= 1
    return output

def main():
    pass

if __name__ == "__main__":
    main()

for i, j in enumerate(['foo', 'bar', 'baz', 'bar']):
    if j == 'bar':
        #print(i)
        i
#nums = [11,2,15,7]
#nums = [2,7,11,15]
#target = 9
nums = [3,2,4]
target = 6
#nums = [3,3]
#nums = [3,2,3]
output = []
#k = 0
#for i, j in enumerate(nums):
 #   try:
  #      print(j + nums[i + 1])
   #     if j + nums[i + 1] == target:
    #        output.append(i)
     #       break
        #else:
                #print()
         #   i += 1
            
    #except IndexError:
        #pass # passe au chiffre suivant
     #   j = nums[k + 1]
      #  k += 1
       # i -= 1
    
i = 0
j = nums[i]
k = 0
while True:
    try:
        #print(j + nums[i + 1])
        if j + nums[i + 1] == target:
            #print(j + nums[i + 1])
            #print(nums.index(nums[i]))
            #print(nums.index(nums[i+1]))
            ls = list(enumerate(nums))
            #print(ls[i-1][0])
            #print(ls[i+1][0])
        
            #print(nums[i+1])
            #print(nums.index(nums[i+1]))
            #print(nums.index(3))
            #output = [nums.index(nums[i]), nums.index(nums[i+1])]
            if i != 0:
                #output = [nums.index(nums[i-1]), nums.index(nums[i+1])]
                output = [ls[i-1][0], ls[i+1][0]]
            elif i == 0:
                #output = [nums.index(nums[i]), nums.index(nums[i+1])]
                output = [ls[i][0], ls[i+1][0]]
            break
        else:
            #print()
            i += 1
            
    except IndexError:
        #pass # passe au chiffre suivant
        j = nums[k + 1]
        k += 1
        i -= 1
    #print(j+1)
    
# USE LIST COMPREHENSION instead of index method (STACKOVERFLOW)

def detect_ranges(L):
    if not L:           # empty list
        return L
    L = sorted(L)
#    L.sort()
    result = []
    begin, end = L[0], L[0]
    for x in L:
        if x == end:
            end += 1             # increase range
        else:
            if begin + 1 == end: # range of length 1
                result.append(begin)
            else:
                result.append((begin, end))
            begin = x
            end = begin + 1
    if begin + 1 == end: # range of length 1
        result.append(begin)
    else:
        result.append((begin, end))
    return result
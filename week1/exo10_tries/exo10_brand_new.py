ls = [2, 4, 5, 6, 7, 8, 10, 12, 13]
new_list = list(range(ls[0], ls[1]))
j = 1
result = []
while j + 1 < len(ls):    
    while (not all(x in ls for x in new_list)): # this got to be a while loop (does it?)
            # append to result the elements of L in new_list
            a = list(set(ls) - (set(ls) - set(new_list))) # don't want it to be a list, but either integer or tuple
            result.append(a)
            new_list = list(range(ls[j], ls[j+1]))
            #print(result)
            #print("oui")
            j += 1
    while (all(x in ls for x in new_list)):
        j += 1
        new_list = list(range(new_list[0], ls[j]))
        print("oui papa")
    #j += 1
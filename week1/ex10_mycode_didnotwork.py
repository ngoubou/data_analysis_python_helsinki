#!/usr/bin/env python3

def detect_ranges(L):
    ls = sorted(L)
    new_list = list(range(ls[0], ls[1]))
    j = 1
    #i = j - 1
    result = []

    while j + 1 < len(ls): 
    # problem with the 3 while loops when evaluating with TMC
    # for the random list it's stuck in the 2nd while loop

      
        while (not all(x in ls for x in new_list)):# and (j < len(ls)): ## CHANGER 2NDE CONDITION
            if len(new_list) == 2:
                #print(new_list[0], end = ",") 
                result.append(new_list[0]) # singletons
                if list(range(ls[j-1], ls[j])) != new_list:
                    new_list = list(range(ls[j-1], ls[j])) 
                elif (list(range(ls[j-1], ls[j])) == new_list) and (j+1 < len(ls)):
                    new_list = list(range(ls[j], ls[j+1]))
                else:
                    result.append(ls[-1])
                    break
              
                j += 1
                #i += 1
            else:
                #print("(" + str(new_list[0])+ "," + str(new_list[-1]) + ")", end = ",")
                #print(tuple((new_list[0], new_list[-1])))
                # si tous les chiffres de new_list, sauf le dernier sont dans ls
                if all(x in ls for x in new_list[:-1]):
                    couple1 = tuple((new_list[0], new_list[-1]))
                    result.append(couple1)
                #result.append(new_list[0]) 
                #result.append(new_list[-1])
                else:
                    if j > 1:
                        result.append(new_list[0])
                if j < len(ls):
                    new_list = list(range(ls[j-1], ls[j])) # if j > 1 ## j-1, j 
                else:
                    result.append(ls[-1])
                    break

                j += 1 # voir son impact sur les autres #### PROBLEME POTENTIEL
                #i += 1
            
            # else:
                    
                #if any(x in ls for x in new_list):
            
                 #   couple1 = tuple((new_list[0], new_list[-1])) # garder
                  #  result.append(couple1) # garder
                #else:
                 #   result.append(new_list)
        
        while (all(x in ls for x in new_list)):# and (j < len(ls)): # CHANGER 2NDE CONDITION
            if j < len(ls):
                new_list = list(range(new_list[0], ls[j]))
            elif j == len(ls):
                new_list = list(range(new_list[0], ls[j-1]))
            else:
                break
            j += 1
            #i += 1
            if ls[-1] == new_list[-1] + 1: # que pour le dernier élément
                #print("(" + str(new_list[0]) + "," + str(ls[-1] + 1), end = ")]")
                couple2 = tuple((new_list[0], ls[-1] + 1)) # newlist[-1] en dernier maybe
                result.append(couple2)
                break
                #result.append(new_list[0])
                #result.append(ls[-1] + 1)

        # pour le dernier élément
        #if ls[j+1] == ls[-1]:
        #    9
    #return "[{},({},{}),{},({},{})]".format(a, b, c, d, e, f)
    return result

def main():
    #L = [2, 5, 4, 8, 12, 6, 7, 10, 13] # works
    #L = [3,4,5,6] # works
    #L = [88, 89, 90, 92, 93, 94, 95, 96, 97] # works
    #L = [-2, 0, 1, 2, 3]  # works
    L = [1, 2, 4] # does not work 
    #L = [4, 2, 0, -2, -4] # list index out of range # works
    #L = [-32, -22, -85, 76, -54, -49, 79, -17, -10, 86] # works
    #L = [32, -63, 51, 23, 95, 90, -5, 29, -98, 31]
    # expected [-98, -63, -5, 23, 29, 31, 32, 51, 90, 95]
    # got      [-98, -63, -5, 23, 29, 31, 51, 90, 95]
    # Lists differ: [-98, -63, -5, 23, 29, 31, 32, 51, 90, 95] != [-98, -63, -5, 23, 29, 31, 51, 90, 95]
    result = detect_ranges(L)
    #print(L)
    print(result)

if __name__ == "__main__":
    main()

# coding=utf-8


def detect_ranges(L):
    ls = sorted(L)
    new_list = list(range(ls[0], ls[1]))
    j = 1
   
    result = []

    while j < len(ls):
      
        
        while (not all(x in ls for x in new_list)) and (j < len(ls)): 
            if len(new_list) == 2:
                #print(new_list[0], end = ",") 
                result.append(new_list[0]) # singletons
                new_list = list(range(ls[j], ls[j+1])) 
                j += 1
            else:
                #print("(" + str(new_list[0])+ "," + str(new_list[-1]) + ")", end = ",")
                result.append(new_list[0]) 
                result.append(new_list[-1])
                new_list = list(range(ls[j-1], ls[j]))
        
        while (all(x in ls for x in new_list)) and (j < len(ls)): 
            new_list = list(range(new_list[0], ls[j]))
            j += 1
            if ls[-1] == new_list[-1] + 1:
                #print("(" + str(new_list[0]) + "," + str(ls[-1] + 1), end = ")]")
                result.append(new_list[0])
                result.append(ls[-1] + 1)

    #return "[{},({},{}),{},({},{})]".format(a, b, c, d, e, f)
    return result

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    #L = [88, 89, 90, 92, 93, 94, 95, 96, 97]
    result = detect_ranges(L)
    #print(L)
    print(result)

if __name__ == "__main__":
    main()

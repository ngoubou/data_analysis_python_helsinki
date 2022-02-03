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

 

def main():

    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]

    result = detect_ranges(L)

    print(L)

    print(result)

 

if __name__ == "__main__":

    main()
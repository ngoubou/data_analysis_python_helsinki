#!/usr/bin/env python3

def extract_numbers(s):
    result = []
    s = s.split(" ")
    for i in s:
        try:
            result.append(int(i))
        except ValueError:
            try:
                result.append(float(i))
            except ValueError:
                continue
    return result

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()


# turns out i did not need regex at all 
# my solution is 98% (yeah i made up than number but it's pretty accurate) close to the course one
## Course Solution ----
#def extract_numbers(s):   
 #   result=[]
  #  for word in s.split():
   #     try:
    #        result.append(int(word))
     #   except ValueError:
      #      try:
       #         result.append(float(word))
        #    except ValueError:
         #       pass
    #return result
# # #!/usr/bin/env python3

# Write your solution here
# limit = int(input("Limit: "))
# ls = range(1, limit+1)
# limit1 = limit

# while (sum(ls) > limit1):
#     if (sum(ls) > limit) and (sum(range(1, limit)) < limit):
#         print(sum(ls))
#         break
#     limit -= 1
#     ls = range(1, limit+1)
   
#     if sum(range(1, limit)) < limit1:
#         print(sum(ls))
#         break
# The above program works, but i'm not supposed to use break

# --------------------------------------


u_n = 1
ls = [u_n]
ls2 = []
limit = 18
#un_1 = u_n + r
#a = []
for _ in range(1,limit):
    #print(i)
    #un_1 += r
    u_n += 1
    ls.append(u_n)
    if sum(ls) >= limit:
        #print(sum(ls))
        ls2.append(sum(ls))
        print("The consecutive sum: ", end = "")
        for i in ls:
            #print(f"{i}", sep=" ")
            if i != ls[-1]:
                print(i,"+",sep=" ", end=" ")
                #i = f"{str(i)} +"
                #a.append(i)
            else:
                print(i,"=", ls2[0], sep=" ")
                #i = f"{str(i)} ="
                #a.append(i)
        #print(a)
        break
            #print("+", end=" ")
        #print("=", ls2[0], sep=" ")
            #prin
        #break
#print(ls2[0])
    # un_1 = u_n + r
    # if un_1 >= limit:
    #     print(un_1)
   # un_1 += u_n #+ r
#print(u_n)

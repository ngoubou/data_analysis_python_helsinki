# # #!/usr/bin/env python3

# Write your solution here
u_n = 1
ls = [u_n]
ls2 = []
limit = int(input("Limit: "))
a = []
for _ in range(1,limit):
    u_n += 1
    ls.append(u_n)

    if sum(ls) >= limit:
        ls2.append(sum(ls))

        for i in ls:
            i = f"{i} +" if i != ls[-1] else f"{i} ="
            a.append(i)
        if sum(ls) == ls2[0]:
            print(f"The consecutive sum: {' '.join(a)} {ls2[0]}")


# My code is sooooo bad

## Course Solution ----
limit = int(input("Limit: "))
number = 1
summ = 1
numbers = "1"
while summ < limit:
    number += 1
    summ += number
    # note that f-string can also be used like this
    numbers += f" + {number}"
print(f"The consecutive sum: {numbers} = {summ}")
   
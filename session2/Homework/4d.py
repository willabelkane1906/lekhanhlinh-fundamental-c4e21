n = int(input("enter a number:"))
for x in range(0, n):
    if (x % 2 == 0):
        print("x", end =" " )
    else:
        print("*", end =" ")
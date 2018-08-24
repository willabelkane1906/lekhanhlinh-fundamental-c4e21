clothes = ['T-shirt','Sweater']


while True:
    command = input( "welcome to our shop,what do you want?(C,R,U,D)")
    if command == "C":
        ask=input("Enter new item?")
        clothes.append(ask)
        print("Our items:", end ="")
        print(*clothes, sep =",")
      
    elif command == "R":
        print("our items:", end ="")
        print(*clothes, sep =",")

    elif command == "U":
        position = int(input("position to update?"))
        clothes_update = input("enter new item?")
        clothes[position] = clothes_update
        print("Our items:", end ="")
        print(*clothes, sep =",")
    else:
        dele = int(input("item to delete ?"))
        clothes.pop(dele-1)
        print("our items:", end ="")
        print( *clothes, sep =",")

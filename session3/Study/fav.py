
fav = ['sprited away', 'howl', '5cm/s']
for index, item in enumerate(fav):
    print(index + 1, ".", item, sep ="")

while True:
    command = input("what do you want?(C,R,U,D)")
    if command.upper() == "C":
        ask=input("item to add?")
        fav.append(ask)
        print(fav)
    elif command == "R":
        print(fav)
    elif command == "U":
        position = int(input("position to update?"))
        fav_update = input("your new fav?")
        fav[position] = fav_update
        print(fav)
    else:
        a = int(input("fav posiotion you want to get rich of?"))
        fav.pop(a)
        print(fav)








 


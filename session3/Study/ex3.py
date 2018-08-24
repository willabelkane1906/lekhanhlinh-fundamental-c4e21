fav = ['sprited away', 'howl', '5cm/s']
for index, item in enumerate(fav):
    print(index + 1, ".", item, sep ="")
print("*" *10)
dele = int(input("fav posiotion you want to get rich of?"))

fav.pop(dele - 1)
print("*" *10)
for index, item in enumerate(fav):
    print(index + 1, ".", item, sep ="")

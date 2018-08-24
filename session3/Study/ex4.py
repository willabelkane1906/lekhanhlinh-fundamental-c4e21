fav = ['sprited away', 'howl', '5cm/s']
for index, item in enumerate(fav):
    print(index + 1, ".", item, sep ="")
print("*" *10)
dele = input("fav posiotion you want to get rich of?")
if dele in fav:
    fav.remove(dele)
else:
    print("huhh")


# fav.remove(dele)
print("*" *10)
for index, item in enumerate(fav):
    print(index + 1, ".", item, sep ="")



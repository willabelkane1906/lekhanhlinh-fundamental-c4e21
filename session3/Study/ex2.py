fav = ['sprited away', 'howl', '5cm/s']
for index, item in enumerate(fav):
    print(index + 1, ".", item, sep ="")
print("*" *10)


# fav_size = len(fav)
# for i in range(fav_size):
#     print(i + 1, ".",fav[i])

position = int(input("position you want to update?"))
fav_update = input("your new fav?")
fav[position] = fav_update

# fav_size = len(fav)
# for i in range(fav_size):
#     print(i + 1, ".",fav[i])






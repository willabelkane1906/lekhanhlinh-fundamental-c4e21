menu_items = ["books", "marathons", "tea"]
print(*menu_items, sep=",")
ask = input("what is your favorite books?")

menu_items.append(ask)
print(*menu_items, sep =",")
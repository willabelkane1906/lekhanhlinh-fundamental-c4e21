inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
for k, v in inventory.items():
    print(k, " ", v)
print()
name = inventory['backpack']
name.remove('dagger')
for k, v in inventory.items():
    print(k, " ", v)
print()
inventory['gold'] += 50
for k, v in inventory.items():
    print(k, " ", v)
prices = {    "banana": 4,    "apple": 2,    "orange": 1.5,    "pear": 3}
stock = {    "banana": 6,    "apple": 0,    "orange": 32,    "pear": 15}

for k,v in prices.items():
    if k in stock:
        print(k)
        print("price:", prices[k])
        print("stock:", stock[k])    
        print()     
    else:
        print()

total = 0
for k in prices.keys():
    cost = prices[k] * stock[k]         
    total += cost
    print(k, "cost:", cost)
print("Total:",total)









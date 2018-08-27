# person = ["doctor",18, "i need", "call me"]
# print(person)

# person = {

# }

# print(person)

# person = {
#     "name": "Flo"
# }

# print(person)

person = {
    "name": "Rich",
    "age" : 21,
    "city": "NewYork",
}
for k in person.keys():
    print(k)
for v in person.values():
    print(v)

for k, v in person.items():
    print(k,";", v)

# print(person["status"])
# person["status"] = "complicated"
# print(person)
# del person["age"]
# print(person)

# print(person)
# print(person["name"])
# person["name"] = "Cabot"
# print(person)
# key = "city"
# print(person[key])
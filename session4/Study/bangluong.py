from collections import OrderedDict
r1 = {    "STT" : 1,
    "Tên" : "Huy",
    "Mức lương" : 25,
    "Số giờ làm" : 14,
}
r2 = {
    "STT" : 2,
    "Tên" : "Hòa",
    "Mức lương" : 20,
    "Số giờ làm" : 17,
}
r3 = {
    "STT" : 3,
    "Tên" : "Tâm",
    "Mức lương" : 15,
    "Số giờ làm" : 10,
}
list_luong = [r1, r2, r3]

# print(list_luong)
# for x in list_luong:
#     print(x)
total_wage = 0
wage_list = []
for luong in list_luong:
    name = luong["Tên"]
    hour = luong["Số giờ làm"]
    level = luong["Mức lương"]
    # print(hour, level)
    wage_info = OrderedDict({
        "Tên" : name,
        "Mức lương" : hour * level,
    })
    wage_list.append(wage_info)
    wage = hour * level
    total_wage += wage
    print(luong["Tên"], ":", wage)
    print("Total:", total_wage)

import pyexcel
pyexcel.save_as(records=wage_list , dest_file_name="sample2.xlsx")





   
yob = int(input("your year of birth?"))
age = 2018 - yob
print("your age:", age)

if age < 10:
    print("baby")
# Dòng số 6 chỉ chạy khi vế sau if đúng
elif age < 18:
    print("teenager")
else:
    print("adult")
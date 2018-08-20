a = int(input("nhap so a"))
b = int(input("nhap so b"))
c = int(input("nhap so c"))

delta = b**2 - 4*a*c
a_2 = a*2

if delta > 0:
    delta_sqrt = delta**0.5
    X1 = (-b + delta_sqrt)/a_2
    X2 = (-b - delta_sqrt)/a_2
    print("phuong trình có hai nghiem", X1, X2)
elif delta == 0:
    X = -b/a_2
    print("phuong trinh co nghiem duy nhat", X)

else:
    print("phuong trinh vo nghiem")

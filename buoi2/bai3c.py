import math


a = float(input("Nhập hệ số a (a ≠ 0): "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
elif delta == 0:
    x = -b / (2*a)
    print(f"phương trình có một nghiệm kép: x = {x}")
else:
    print("phương trình vô nghiệm")
#Kiểm tra tam giác:
#Viết chương trình yêu cầu người dùng nhập vào 3 số nguyên dương. Kiểm tra xem 3 số đó có tạo thành tam giác hay không? Nếu có thì đó là tam giác gì?(Cân, đều, vuông, nhọn, tù)
a = int(input("Nhập độ dài cạnh thứ nhất: "))
b = int(input("Nhập độ dài cạnh thứ hai: "))
c = int(input("Nhập độ dài cạnh thứ ba: "))
a, b, c = sorted([a, b, c])
if a+b<=c:
    print("k phải tam giác")
else:
    if a==b and a==c and b==c:
        print("tam giác đều")
    elif a==b and a!=c or a==c and a!=b or b==c and b!=a:
        print("tam giác cân")
    if a*a+b*b==c*c:
        print("tam giác vuông")
    elif a*a+b*b<c*c:
        print("tam giác tù")
    else: print("tam giác nhọn")

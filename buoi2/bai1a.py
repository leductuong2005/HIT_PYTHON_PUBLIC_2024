a=int(input("nhập số nguyên dương : "))
sum=0
while (a>0):

    sum+=a%10
    a=int(a/10)

print("tổng các chữ số là : ",sum)
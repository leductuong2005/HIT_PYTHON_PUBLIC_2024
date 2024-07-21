import math
a=int(input())
dem=0
while(a>1):
    dem+=1
    a=a/2
if a%2==1:
    dem+=1
print("cần ",dem," bit để biểu diễn ở hệ nhị phân")

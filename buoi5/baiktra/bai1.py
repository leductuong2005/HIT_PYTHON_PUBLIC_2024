lst=map(int,input().split())
tuple1=tuple(lst)
print (tuple1)
count=0
for i in tuple1:
    if i==i+1 :
        count+1
        if count(i)%5==0 and count(i)%10!=0:
            print (i)
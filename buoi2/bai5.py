n=int(input())
for i in range (1,n+1):
    sum=0
    j=i
    while (i>0):
            a=i%10
            i=int(i/10)
            sum+=a**3
    if(sum==j):
         print (sum, " ")
       
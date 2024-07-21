n=int(input())
s=0
for i in range (1,2*n+2):
    if(i%2==0):s=s-i
    else:s=s+i
print(s)
mystr=input()
mylist=[]
for char in mystr: 
    if char == " ":continue
    else :
        mylist.append(char)

mylist=set(mylist)
print(mylist)

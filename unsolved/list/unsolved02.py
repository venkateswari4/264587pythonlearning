l=[1,2,3,4,5,6]
s=l[0]
for i in range(0,len(l)-1):
    l[i]=l[i+1]
l[len(l)-1]=s
print('new list')
print(l)
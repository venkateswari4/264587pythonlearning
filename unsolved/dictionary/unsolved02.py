l=['a','b','c']
d=a={}
for i in l:
    a[i]={}
    a=a[i]
print(d)
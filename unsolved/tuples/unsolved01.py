tup=(1,1,2,2,4,5,6,7,7,8)
print('repeated elements')
s=set()
for i in tup:
    if tup.count(i) > 1:
        s.add(i)
print(s)

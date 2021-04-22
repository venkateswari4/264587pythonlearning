i=10
#i=10.9
#i=3+4j
#i="rama"
#i=0
if i==0:
    print("Zero")
elif(isinstance(i,int)):
    print("Integer")
elif(isinstance(i,float)):
    print("Float")
elif(isinstance(i,complex)):
    print("Complex")
elif(isinstance(i,str)):
    print("String")

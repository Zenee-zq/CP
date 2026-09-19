e=int(input())
z=[]
for i in range(1,e*4+1):
    if i%4!=0:
        z.append(i)
    else:
        z.append("PUM")
for c in z:
    if c=="PUM":
        print(c)
    else:
        print(c,end=" ")
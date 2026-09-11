n=int(input())
z=[]
for i in range(1,n+1):
    if n%i==0:
        z.append(i)
for i in z:
    print(i)

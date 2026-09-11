n=int(input())
prime=[]

for c in range(2,n+1):
    found = False
    for i in range(2,c):
        if c%i==0:
            found = True
    if found==False:
        prime.append(c)

for i in prime:
    print(i,end=" ")
    
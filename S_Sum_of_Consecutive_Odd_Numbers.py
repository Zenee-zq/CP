e=int(input())
i=0
while i<e:
    n=list(map(int,input().split()))
    n.sort()
    z=[]
    d=0
    for c in range(n[0]+1,n[1]):
        if c%2!=0:
           d+=c 
    print(d)
    i+=1
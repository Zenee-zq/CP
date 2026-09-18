e=int(input())
n=list(map(int,input().split()))
for i in n:
    if i > 0:
        d=n.index(i)
        n[d]=1
    if i < 0:
        f=n.index(i)
        n[f]=2
for i in n:
    print(i,end=" ")
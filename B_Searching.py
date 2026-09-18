e=input()
c=list(map(int,input().split()))
f=int(input())
u=False
for i in c:
    if i == f:
        u = True
if u:
    print(c.index(f))
else:
    print(-1)
e=int(input())
z=0
for i in range(e):
    x=list(map(int,input().split()))
    if x.count(1)>=2:
        z+=1
print(z)
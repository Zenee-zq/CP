e=input()
c=list(map(int,input().split()))
o=0
for i in c:
    if i > o:
        o=i
print(o)
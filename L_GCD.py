n=list(map(int,input().split()))
a=n[0]
b=n[1]
p=[]
for i in range(1,a+1):
    if a%i==0:
        p.append(i)
for i in range(1,b+1):
    if b%i==0:
        p.append(i)
v=[]
for c in p:
    found= False
    if p.count(c)==2:
        found= True
    if found ==True:
        v.append(c)
o = 0
for i in v:
    if i >o:
        o = i
print(o)
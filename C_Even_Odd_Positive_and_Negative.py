i=int(input())
c=list(map(int,input().split()))
e,o,p,n=0,0,0,0


for i in c:
    if i % 2 == 0:
        e += 1
    if i % 2 != 0:
        o+= 1
    if i >0:
        p+=1
    if i <0:
        n+=1

print('Even:',e)
print('Odd:',o)
print('Positive:',p)
print('Negative:',n)
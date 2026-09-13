def lucky(n):
    c= str(n)
    for ch in c:
        if ch!='4' and ch!='7':
            return False
    return True

a,b= map(int,input().split())
found= False
for i in range(a,b+1):
    if lucky(i):
        print(i,end=' ')
        found = True
if found== False:
    print("-1")
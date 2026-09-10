i=int(input())
c=list(map(int,input().split()))
e,o,p,n=0,0,0,0


for i in c:
    if i % 2 == 0:
        print('even:',e)
        e += 1
    elif i % 2 != 0:
        print('odd:',i)
    elif i >0:
        print('positive:',i)
    elif i <0:
        print('negative',i)
    else:
        print('zero',i)

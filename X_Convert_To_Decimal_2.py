e=int(input())
i=0
while i<e:
    x=int(input())
    z=f"{x:b}"
    x=int(z.replace("0",""),2)
    print(x)
    i+=1
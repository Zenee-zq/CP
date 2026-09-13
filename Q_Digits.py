e=int(input())
i=0
while i<e:
    x=input()
    s=list(x)
    for c in s[::-1]:
        print(c,end=" ")
    print(" ")
    i+=1
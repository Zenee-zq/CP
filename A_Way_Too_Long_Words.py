e=int(input())
i=0
while i<e:
    x=list(input())
    if len(x)>10:
        print(f"{x[0]}{len(x)-2}{x[len(x)-1]}")
    else:
        print("".join(x))
    i+=1
w=int(input())
x=0
for i in range(w):
    e=input()
    if e=="++X" or e=="X++":
        x+=1
    elif e=="X--" or e== "--X":
        x-=1
print(x)
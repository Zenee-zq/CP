s=input()
e=int(input())
f=map(int,input().split())
for i in range(e):
    for c in f:
        print(s*c)
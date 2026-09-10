c=int(input())
found = True
for i in range(2,c):
    if c%i==0:
        found = False

if not found:
    print("NO")
else:
    print("YES")
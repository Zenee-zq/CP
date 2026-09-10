c=int(input())
found = False


for i in range(1,c+1):
    if i % 2 == 0:
        print(i)
        found = True

if not found:
    print("-1")
    
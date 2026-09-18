e=int(input())
A=list(map(int,input().split()))
for i in range(0,len(A)):
    if A[i]<=10:
        print("A"+"["+str(i)+"]","=",A[i])
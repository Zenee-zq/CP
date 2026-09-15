r=0
while r==0:
        n=list(map(int,input().split()))
        if n[0] <=0 or n[1] <=0:
          break
        if n[0]>n[1]:
          a,b=n[0],n[1]
        else:
            a,b=n[1],n[0]
        s=0
        for i in range(b,a+1):
            s=s+i
            print(i,end=" ")
        print("sum ="+str(s))

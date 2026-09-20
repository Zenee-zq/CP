e=int(input())
for i in range(1,e+1):
    print(" "*(e-i)+"*"*(2*i-1))
for i in range(0,e+1):
    print(" "*(i)+"*"*(2*(e-i)-1))